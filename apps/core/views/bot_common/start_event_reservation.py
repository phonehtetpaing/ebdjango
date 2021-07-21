# -*- coding: utf-8 -*-
import json
import time
import traceback

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_line import EndUserLINE

# import views
from apps.core.views.bot_common.event_reservation_common import *
from apps.core.views.bot_common.event_reservation_with_google_calendar import *


def start_event_reservation(payload_text, text, end_user_info):

    try:
        if payload_text == "__event_GET_STARTED":
            end_user = end_user_info["end_user_obj"]
            end_user = EndUser.objects.filter(id=end_user.id).first()
            end_user.reservation_data_json = None
            end_user.save()
            end_user_line = EndUserLINE.objects.filter(end_user=end_user).first()
            if end_user_line:
                end_user_line.payload = None
                end_user_line.save()
                time.sleep(settings.SLEEP_SEC)

            show_event_category(payload_text, text, end_user_info)

        elif "__event_EVENT_CATEGORY" in payload_text:
            show_event(payload_text, text, end_user_info)

        elif "__event_EVENT_EVENT" in payload_text:
            ask_first_question(payload_text, text, end_user_info)

        elif "__event_USER_MINUTES" in payload_text:
            show_event_available_time(payload_text, end_user_info)

        elif "__event_CONFIRM" in payload_text:
            confirm_schedule(payload_text, text, end_user_info)

        elif "__event_COMPLETE" in payload_text:
            complete_schedule(payload_text, text, end_user_info)

        return True

    except Exception as e:
        print('start_event_reservation Exception: %r' % e)
        print(traceback.format_exc())
        return False
