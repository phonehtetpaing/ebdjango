# -*- coding: utf-8 -*-
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# import view
from apps.core.views.bot_parts.fbms.access_util import *
from apps.core.views.bot_parts.fbms.end_user_info import *
from apps.core.views.bot_common.message_sequence import *
from apps.core.views.bot_common.start_event_reservation import *
from apps.core.views.bot_common.event_reservation_with_google_calendar import *

from apps.core.views.logging.end_user_logging import end_user_logger


import traceback


class MessageView(generic.View):

    def get(self, request, *args, **kwargs):
        print("Received GET request")
        access_url_path_dict = get_access_url_path_dict(self.request.path)
        access_url_part = access_url_path_dict["vendor_access_url"]

        verify_token = get_verify_token(access_url_part)

        # for debugging
        if self.request:
            print(self.request)

        else:
            print("No request")

        if self.request.GET['hub.verify_token'] == verify_token:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))

        # Initialize
        end_user_info = None
        text = None
        payload = None

        print(incoming_message)
        for entry in incoming_message['entry']:

            if not 'messaging' in entry:
                break

            print("entry-----------------")
            print(entry)

            for message in entry['messaging']:

                if 'message' in message:
                    print('+++=== GOT MESSAGE ===++')
                    # GET END USER INFO
                    sender_id = message['sender']['id']

                    try:
                        # quick reply button
                        if 'quick_reply' in message['message']:
                            if 'payload' in message['message']['quick_reply']:
                                payload = message['message']['quick_reply']['payload']
                                # get end_user_info
                                end_user_info = get_end_user_info(self.request.path, sender_id)
                                # start auto reply
                                if "__event_" in payload:
                                    start_event_reservation(payload, text, end_user_info)

                                else:
                                    update_message_sequence(payload, text, end_user_info)

                        # text receive
                        elif 'text' in message['message']:
                            text = message['message']['text']
                            # get end_user_info
                            end_user_info = get_end_user_info(self.request.path, sender_id)

                            # Input Text
                            event_controller_from_text(end_user_info, text)

                            # start auto reply
                            if payload is None:
                                payload = ""

                            if "__event_" in payload:
                                start_event_reservation(payload, text, end_user_info)

                            else:
                                update_message_sequence(payload, text, end_user_info)

                    except Exception as e:
                        print("messaging exception")
                        print('%r' % e)
                        print(traceback.format_exc())

                if 'postback' in message:
                    print('=== GOT POSTBACK ===')
                    # GET END USER INFO
                    # end_user_info = get_end_user_info(self.request.path)

                    try:
                        # print the message in terminal
                        pprint("postback =========================================================")
                        pprint(message)
                        payload = message['postback']['payload']
                        sender_id = message['sender']['id']

                        # START BUTTON
                        if payload == 'GET_STARTED_PAYLOAD':
                            # TODO: typing

                            # create or update the user
                            end_user_vendor_info_dict = get_end_user_vendor_info(self.request.path)
                            if end_user_vendor_info_dict:
                                create_or_update_auth_user(sender_id, end_user_vendor_info_dict)

                            # get end_user_info
                            end_user_info = get_end_user_info(self.request.path, sender_id)

                            # start auto reply
                            if "__event_" in payload:
                                start_event_reservation(payload, text, end_user_info)

                            else:
                                update_message_sequence(payload, text, end_user_info)

                        elif payload == "__event_GET_STARTED":
                            end_user_info = get_end_user_info(self.request.path, sender_id)
                            start_event_reservation(payload, text, end_user_info)

                        else:
                            pass

                    except Exception as e:
                        print('%r' % e)

                # ref parameter
                if 'referral' in message:
                    ref_param = message['referral']['ref']
                    pprint("ref_param========")
                    pprint(ref_param)

                end_user_logger(request, end_user_info)

        return HttpResponse("Success", status=200)
