# -*- coding: utf-8 -*-
import json
from datetime import datetime
import time
from django.utils.translation import gettext

# import models
from apps.core.models.event_category import EventCategory
from apps.core.models.event import Event
from apps.core.models.event_reservation import EventReservation
from apps.core.models.event_reservation_status import EventReservationStatus

# import views
from apps.core.views.messaging_adapter_chat.text_send_message import *
from apps.core.views.messaging_adapter_chat.button_select_message import *
from apps.core.views.google_utils.google_calendar_search_available_time_by_keyword import *
from apps.core.views.google_utils.google_calendar_insert import *


def show_event_category(payload_text, text, end_user_info):

    event_categories = EventCategory.objects.filter(vendor_branch_id=end_user_info["vendor_branch_id"], is_public=1, is_delete=0).order_by("display_order_num")

    quick_reply_list = []
    for event_category in event_categories:
        # check if there are any options possible at all
        events = Event.available.filter(event_category=event_category).count()

        if events >= 1:
            payload = "__event_EVENT_CATEGORY" + "@" + str(event_category.id)

            quick_reply_dict = {
                "content_type": "text",
                "title": event_category.name,
                "payload": payload
            }

            quick_reply_list.append(quick_reply_dict)

    # if no events are available, send an info message instead
    if len(quick_reply_list) > 0:
        param = {
            "text": "選択してください。",
            "quick_replies": quick_reply_list
        }

        button_select_message(end_user_info, param)
    else:
        param = {
            "text": gettext("Currently there are no events being held. We will inform you of new events as they appear.")
        }
        text_send_message(end_user_info, param)


def show_event(payload_text, text, end_user_info):
    event_categoy_id = payload_text.split("@")[1]
    event_category = EventCategory.objects.filter(id=event_categoy_id, vendor_branch_id=end_user_info["vendor_branch_id"], is_public=1, is_delete=0).first()
    events = Event.available.filter(event_category=event_category).all()

    quick_reply_list = []
    for event in events:
        payload = "__event_EVENT_EVENT" + "@" + str(event.id)

        quick_reply_dict = {
            "content_type": "text",
            "title": event.name,
            "payload": payload
        }

        quick_reply_list.append(quick_reply_dict)

    param = {
                "text": "選択してください",
                "quick_replies": quick_reply_list
            }

    button_select_message(end_user_info, param)


def ask_first_question(payload_text, text, end_user_info):

    event_id = payload_text.split("@")[1]
    event = Event.objects.filter(id=event_id).first()

    if event.event_category.is_user_select_event_minutes:
        # Save Event Info.
        reservation_data_dict = {
            "event_category_id": event.event_category.id,
            "event_id": event_id,
            "payload": payload_text
        }
        end_user = end_user_info["end_user_obj"]
        end_user.reservation_data_json = json.dumps(reservation_data_dict)
        end_user.save()

        text = """
ご希望の日を年月日(8桁)で入力して下さい。
[例]
2018年4月3日 ⇛ 20180403
            """
        param = {"text": text}
        text_send_message(end_user_info, param)

    else:
        if event.event_category.is_gcal_use:
            # Use available time of Google Calendar
            google_event_list = get_available_time_by_keyword(end_user_info, event_id)

            quick_reply_list = []
            for g_event in google_event_list:
                # Example:
                # {'summary': 'G-Nm 02', 'start_time': '2018-06-16T12:45:00+09:00',
                #  'end_time': '2018-06-16T14:30:00+09:00', 'location': 'location G-Nm 02', 'time_zone': 'Asia/Tokyo'}

                yyyymmdd = g_event["start_time"].split("T")[0]
                start_hhmm = g_event["start_time"].split("T")[1]
                end_hhmm = g_event["end_time"].split("T")[1]
                event_time_str = yyyymmdd + "/" + start_hhmm + "/" + end_hhmm
                payload = "__event_CONFIRM" + "@" + str(event.id) + "@" + event_time_str

                print(payload)

                # Create Title of quick reply text
                yyyymmdd_list = yyyymmdd.split("-")
                start_hhmm_list = start_hhmm.split(":")
                end_hhmm_list = end_hhmm.split(":")
                title = yyyymmdd_list[1] + "/" + yyyymmdd_list[2] + " " + " " + start_hhmm_list[0] + ":" + start_hhmm_list[1] + "〜" + end_hhmm_list[0] + ":" + end_hhmm_list[1]

                quick_reply_dict = {
                    "content_type": "text",
                    "title": title,
                    "payload": payload
                }

                quick_reply_list.append(quick_reply_dict)

            text = """
【{event_name}】
　{event_description}

ご希望の日程を選んでください。
             """.format(event_name=event.name, event_description=event.description).strip()

            param = {
                "text": text,
                "quick_replies": quick_reply_list
            }

            button_select_message(end_user_info, param)

        else:
            # Not use google calendar
            yyyymmdd = event.start_dt.strftime('%Y-%m-%d')
            start_hhmm = event.start_dt.strftime('%H:%M')
            end_hhmm = event.end_dt.strftime('%H:%M')

