import json, requests
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
import boto3
import time
import threading
import csv
import os
import datetime
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from apps.core.models.summary_log_vendor_users import SummaryLogVendorUsers
from apps.core.models.summary_log_end_users import SummaryLogEndUsers


# TODO: active CSRF
@csrf_exempt
def load_to_rds(request):

    sns_message_json = request.body
    sns_message_dict = json.loads(sns_message_json)

    if sns_message_dict["Type"] == "SubscriptionConfirmation":
        print("SubscriptionConfirmation")

        subscribe_url = sns_message_dict["SubscribeURL"]
        requests.post(subscribe_url, headers={"Content-Type": "text/plain"})

        return HttpResponse()

    elif sns_message_dict["Type"] == "Notification":
        print("Notification")

        # get uploaded file data
        print("===== getting the uploaded athena output files =======")
        message_dict = json.loads(sns_message_dict["Message"])
        record_list = message_dict["Records"]
        object_list = []
        for record in record_list:
            tmp_dict = {
                # "event_time": record["eventTime"],
                "Bucket": record["s3"]["bucket"]["name"],
                "Key": record["s3"]["object"]["key"],
            }
            object_list.append(tmp_dict)

        print("object_list =======")
        print(object_list)

        print(object_list)
        if len(object_list) == 0:
            print("No object")
            return HttpResponse()

        elif len(object_list) == 1:
            object = object_list[0]

        else:
            object = object_list[0]

        try:
            # # Thread: download --> insert ---> upload --> delete
            print("Thread Start ==============")
            args_list = [object]
            t = threading.Thread(target=__load_csv__, args=args_list)
            t.setDaemon(True)
            t.start()
            print("Thread End ==============")
            return HttpResponse()

        except Exception as e:
            print("ERROR: Threading")
            print('%r' % e)
            return HttpResponse()

    else:
        print("failed....")
        return HttpResponse()


def __load_csv__(*arguments):

    object = arguments[0]
    key = object["Key"]

    # Download from S3
    download_file = download_from_csv(key)
    if download_file is None:
        print("Failed: download_file")
        return False

    # insert
    result = insert_log_table(download_file)
    if result is False:
        print("Failed: insert_log_table")
        return False

    # upload to s3
    target_bucket = settings.APP_LOGS_S3_BUCKET
    result = copy_key_to_load(object, target_bucket)
    if result is False:
        print("Failed: upload to s3")
        return False

    # Delete local csv
    if download_file is not None:
        os.remove(download_file)

    print("END: __load_csv__")

    return True


def download_from_csv(key):
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name='ap-northeast-1'
        )

        mode_prefix = "local"
        if settings.MODE == "DEV":
            mode_prefix = "development"

        elif settings.MODE == "STAGING":
            mode_prefix = "staging"

        elif settings.MODE == "PRODUCTION":
            mode_prefix = "production"

        # Get File name
        key_list = key.split("/")
        download_file_name = key_list[3]

        # Specify user_prefix (end or vendor)
        if "end_user" in key:
            user_prefix = "end_user"
        else:
            user_prefix = "vendor_user"

        download_file = settings.BASE_DIR + "/apps/core/views/api/stats/load_csv/" + mode_prefix + "/" + user_prefix + "/" + download_file_name
        s3_client.download_file(settings.APP_LOGS_S3_BUCKET, key, download_file)

        return download_file

    except Exception as e:
        print('%r' % e)
        return None


