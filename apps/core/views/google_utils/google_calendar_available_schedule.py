# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os
import ast

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from django.conf import settings

# import views
from apps.core.views.google_utils.google_calendar_oauth import *

# import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.event import Event


import datetime
import pytz


def get_available_schedule(end_user_info, param_dict, time_min=None, time_max=None):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """

    """ 例： param_dict 
    param_dict = {
        "off_day": [1,2], 休業曜日
        "start_hhmmss": '09:00:00', #就業開始時刻
        "start_hhmmss": '19:00:00', #就業終了時刻 
        "buffer_period": 30, #予定間のバッファ時間（分）※既に予定が入っている場合、その前後30分は予約できないようにする
        "mtg_period": 60, #エンドユーザが希望する面談時間（分）
    }
    """

    # credentials = get_credentials(company_id)
    # http = credentials.authorize(httplib2.Http())
    # service = discovery.build('calendar', 'v3', http=http)
    vendor_branch = end_user_info["vendor_branch"]
    credentials_dict = ast.literal_eval(vendor_branch.google_credentials)
    credentials = google.oauth2.credentials.Credentials(**credentials_dict)
    service = discovery.build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('----------------')
    print(now)
    print(type(now))
    print('----------------')
    mex_result = 20

    if time_min is None or time_max is None:
        print('Getting the upcoming events: ' + mex_result)

        eventsResult = service.events().list(
            calendarId='primary', timeMin=now, maxResults=mex_result, singleEvents=True,
            orderBy='startTime').execute()

    else:
        print("time_min:" + time_min)
        print(type(time_min))
        print("time_min:" + time_max)
        eventsResult = service.events().list(
            calendarId='primary', timeMin=time_min, timeMax=time_max, singleEvents=True,
            orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    # print(events)

    # TODO: 終日設定していた場合の対応

    # 初期値設定
    tmp_datetime = None
    tmp_start_day = None
    booked_datetime_dict = {
        "date": None,
        "booked_time": []
    }
    booked_datetime_list = []
    # 日程取得処理に考慮すべきパラメータ
    off_days_list = param_dict["off_day"]
    buffer_period = param_dict["buffer_period"]
    mtg_period = int(param_dict["mtg_period"])

    if not events:
        print('No upcoming events found.')
        tmp_dict = {
            "date": time_min.split('T')[0],
            # 勤務時間として00:00:01-00:00:02と想定する TODO: この設定でよいか？
            # "booked_time": [{"start": param_dict["start_hhmmss"], "end": param_dict["end_hhmmss"]}]
            "booked_time": [{"start": "00:00:01", "end": "00:00:02"}]
        }
        booked_datetime_list.append(tmp_dict)

    else:
        minum_datetime = datetime.datetime.now() + datetime.timedelta(minutes=buffer_period)

        try:
            # STEP1: スケジュール済みの予定を取得する {"date":<日付YYYYMMDD>, "booked_time": [{"start":<時刻>, "end":<時刻>}, ・・・]
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                start_yyyymmdd = start.split('T')[0]
                try:
                    start_hhmmss = (start.split('T')[1]).split('+')[0]
                except Exception as e:
                    # TODO: 業務開始時刻を設定
                    start_hhmmss = param_dict["start_hhmmss"]

                end = event['end'].get('dateTime', event['end'].get('date'))
                end_yyyymmdd = end.split('T')[0]
                try:
                    end_hhmmss = (end.split('T')[1]).split('+')[0]
                except Exception as e:
                    # TODO: 業務終了時刻を設定
                    end_hhmmss = param_dict["end_hhmmss"]

                start_yyyymmdd_datetime = datetime.datetime.strptime(start_yyyymmdd, '%Y-%m-%d')
                start_day = start_yyyymmdd_datetime.weekday()

                if tmp_datetime != start_yyyymmdd:
                    if tmp_datetime is not None:
                        # 休暇は含めない
                        if tmp_start_day not in off_days_list and tmp_datetime_datetime >= minum_datetime:
                            booked_datetime_list.append(booked_datetime_dict)

                        booked_datetime_dict = {
                            "date": None,
                            "booked_time": []
                        }
                    booked_datetime_dict["date"] = start_yyyymmdd
                booked_datetime_dict["booked_time"].append({"start": start_hhmmss, "end": end_hhmmss})
                print("booked_datetime_dict >>>>>>>>")
                print(booked_datetime_dict)

                tmp_datetime_datetime = start_yyyymmdd_datetime
                tmp_datetime = start_yyyymmdd
                tmp_start_day = start_day

                print(start, end, event['summary'])
                # print(start_hhmmss)
                # print(end_hhmmss)

            start_yyyymmdd_datetime = datetime.datetime.strptime(booked_datetime_dict["date"], '%Y-%m-%d')
            start_day = start_yyyymmdd_datetime.weekday()
            # 休暇は含めない
            print("休暇")
            print(start_day)
            print(off_days_list)
            if start_day not in off_days_list:
                booked_datetime_list.append(booked_datetime_dict)

            print("booked_datetime_list >>>>>>")
            print(booked_datetime_list)

        except Exception as e:
            print("STEP1: error-----")
            print('%r' % e)

    # STEP2: 予約可能な時間を出す
    try:
        available_datetime_list = []
        for bdl in booked_datetime_list:
            available_datetime_dict = {
                "date": bdl["date"],
                "time": []
            }
            # TODO: 業務時間はDBから取得
            base_start = param_dict["start_hhmmss"]
            base_end = param_dict["end_hhmmss"]

            for bt in bdl["booked_time"]:
                print("????? debug ")
                print(bdl)
                print(bt)
                # print(bdl["date"] + " " + base_start)

                base_start_time = datetime.datetime.strptime(bdl["date"] + " " + base_start, '%Y-%m-%d %H:%M:%S')
                base_end_time = datetime.datetime.strptime(bdl["date"] + " " + base_end, '%Y-%m-%d %H:%M:%S')
                start_time = datetime.datetime.strptime(bdl["date"] + " " + bt["start"], '%Y-%m-%d %H:%M:%S')
                end_time = datetime.datetime.strptime(bdl["date"] + " " + bt["end"], '%Y-%m-%d %H:%M:%S')

                # 業務時間外に予定が入っている場合、業務時間内が予約可能とする
                if (start_time <= base_start_time and end_time < base_start_time) or (start_time > base_end_time and end_time >= base_end_time):
                    delta = ((base_end_time - base_start_time).total_seconds()) / 60
                    if delta >= mtg_period:
                        mtg_start_datetime = base_start_time

                        for m in range(int(delta/mtg_period)):
                            mtg_end_datetime = mtg_start_datetime + datetime.timedelta(minutes=mtg_period)
                            if mtg_end_datetime <= base_end_time:
                                available_datetime_dict["time"].append(
                                    {
                                        "start": mtg_start_datetime.strftime('%H:%M:%S'),
                                        "end": mtg_end_datetime.strftime('%H:%M:%S'),
                                    }
                                )
                            mtg_start_datetime = mtg_end_datetime

                        # 予約可能な時間リストへ追加
                        available_datetime_list.append(available_datetime_dict)
                        continue

                if start_time >= base_start_time and end_time <= base_end_time:
                    if end_time <= base_end_time: #業務終了時間内か判定
                        # ユーザ選択した時間で分割して、辞書に登録
                        # end-startの差分（分）を求める
                        tmp_end_datetime = start_time - datetime.timedelta(minutes=buffer_period)
                        delta = ((tmp_end_datetime - base_start_time).total_seconds())/60
                        # end-startをmtg_periodで分割
                        if delta >= mtg_period:
                            mtg_start_datetime = base_start_time

                            for m in range(int(delta/mtg_period)):
                                mtg_end_datetime = mtg_start_datetime + datetime.timedelta(minutes=mtg_period)
                                if mtg_end_datetime <= tmp_end_datetime:
                                    available_datetime_dict["time"].append(
                                        {
                                            "start": mtg_start_datetime.strftime('%H:%M:%S'),
                                            "end": mtg_end_datetime.strftime('%H:%M:%S'),
                                        }
                                    )
                                mtg_start_datetime = mtg_end_datetime

                        # 予約可能な時間リストへ追加
                        available_datetime_list.append(available_datetime_dict)

                tmp_end_datetime = end_time + datetime.timedelta(minutes=buffer_period)
                base_start = tmp_end_datetime.strftime('%H:%M:%S')

            # 最後のスケジュール済み時間以降＆営業時間内であれば、予約可能時間に追加する
            bdl_booked_time_list = bdl["booked_time"]
            last_dbl_time = bdl_booked_time_list[len(bdl_booked_time_list) - 1]
            last_dbl_date = bdl["date"]
            print("last_dbl >>>>>>>>>")
            print(last_dbl_time)
            print(last_dbl_date)
            base_start_time = datetime.datetime.strptime(last_dbl_date + " " + base_start, '%Y-%m-%d %H:%M:%S')
            base_end_time = datetime.datetime.strptime(last_dbl_date + " " + base_end, '%Y-%m-%d %H:%M:%S')
            start_time = datetime.datetime.strptime(last_dbl_date + " " + last_dbl_time["start"], '%Y-%m-%d %H:%M:%S')
            end_time = datetime.datetime.strptime(last_dbl_date + " " + last_dbl_time["end"], '%Y-%m-%d %H:%M:%S')

            if end_time <= base_end_time:
                delta = ((base_end_time - end_time).total_seconds()) / 60
                # devided by mtg_period
                if delta >= mtg_period:
                    mtg_start_datetime = end_time + datetime.timedelta(minutes=buffer_period)

                    for m in range(int(delta/mtg_period)):
                        mtg_end_datetime = mtg_start_datetime + datetime.timedelta(minutes=mtg_period)
                        if mtg_end_datetime <= base_end_time and mtg_start_datetime >= base_start_time:
                            available_datetime_dict["time"].append(
                                {
                                    "start": mtg_start_datetime.strftime('%H:%M:%S'),
                                    "end": mtg_end_datetime.strftime('%H:%M:%S'),
                                }
                            )
                        mtg_start_datetime = mtg_end_datetime

                    print("test>>>>>>>>>>>>>>")
                    print(available_datetime_dict["time"])

                # add available time list
                available_datetime_list.append(available_datetime_dict)

    except Exception as e:
        print("STEP2: error-----")
        print('%r' % e)

    try:
        # STEP3: Data cleaning (remove empty date)
        for i, adl in enumerate(available_datetime_list):
            if not adl["time"]:
                available_datetime_list[i] = "__delete"

        while '__delete' in available_datetime_list:
            available_datetime_list.remove('__delete')

        # STEP4: Data cleaning (distinct by time)
        for i, adl in enumerate(available_datetime_list):
            time_list_uniq = []
            for time in adl["time"]:
                if time not in time_list_uniq:
                    time_list_uniq.append(time)

            available_datetime_list[i]["time"] = time_list_uniq

        # STEP5: Data cleaning (distinct by date)
        available_datetime_list_uniq = []
        for i, adl in enumerate(available_datetime_list):
            if adl not in available_datetime_list_uniq:
                available_datetime_list_uniq.append(adl)

        print("available_datetime_list >>>> ")
        print(len(available_datetime_list))
        print(available_datetime_list)

        # return available_datetime_list
        return available_datetime_list_uniq

    except Exception as e:
        print("STEP3:error-----")
        print('%r' % e)


def get_available_schedule_with_keyword(end_user_info, param_dict, time_min=None, time_max=None, search_keyword=None):
    vendor_branch = end_user_info["vendor_branch"]
    credentials_dict = ast.literal_eval(vendor_branch.google_credentials)
    credentials = google.oauth2.credentials.Credentials(**credentials_dict)
    service = discovery.build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('----------------')
    print(now)
    print(type(now))
    print('----------------')
    mex_result = 20

    if time_min is None or time_max is None:
        print('Getting the upcoming events: ' + mex_result)

        eventsResult = service.events().list(
            calendarId='primary', timeMin=now, maxResults=mex_result, singleEvents=True,
            orderBy='startTime').execute()

    else:
        print("time_min:" + time_min)
        print(type(time_min))
        print("time_min:" + time_max)
        eventsResult = service.events().list(
            calendarId='primary', timeMin=time_min, timeMax=time_max, singleEvents=True,
            orderBy='startTime').execute()
    events = eventsResult.get('items', [])


    if not events:
        print('No upcoming events found.')
        return None

    else:
        try:
            # STEP1: スケジュール済みの予定を取得する {"date":<日付YYYYMMDD>, "booked_time": [{"start":<時刻>, "end":<時刻>}, ・・・]
            available_datetime_list = []
            date_str = time_min.split('T')[0]
            available_datetime_dict = {
                "date": date_str,
                "time": [],
            }

            for event in events:

                if event["summary"] == search_keyword:
                    # 時刻データを取得・算出
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    start_yyyymmdd = start.split('T')[0]
                    try:
                        start_hhmmss = (start.split('T')[1]).split('+')[0]
                    except Exception as e:
                        # Set Work Start Time
                        start_hhmmss = param_dict["start_hhmmss"]

                    end = event['end'].get('dateTime', event['end'].get('date'))
                    end_yyyymmdd = end.split('T')[0]
                    try:
                        end_hhmmss = (end.split('T')[1]).split('+')[0]
                    except Exception as e:
                        # Set Work End Time
                        end_hhmmss = param_dict["end_hhmmss"]

                    start_yyyymmdd_datetime = datetime.datetime.strptime(start_yyyymmdd, '%Y-%m-%d')

                    available_datetime_dict["time"].append({"start": start_hhmmss, "end": end_hhmmss})

            mtg_datetime_list = []
            for time in available_datetime_dict['time']:
                start_datetime = datetime.datetime.strptime(date_str + " " + time["start"], '%Y-%m-%d %H:%M:%S')
                end_datetime = datetime.datetime.strptime(date_str + " " + time["end"], '%Y-%m-%d %H:%M:%S')

                mtg_period = int(param_dict["mtg_period"])
                delta = ((end_datetime - start_datetime).total_seconds()) / 60
                if delta >= mtg_period:
                    mtg_start_datetime = start_datetime

                    for m in range(int(delta/mtg_period)):
                        mtg_end_datetime = mtg_start_datetime + datetime.timedelta(minutes=mtg_period)
                        if mtg_end_datetime <= end_datetime:
                            mtg_datetime_dict = {
                                "start": mtg_start_datetime.strftime('%H:%M:%S'),
                                "end": mtg_end_datetime.strftime('%H:%M:%S'),
                            }
                            mtg_datetime_list.append(mtg_datetime_dict)

                        mtg_start_datetime = mtg_end_datetime

            available_datetime_dict['time'] = mtg_datetime_list
            available_datetime_list.append(available_datetime_dict)
            print("available_datetime_list")
            print(available_datetime_list)

            return available_datetime_list

        except Exception as e:
            print("STEP3:error-----")
            print('%r' % e)