#             text = """
# 【{event_name}】
# 　{event_description}
#
# [日時]
# 　{yyyymmdd}
# 　{start_hhmm} 〜 {end_hhmm}
#              """.format(event_name=event.name, event_description=event.description, yyyymmdd=yyyymmdd, start_hhmm=start_hhmm, end_hhmm=end_hhmm).strip()

            text = """
【{event_name}】
[日時]
　{start_hhmm} 〜 {end_hhmm}
                         """.format(event_name=event.name, event_description=event.description, yyyymmdd=yyyymmdd,
                                    start_hhmm=start_hhmm, end_hhmm=end_hhmm).strip()

            quick_reply_dict_confirm = {
                "content_type": "text",
                "title": "確定",
                "payload": "__event_COMPLETE@" + event_id
            }

            quick_reply_dict_no = {
                "content_type": "text",
                "title": "もう一度やり直す",
                "payload": "__event_GET_STARTED"
            }

            quick_reply_list = [quick_reply_dict_confirm, quick_reply_dict_no]

            param = {
                "text": text,
                "quick_replies": quick_reply_list
            }

            button_select_message(end_user_info, param)


def confirm_schedule(payload_text, text, end_user_info):
    # Example: paload_text
    # __event_CONFIRM @ 5 @ 2018 - 06 - 16 / 12: 45:00 + 09: 00 / 14:30: 00 + 09: 00

    payload_list = payload_text.split("@")
    date_list = payload_list[2].split("/") #2018 - 06 - 16 / 12: 45:00 + 09: 00 / 14:30: 00 + 09: 00
    event_id = payload_list[1]
    yyyymmdd = date_list[0]
    start_hhmm = date_list[1].split("+")[0]
    end_hhmm = date_list[2].split("+")[0]

    event = Event.objects.filter(id=event_id).first()
    event_time_str = yyyymmdd + "/" + start_hhmm + "/" + end_hhmm
    payload = "__event_COMPLETE" + "@" + str(event.id) + "@" + event_time_str

    # Create Text
    start_hhmm_list = start_hhmm.split(":")
    end_hhmm_list = end_hhmm.split(":")
    text_start_hhmm = start_hhmm_list[0] + ":" + start_hhmm_list[1]
    text_end_hhmm = end_hhmm_list[0] + ":" + end_hhmm_list[1]

# LINE ERROR  {"message": "must not be longer than 40 characters", "property": "template/title"}
#     text = """
# 【{event_name}】
# 　{event_description}
#
# [日時]
# 　{yyyymmdd}
# 　{start_hhmm} 〜 {end_hhmm}
#          """.format(event_name=event.name, event_description=event.description, yyyymmdd=yyyymmdd,
#                     start_hhmm=text_start_hhmm, end_hhmm=text_end_hhmm).strip()

    text = """
{event_name}
　{yyyymmdd} 
　{start_hhmm} 〜 {end_hhmm}
             """.format(event_name=event.name, yyyymmdd=yyyymmdd,
                        start_hhmm=text_start_hhmm, end_hhmm=text_end_hhmm).strip()

    quick_reply_dict_confirm = {
        "content_type": "text",
        "title": "確定",
        "payload": payload
    }

    quick_reply_dict_no = {
        "content_type": "text",
        "title": "もう一度やり直す",
        "payload": "__event_GET_STARTED"
    }

    quick_reply_list = [quick_reply_dict_confirm, quick_reply_dict_no]

    param = {
        "text": text,
        "quick_replies": quick_reply_list
    }

    button_select_message(end_user_info, param)


