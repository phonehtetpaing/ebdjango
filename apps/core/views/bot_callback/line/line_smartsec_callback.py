# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
import time
import mimetypes

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

# import views
from apps.core.views.bot_parts.line.end_user_info import *
from apps.core.views.bot_common.message_sequence import *
from apps.core.views.bot_common.start_event_reservation import *
from apps.core.views.bot_common.payload_converter import *


@csrf_exempt
def callback(request, code=None):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            end_user_vendor_info_dict = get_end_user_vendor_info(request.path)
            parser = WebhookParser(end_user_vendor_info_dict["line_verify_token"])
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        text = None
        payload = None

        for event in events:
            user_id = event.source.user_id

            if isinstance(event, JoinEvent):
                print('DEBUG Join EVENT')

                end_user_vendor_info_dict = get_end_user_vendor_info(request.path)
                if end_user_vendor_info_dict:
                    create_or_update_auth_user(user_id, end_user_vendor_info_dict)

                # get end_user_info
                end_user_info = get_end_user_info(request.path, user_id)
                # start auto reply
                #todo get started with welcome flow
                payload = "GET_STARTED_PAYLOAD"
                update_message_sequence(payload, text, end_user_info)

            elif isinstance(event, PostbackEvent):
                print('DEBUG Postback EVENT', event, PostbackEvent)
                # Save postback data
                payload = event.postback.data
                print(payload)
                # todo sets payload and then.. waits?
                set_payload(user_id, payload)
                time.sleep(settings.SLEEP_SEC)

            elif isinstance(event, MessageEvent):
                print('DEBUG Message EVENT', event, MessageEvent)
                event_type = event.message.type
                try:
                    if event_type == 'text':
                        text = event.message.text
                        if text == "hello world":
                            return HttpResponse()

                        if text in settings.LINE_GET_STARTED_TEXT:
                            text = None
                            end_user_vendor_info_dict = get_end_user_vendor_info(request.path)
                            if end_user_vendor_info_dict:
                                create_or_update_auth_user(user_id, end_user_vendor_info_dict)

                            # get end_user_info
                            end_user_info = get_end_user_info(request.path, user_id)
                            # start auto reply
                            payload = "GET_STARTED_PAYLOAD"
                            update_message_sequence(payload, text, end_user_info)

                        end_user_info = get_end_user_info(request.path, user_id)
                        time.sleep(settings.SLEEP_SEC)
                        payload = get_payload(user_id)

                        # start auto reply
                        if payload is not None and "__event_" in payload:
                            # text input
                            event_controller_from_text(end_user_info, text)
                            payload = get_payload(user_id)
                            print("payload -------", payload)
                            print(end_user_info["reservation_data"])
                            # reservation flow
                            start_event_reservation(payload, text, end_user_info)
                        elif text and end_user_info["end_user_obj"].end_user_state.cd == "WAIT_INPUT":
                            update_message_sequence(payload, text, end_user_info)
                        elif payload:
                            update_message_sequence(payload, None, end_user_info)

                    elif event_type == 'sticker':
                        # Do Nothing
                        pass

                    elif event_type == 'image':
                        pass

                    elif event_type == 'video':
                        pass

                    elif event_type == 'audio':
                        pass

                    elif event_type == 'location':
                        pass

                    elif event_type == 'imagemap':
                        pass

                    else:
                        pass

                except Exception as e:
                    print('Message Event Exception: %r' % e)

            elif isinstance(event, FollowEvent):
                print('DEBUG FOLLOW EVENT')
                end_user_vendor_info_dict = get_end_user_vendor_info(request.path)
                if end_user_vendor_info_dict:
                    create_or_update_auth_user(user_id, end_user_vendor_info_dict)

                # get end_user_info
                end_user_info = get_end_user_info(request.path, user_id)
                # start auto reply
                payload = "GET_STARTED_PAYLOAD"
                update_message_sequence(payload, text, end_user_info)

            elif isinstance(event, UnfollowEvent):
                print(event)

            elif isinstance(event, LeaveEvent):
                print(event)
                print("Bye!")

        return HttpResponse()
    else:
        return HttpResponseBadRequest()