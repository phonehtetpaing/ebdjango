# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

# import views
from future.moves import collections

from apps.core.views.bot_parts.contactchat.end_user_info import *
from apps.core.views.bot_parts.contactchat.access_util import *
from apps.core.views.bot_common.message_sequence import *
from apps.core.views.bot_common.start_event_reservation import *
from apps.core.views.bot_common.payload_converter import *
from apps.core.views.logging.end_user_logging import end_user_logger
from apps.contactchat.webhook import CCWebhookParser
from apps.contactchat.exceptions import InvalidSignatureError
from apps.qa.views.utilities.questionnaire_sequence import process_questionnaire_sequence


class MessageView(generic.View):

    def get(self, request, *args, **kwargs):
        try:
            print("Received GET request", self.request)

            # break up the url to identify the service and vendor
            access_url_path_dict = get_access_url_path_dict(self.request.path)
            access_url_part = access_url_path_dict["vendor_access_url"]

            # retrieve the verify token for the specified vendor to use for authentication
            verify_token = get_verify_token(access_url_part)
            signature = request.META['HTTP_X_CONTACTCHAT_SIGNATURE']
            body = request.body.decode('utf-8')
            parser = CCWebhookParser(verify_token)

            print("debugging body", body)

            return HttpResponse()

        except InvalidSignatureError:
            print('ERROR: signatures did not match')
            return HttpResponseForbidden()
        except Exception as e:
            print('%r' % e)
            return HttpResponseBadRequest()

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            print("Received POST request", self.request)
            # break up the url to identify the service and vendor
            access_url_path_dict = get_access_url_path_dict(self.request.path)
            access_url_part = access_url_path_dict["vendor_access_url"]

            # retrieve the verify token for the specified vendor to use for authentication
            verify_token = get_verify_token(access_url_part)
            signature = request.META['HTTP_X_CONTACTCHAT_SIGNATURE']

            body = request.body.decode('utf-8')
            parser = CCWebhookParser(verify_token)
            incoming_message = parser.parse(body, signature)

            for message in incoming_message:
                user_id = message['sender']['id']

                if 'message' in message:
                    # start questionnaire sequence
                    if message['message'] and message['message'].get('endpoint') and message['message']['endpoint'] == 'qa':
                        print('testing questionnaire')
                        # get end_user_vendor_info and update user
                        end_user_vendor_info_dict = get_end_user_vendor_info(request.path)
                        if end_user_vendor_info_dict:
                            create_or_update_auth_user(user_id, end_user_vendor_info_dict)

                        # get end_user_info # todo replace this with a qa alternative
                        print('testing end_user_info')
                        end_user_info = get_end_user_info(request.path, user_id)

                        process_questionnaire_sequence(message['message'], end_user_info)
                    else:
                        text = message['message']['text']
                        payload = message['message']['payload']



                        # start welcome message sequence
                        if payload == "GET_STARTED_PAYLOAD":

                            # get end_user_vendor_info and update user
                            end_user_vendor_info_dict = get_end_user_vendor_info(request.path)
                            if end_user_vendor_info_dict:
                                create_or_update_auth_user(user_id, end_user_vendor_info_dict)

                            # get end_user_info
                            end_user_info = get_end_user_info(request.path, user_id)

                            update_message_sequence(payload, text, end_user_info)

                        # continue previous sequence
                        else:
                            # get end_user_info
                            end_user_info = get_end_user_info(request.path, user_id)

                            # start event registration
                            if "__event_" in payload:
                                start_event_reservation(payload, text, end_user_info)

                            elif "__session_close" in payload:
                                delete_auth_user(user_id, end_user_vendor_info_dict)

                            elif "test_payload" in payload:
                                # echo message back as test
                                text_send_message(end_user_info, {'text': text})
                            # update existing message sequence
                            else:
                                update_message_sequence(payload, text, end_user_info)

                # todo testing
                end_user_logger(request, end_user_info)

            return HttpResponse()

        except InvalidSignatureError:
            print('ERROR: signatures did not match')
            return HttpResponseForbidden()
        except Exception as e:
            import traceback
            traceback.print_exc()
            print('%r' % e)
            return HttpResponseServerError()