def complete_schedule(payload_text, text, end_user_info):
    google_event_dict = None
    event_reservation = None
    event_id = payload_text.split("@")[1]
    event_reservation_status = EventReservationStatus.objects.order_by('display_order_num').first()
    event = Event.objects.filter(id=event_id).first()
    end_user = end_user_info["end_user_obj"]

    if end_user.last_name:
        end_user_last_name = end_user.last_name
    else:
        end_user_last_name = " "

    if end_user.first_name:
        end_user_first_name = end_user.first_name
    else:
        end_user_first_name = " "

    user_full_name = end_user_last_name + " " + end_user_first_name + " 様"

    if event.event_category.is_gcal_use:
        # Use Google Calendar
        payload_list = payload_text.split("@")
        date_list = payload_list[2].split("/")  # 2018 - 06 - 16 / 12: 45:00 + 09: 00 / 14:30: 00 + 09: 00
        yyyymmdd = date_list[0]
        start_datetime_str = yyyymmdd + " " + date_list[1]
        end_datetime_str = yyyymmdd + " " + date_list[2]
        start_datetime = datetime.datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M:%S')
        end_datetime = datetime.datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M:%S')

        try:
            event_reservation = EventReservation()
            event_reservation.vendor_branch_id = end_user_info["vendor_branch_id"]
            event_reservation.event = event
            event_reservation.end_user = end_user
            event_reservation.reservation_date = start_datetime.strftime('%Y-%m-%d')
            event_reservation.reservation_start_time = start_datetime.strftime('%H:%M:%S')
            event_reservation.reservation_end_time = end_datetime.strftime('%H:%M:%S')
            event_reservation.event_reservation_status = event_reservation_status
            event_reservation.save()

        except Exception as e:
            print('%r' % e)
            return None

    else:
        # Not use google calendar
        event_reservation = EventReservation.objects.filter(vendor_branch_id=end_user_info["vendor_branch_id"], event=event, end_user=end_user).first()
        if event_reservation:
            regist_dt = event_reservation.regist_dt.strftime('%Y-%m-%d %H:%M')

            text = """
{user_full_name}、
既に予約済みです。当日お待ちしております！
------
【予約日時】
{date}
　{start_time} 〜 {end_time}
------
【予約受付日】
{regist_dt}
------
※キャンセルする場合、{tel} までご連絡下さい。
             """.format(user_full_name=user_full_name, date=event_reservation.reservation_date,
                        start_time=event_reservation.reservation_start_time,
                        end_time=event_reservation.reservation_end_time, regist_dt=regist_dt, tel=event.tel)

            param = {
                "text": text,
            }

            text_send_message(end_user_info, param)
            return None

        else:
            event_reservation = EventReservation()
            event_reservation.vendor_branch_id = end_user_info["vendor_branch_id"]
            event_reservation.event = event
            event_reservation.end_user = end_user
            event_reservation.reservation_date = event.start_dt.strftime('%Y-%m-%d')
            event_reservation.reservation_start_time = event.start_dt.strftime('%H:%M:%S')
            event_reservation.reservation_end_time = event.end_dt.strftime('%H:%M:%S')
            event_reservation.event_reservation_status = event_reservation_status
            event_reservation.save()

    start_time_list = event_reservation.reservation_start_time.split(":")
    start_time_text = start_time_list[0] + ":" + start_time_list[1]
    end_time_list = event_reservation.reservation_end_time.split(":")
    end_time_text = end_time_list[0] + ":" + end_time_list[1]

    # [common] THANK YOU message
    text = """
{user_full_name}、
ご予約ありがとうございます。当日お待ちしております。
【予約日時】
{date}
　{start_time} 〜 {end_time}

※キャンセルする場合、{tel} までご連絡下さい。
     """.format(user_full_name=user_full_name, date=event_reservation.reservation_date, start_time=start_time_text, end_time=end_time_text, tel=event.tel)

    if event.is_gcal_set:

        try:
            start_time = str(event_reservation.reservation_date) + "T" + str(event_reservation.reservation_start_time) + "+09:00"
            end_time = str(event_reservation.reservation_date) + "T" + str(event_reservation.reservation_end_time) + "+09:00"

            google_event_dict = {
                "summary": "[" + event.name+ "]" + user_full_name,
                "start_time": start_time,
                "end_time": end_time,
                "location": event.location,
                "timezone": "Asia/Tokyo",
            }

            calendar_url = insert_event_schedule(end_user_info, google_event_dict)
            event_reservation.gcal_url = calendar_url
            event_reservation.save()

        except Exception as e:
            print('%r' % e)
            return None

    param = {
        "text": text,
    }

    text_send_message(end_user_info, param)
