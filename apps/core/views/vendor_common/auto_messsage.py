from django.shortcuts import render

import json
import datetime
import threading

# import views
from apps.core.views.messaging_adapter_web.text_send_message import *
from apps.core.views.messaging_adapter_web.button_select_message import *
from apps.core.views.messaging_adapter_web.image_send_message import *
from apps.core.views.messaging_adapter_web.carousel_send_message import *
from apps.core.views.vendor_common.message_json_converter import *
from apps.core.views.vendor_common.login_user_info import *

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_facebook import EndUserFacebook
from apps.core.models.end_user_line import EndUserLINE
from apps.core.models.auto_message_controller import AutoMessageController
from apps.core.models.auto_message_history import AutoMessageHistory
from apps.core.models.tag import Tag


def send_unit_message(request, auto_message_trigger, target_user_id_list, send_test_flg):
    """  Send Auto Message related with auto_message_trigger """
    try:

        args_list = [request, auto_message_trigger, target_user_id_list, send_test_flg]

        # t = threading.Thread(target=__send_unit_message, args=args_list)
        # t.setDaemon(True)
        # t.start()

        arguments = args_list

    # def __send_unit_message(*arguments):
        request = arguments[0]
        auto_message_trigger = arguments[1]
        target_user_id_list = arguments[2]
        send_test_flg = arguments[3]

        # TEST or NOT
        if send_test_flg:
            user_obj = get_login_user_objects(request)
            vendor_user = user_obj["vendor_user"]
            facebook_sender_id = vendor_user.facebook_sender_id
            line_user_id = vendor_user.line_user_id

            end_user_list = []
            end_user_facebooks = EndUserFacebook.objects.filter(sender_id=facebook_sender_id).all()
            end_user_lines = EndUserLINE.objects.filter(user_id=line_user_id).all()

            for end_user_facebook in end_user_facebooks:
                end_user_list.append(end_user_facebook.end_user_id)

            for end_user_line in end_user_lines:
                end_user_list.append(end_user_line.end_user_id)

            end_users = EndUser.objects.filter(id__in=end_user_list)

        else:
            # Get Receiver EndUsers
            end_users = EndUser.objects.filter(id__in=target_user_id_list, is_delete=False).all()

        # Send Messages by user
        auto_message_controllers = AutoMessageController.objects.filter(auto_message_trigger=auto_message_trigger, is_delete=0).order_by("run_order_num")

    except Exception as e:
        print("send_unit_message exception")
        print('%r' % e)
        return False

    try:
        print("end_users")
        # print(end_users)
        for end_user in end_users:
            try:
                for auto_message_controller in auto_message_controllers:

                    # convert json format
                    param_dict = vendor_to_mesasge(auto_message_controller.messaging_api_param_json)

                    if auto_message_controller.messaging_api_type.cd == "text":
                        text_send_message(end_user, param_dict)

                    elif auto_message_controller.messaging_api_type.cd == "file":
                        file_send_message(end_user, param_dict)

                    elif auto_message_controller.messaging_api_type.cd == "image":
                        file_send_message(end_user, param_dict)

                    elif auto_message_controller.messaging_api_type.cd == "carousel":
                        carousel_send_message(end_user, param_dict)

                    elif auto_message_controller.messaging_api_type.cd == "button_select":
                        button_select_message(end_user, param_dict)

            except Exception as e:
                print("end_users messaging exception")
                print('%r' % e)

    except Exception as e:
        print("messaging exception")
        print('%r' % e)

    # # Save History
    # try:
    #     # batch
    #     if not send_test_flg:
    #
    #         vendor_branch = auto_message_trigger.auto_message_condition.vendor_branch
    #
    #         target_user_id_list = []
    #         for end_user in end_users:
    #             target_user_id_list.append(end_user.id)
    #
    #         send_user_id_csv = ",".join(map(str, target_user_id_list))
    #         send_user_count = end_users.count()
    #         send_dt = datetime.datetime.now()
    #
    #         auto_message_history = AutoMessageHistory()
    #         auto_message_history.vendor_branch = vendor_branch
    #         auto_message_history.auto_message_condition = auto_message_trigger.auto_message_condition
    #         auto_message_history.auto_message_trigger = auto_message_trigger
    #         auto_message_history.send_dt = send_dt
    #         auto_message_history.send_user_count = send_user_count
    #         auto_message_history.send_user_id_csv = send_user_id_csv
    #         auto_message_history.selected_tag_csv = None
    #         auto_message_history.save()
    #
    # except Exception as e:
    #     print("auto message exception")
    #     print('%r' % e)
    #     return False

    return True