def insert_log_table(download_file):
    try:
        csv_file = open(download_file, "r", encoding="utf8", errors="", newline="")
        f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"',
                           skipinitialspace=True)

        if "end_user" in download_file:
            for row in f:
                try:
                    summary_log_end_users = SummaryLogEndUsers()
                    summary_log_end_users.level = row["level"]
                    # TODO: ValueError('unconverted data remains: .000',)
                    log_dt_str = row["log_dt"].rstrip(".000")
                    summary_log_end_users.log_dt = datetime.datetime.strptime(log_dt_str, '%Y-%m-%d %H:%M:%S')
                    summary_log_end_users.service_id = int(row["app_id"])
                    summary_log_end_users.vendor_branch_id = int(row["vendor_branch_id"])
                    summary_log_end_users.vendor_id = int(row["vendor_id"])

                    end_user_id = None
                    if not (row["end_user_id"] is None or row["end_user_id"] == ""):
                        end_user_id = int(row["end_user_id"])

                    summary_log_end_users.end_user_id = end_user_id

                    device_type = None
                    if not (row["device_type"] is None or row["device_type"] == ""):
                        device_type = int(row["device_type"])
                    summary_log_end_users.device_type = device_type
                    summary_log_end_users.device_family = row["device_family"]
                    summary_log_end_users.os_family = row["os_family"]
                    summary_log_end_users.os_version = row["os_version"]
                    summary_log_end_users.browser_family = row["browser_family"]
                    summary_log_end_users.browser_version = row["browser_version"]
                    summary_log_end_users.ip_address = row["ip_address"]
                    # summary_log_end_users.server_host = row["server_host"]
                    summary_log_end_users.status_code = row["status_code"]
                    summary_log_end_users.content_type = row["content_type"]
                    summary_log_end_users.http_referer = row["http_referer"]
                    summary_log_end_users.action_type = row["action_type"]
                    summary_log_end_users.params = row["params"]
                    summary_log_end_users.endpoint = row["endpoint"]

                    message_block_id = None
                    if not (row["message_block_id"] is None or row["message_block_id"] == ""):
                        message_block_id = int(row["message_block_id"])
                    summary_log_end_users.message_block_id = message_block_id

                    summary_log_end_users.message_progress = row["message_progress"]
                    summary_log_end_users.save()
                except Exception as e:
                    print('%r' % e)

        elif "vendor_user" in download_file:
            for row in f:
                try:
                    summary_log_vendor_users = SummaryLogVendorUsers()
                    summary_log_vendor_users.level = row["level"]
                    log_dt_str = row["log_dt"].rstrip(".000")
                    summary_log_vendor_users.log_dt = datetime.datetime.strptime(log_dt_str, '%Y-%m-%d %H:%M:%S')
                    vendor_user_id = None
                    if not (row["vendor_user_id"] is None or row["vendor_user_id"] == ""):
                        vendor_user_id = int(row["vendor_user_id"])
                    summary_log_vendor_users.vendor_user_id = vendor_user_id
                    summary_log_vendor_users.device_type = int(row["device_type"])
                    summary_log_vendor_users.device_family = row["device_family"]
                    summary_log_vendor_users.os_family = row["os_family"]
                    summary_log_vendor_users.os_version = row["os_version"]
                    summary_log_vendor_users.browser_family = row["browser_family"]
                    summary_log_vendor_users.browser_version = row["browser_version"]
                    summary_log_vendor_users.ip_address = row["ip_address"]
                    # summary_log_vendor_users.server_host = row["server_host"]
                    summary_log_vendor_users.status_code = row["status_code"]
                    summary_log_vendor_users.content_type = row["content_type"]
                    summary_log_vendor_users.http_referer = row["http_referer"]
                    summary_log_vendor_users.action_type = row["action_type"]
                    summary_log_vendor_users.params = row["params"]
                    summary_log_vendor_users.endpoint = row["endpoint"]
                    summary_log_vendor_users.save()
                except Exception as e:
                    print('%r' % e)

        csv_file.close()

        return True

    except Exception as e:
        print('%r' % e)
        return False


def copy_key_to_load(object, target_bucket):
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name='ap-northeast-1'
        )

        # get csv file name
        key = object["Key"]
        key_list = key.split("/")
        target_prefix = "load_to_rds/" + key_list[1] + "/" + key_list[2] + "/" + key_list[3]
        # upload load_to_csv
        s3_client.copy(object, target_bucket, target_prefix)

        return True

    except Exception as e:
        print('%r' % e)
        return False
