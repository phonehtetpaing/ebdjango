# -*- coding: utf-8 -*-
import json
import time

# import models
from apps.core.models.event_category import EventCategory
from apps.core.models.vendor_event_settings import VendorEventSettings
from apps.core.models.end_user_line import EndUserLINE

# import views
from apps.core.views.bot_common.end_user_story_history import *
from apps.core.views.messaging_adapter_chat.text_send_message import *
from apps.core.views.messaging_adapter_chat.image_send_message import *
from apps.core.views.messaging_adapter_chat.carousel_send_message import *
from apps.core.views.messaging_adapter_chat.button_select_message import *
from apps.core.views.google_utils.google_calendar_available_schedule import *


def event_controller_from_text(end_user_info, text):
    end_user = end_user_info["end_user_obj"]
    if end_user.reservation_data_json:
        reservation_data_dict = json.loads(end_user.reservation_data_json)
    else:
        return None

    event_category_id = reservation_data_dict["event_category_id"]
    payload = reservation_data_dict["payload"]

    if ("event_EVENT_EVENT" in payload) and ("yyyymmdd" not in reservation_data_dict):
        reservation_data_dict["yyyymmdd"] = text
        end_user.reservation_data_json = json.dumps(reservation_data_dict)
        end_user.save()

        ask_event_minutes(end_user_info, event_category_id)


def ask_event_minutes(end_user_info, event_category_id):
    # for LINE
    end_user_line = EndUserLINE.objects.filter(end_user=end_user_info["end_user_obj"]).first()
    if end_user_line:
        end_user_line.payload = "__event_USER_INPUT_MINUTES"
        end_user_line.save()
        time.sleep(settings.SLEEP_SEC)

    event_category = EventCategory.objects.filter(id=event_category_id, vendor_branch_id=end_user_info["vendor_branch_id"], is_delete=0).first()
    event_minutes_list = event_category.event_minutes_csv.split(",")

    quick_reply_list = []
    for event_minutes in event_minutes_list:
        payload = "__event_USER_MINUTES" + "@" + str(event_minutes)

        quick_reply_dict = {
            "content_type": "text",
            "title": str(event_minutes) + "分",
            "payload": payload
        }

        quick_reply_list.append(quick_reply_dict)

    param = {
        "text": "ご希望の時間を選択してください",
        "quick_replies": quick_reply_list
    }

    button_select_message(end_user_info, param)


def show_event_available_time(payload, end_user_info):
    end_user = end_user_info["end_user_obj"]
    reservation_data_dict = json.loads(end_user.reservation_data_json)
    reservation_data_dict["minutes"] = payload.split("@")[1]
    end_user.reservation_data_json = json.dumps(reservation_data_dict)
    end_user.save()

    event_category = EventCategory.objects.filter(id=reservation_data_dict["event_category_id"]).first()
    event = Event.objects.filter(id=reservation_data_dict["event_id"]).first()
    vendor_event_settings = VendorEventSettings.objects.filter(vendor_branch=end_user.vendor_branch).first()

    off_day_list = vendor_event_settings.day_off_csv.split(",")
    start_hhmmss = datetime.time.strftime(vendor_event_settings.work_start_time, '%H:%M:%S')
    end_hhmmss = datetime.time.strftime(vendor_event_settings.work_end_time, '%H:%M:%S')

    buffer_period = vendor_event_settings.buffer_period
    mtg_period = reservation_data_dict["minutes"]
    yyyymmdd = reservation_data_dict["yyyymmdd"]

    param_dict = {
        "off_day": off_day_list,
        "start_hhmmss": start_hhmmss,
        "end_hhmmss": end_hhmmss,
        "buffer_period": buffer_period,
        "mtg_period": mtg_period,
    }

    time_min_list = list(yyyymmdd)
    time_max_list = list(yyyymmdd)

    yyyymmdd = time_min_list[0] + time_min_list[1] + time_min_list[2] + time_min_list[3] \
               + "-" + time_min_list[4] + time_min_list[5] \
               + "-" + time_min_list[6] + time_min_list[7]

    # Create Payload

    param_time_min = time_min_list[0] + time_min_list[1] + time_min_list[2] + time_min_list[3] \
                     + "-" + time_min_list[4] + time_min_list[5] \
                     + "-" + time_min_list[6] + time_min_list[7]

    param_time_max = time_max_list[0] + time_max_list[1] + time_max_list[2] + time_max_list[3] \
                     + "-" + time_max_list[4] + time_max_list[5] \
                     + "-" + time_max_list[6] + time_max_list[7]

    param_time_min = param_time_min + 'T00:00:00.123456+0900'
    param_time_max = param_time_max + 'T23:59:59.999243Z'

    if event_category.is_gcal_available_time:
        available_schedule_list = get_available_schedule(end_user_info, param_dict, param_time_min, param_time_max)

    else:
        available_schedule_list = get_available_schedule_with_keyword(end_user_info, param_dict, param_time_min, param_time_max, event.gcal_keyword)

    if len(available_schedule_list) == 0:
        return None

    try:
        # 選択した日付の時間を取得する
        quick_reply_list = []
        for ac in available_schedule_list:
            if ac["date"] == yyyymmdd:
                for time in ac["time"]:
                    start_time_list = time["start"].split(":")
                    end_time_list = time["end"].split(":")
                    start_hhmm = start_time_list[0] + ":" + start_time_list[1]
                    end_hhmm = end_time_list[0] + ":" + end_time_list[1]

                    event_time_str = yyyymmdd + "/" + start_hhmm + ":00" + "/" + end_hhmm + ":00"
                    payload = "__event_CONFIRM" + "@" + str(reservation_data_dict["event_id"])+ "@" + event_time_str

                    quick_reply_dict = {
                        "content_type": "text",
                        "title": start_hhmm + "〜" + end_hhmm,
                        "payload": payload,
                    }

                    quick_reply_list.append(quick_reply_dict)

        if len(quick_reply_list) >= 8:
            quick_reply_list = quick_reply_list[0:8]

        param = {
            "text": "ご希望の時間帯を選んでください",
            "quick_replies": quick_reply_list
        }

        button_select_message(end_user_info, param)

    except Exception as e:
        print('%r' % e)
        return None