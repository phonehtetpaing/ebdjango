# -*- coding:utf-8 -*-
import json, requests
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
import datetime
import time
import boto3
import threading
import csv
import os
import re
from django.conf import settings

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from apps.core.models.logs_history import LogsHistory


@csrf_exempt
def run_query(request):
    sns_message_json = request.body
    sns_message_dict = json.loads(sns_message_json)

    if sns_message_dict["Type"] == "SubscriptionConfirmation":
        print("SubscriptionConfirmation")

        subscribe_url = sns_message_dict["SubscribeURL"]
        requests.post(subscribe_url, headers={"Content-Type": "text/plain"})

        return HttpResponse()

    elif sns_message_dict["Type"] == "Notification":
        print("Notification")

        athena_client = boto3.client(
            'athena',
            aws_access_key_id=settings.AWS_ATHENA_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_ATHENA_SECRET_ACCESS_KEY,
            region_name='ap-northeast-1'
        )

        log_history = LogsHistory.objects.filter(is_athena_query=False, is_delete=False).order_by(
            "-event_end_dt").first()

        # Run query of vendor_user
        try:

            if log_history:
                # # Thread: download --> insert ---> upload --> delete
                print("Thread Start (vendor_user) ==============")
                sql = get_sql("vendor_user")

                args_list = [athena_client, "vendor_user", sql]
                vendor_t = threading.Thread(target=__run_query__, args=args_list)
                vendor_t.setDaemon(True)
                vendor_t.start()
                print("Thread End ==============")

                print("Thread Start (end_user) ==============")
                sql = get_sql("end_user")

                args_list = [athena_client, "end_user", sql]
                end_t = threading.Thread(target=__run_query__, args=args_list)
                end_t.setDaemon(True)
                end_t.start()
                print("Thread End ==============")

                vendor_t.join()
                end_t.join()
                print("ALL Threads End ==============")
                # Athena Query FLG: ON
                event_end_dt = log_history.event_end_dt
                update_log_histories = LogsHistory.objects.filter(is_athena_query=False, is_delete=False,
                                                                  event_end_dt__lte=event_end_dt).all()
                for log in update_log_histories:
                    log.is_athena_query = True
                    log.save()

                print(" === END: Run Athena Query ==== ")

            else:
                print(" === No Datetime Data for Query =====")

            return HttpResponse()

        except Exception as e:
            print("ERROR: Threading")
            print('%r' % e)
            return HttpResponse()


def __run_query__(*arguments):
    print("run quesry")
    athena_client = arguments[0]
    prefix = arguments[1]
    sql = arguments[2]

    RETRY_COUNT = 10

    try:
        cloudwatch_logs_s3_bucket = settings.APP_LOGS_S3_BUCKET
        dt_now = datetime.datetime.now()
        directory_prefix = dt_now.strftime('%Y-%m-%d')
        output_location = "s3://" + cloudwatch_logs_s3_bucket + "/athena_output/" + prefix + "/" + directory_prefix + "/"

        print("=======  athena query result output_location  =======")
        print(output_location)

        response = athena_client.start_query_execution(
            QueryString=sql,
            QueryExecutionContext={
                'Database': 'smartby'
            },
            ResultConfiguration={
                'OutputLocation': output_location
            }
        )

        query_execution_id = response["QueryExecutionId"]

        print(response)
        print(query_execution_id)

        # get execution status
        for i in range(1, 1 + RETRY_COUNT):

            # get query execution
            query_status = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
            query_execution_status = query_status['QueryExecution']['Status']['State']

            if query_execution_status == 'SUCCEEDED':
                print("STATUS:" + query_execution_status)
                break

            if query_execution_status == 'FAILED':
                raise Exception("STATUS:" + query_execution_status)

            else:
                print("STATUS:" + query_execution_status)
                time.sleep(i)

        return True

    except Exception as e:
        print("ERROR:" + prefix + "::"+ str(e))
        return False

def get_sql(user_prefix):

    # user_prefix: end_user / vendor_user
    if user_prefix == "vendor_user":
        sql_file = settings.BASE_DIR + "/apps/core/views/api/stats/athena_query/select_vendor_user_data.sql"
    else:
        sql_file = settings.BASE_DIR + "/apps/core/views/api/stats/athena_query/select_end_user_data.sql"

    # get start_dt, end_dt
    log_history = LogsHistory.objects.filter(is_athena_query=False, is_delete=False).order_by("event_start_dt").first()
    event_start_dt = log_history.event_start_dt
    log_history = LogsHistory.objects.filter(is_athena_query=False, is_delete=False).order_by("-event_end_dt").first()
    event_end_dt = log_history.event_end_dt

    event_start_dt_str = event_start_dt.strftime('%Y-%m-%d %H:%M:%S')
    event_end_dt_str = event_end_dt.strftime('%Y-%m-%d %H:%M:%S')
    where = " and time >= \'" + event_start_dt_str + "\' and " + "time <= \'" + event_end_dt_str + "\'"

    sql_base = open(sql_file, 'r').read()

    # Set Athena Database
    if settings.MODE == "DEV":
        mode = "development"

    elif settings.MODE == "STAGING":
        mode = "staging"

    elif settings.MODE == "PRODUCTION":
        mode = "production"

    else:
        mode = "local"

    logs_db = "logs_" + mode
    sql_base_exec = sql_base.format(logs_db=logs_db)

    sql = str(sql_base_exec) + where
    print("sql ======== ")
    print(sql)

    return sql
