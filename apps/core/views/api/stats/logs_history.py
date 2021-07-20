import json, requests
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.http.response import JsonResponse
import boto3
import time
import datetime
import pytz
import threading
import csv
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from apps.core.models.logs_history import LogsHistory


# TODO: active CSRF
@csrf_exempt
def insert_history(request):
    # lambda function runs this method to get event datetime
    interval = 5

    try:
        # get datetime
        now = datetime.datetime.now()
        now_str = now.strftime('%Y-%m-%d %H')
        now_str_minute = now.strftime('%M')
        f_min = get_flat_minute(now_str_minute)
        f_now = now_str + ":" + f_min + ":00"
        now_dt = datetime.datetime.strptime(f_now, '%Y-%m-%d %H:%M:%S')

        log_history = LogsHistory.objects.filter(is_athena_query=False, is_delete=False).order_by("regist_dt").first()

        if log_history:
            event_start_dt = log_history.event_end_dt
            event_end_dt = now_dt

        else:
            log_history_athena = LogsHistory.objects.filter(is_athena_query=True, is_delete=False).order_by("-regist_dt").first()
            if log_history_athena:
                # aware→naive
                event_start_dt = log_history_athena.event_end_dt.astimezone(pytz.timezone('Asia/Tokyo')).replace(tzinfo=None)
                event_end_dt = now_dt

                print("debug: datetime check....")
                print(event_start_dt)
                print(event_end_dt)

                if event_start_dt >= event_end_dt:
                    data = {
                        "event_start_dt": None,
                        "event_end_dt": None
                    }
                    print(data)
                    return JsonResponse(data)
            else:
                event_start_dt = now_dt - datetime.timedelta(minutes=interval)
                event_end_dt = now_dt

        # Insert History
        log_history = LogsHistory()
        log_history.event_start_dt = event_start_dt
        log_history.event_end_dt = event_end_dt
        log_history.is_athena_query = False
        log_history.save()

        # Change to UTC from JST for cloudwatchlogs export
        event_start_dt = event_start_dt.replace(tzinfo=datetime.timezone.utc)
        event_end_dt = event_end_dt.replace(tzinfo=datetime.timezone.utc)

        data = {
            "event_start_dt": event_start_dt.strftime('%Y-%m-%d %H:%M:%S'),
            "event_end_dt": event_end_dt.strftime('%Y-%m-%d %H:%M:%S')
        }

        print(data)

        data = {
            "event_start_dt": int(event_start_dt.timestamp()),
            "event_end_dt": int(event_end_dt.timestamp())
        }

        print("insert data ====")
        print(data)

        return JsonResponse(data)

    except Exception as e:
        data = {
            "event_start_dt": None,
            "event_end_dt": None
        }
        print('%r' % e)
        return JsonResponse(data)


def get_flat_minute(minutes):
    min = int(minutes)
    f_min = "00"

    if min >= 0 and min <=9:
        f_min = "00"

    elif min >=10 and min <=19:
        f_min = "10"

    elif min >=20 and min <=29:
        f_min = "20"

    elif min >=30 and min <=39:
        f_min = "30"

    elif min >=40 and min <=49:
        f_min = "40"

    elif min >=50 and min <=59:
        f_min = "50"

    return f_min
