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
from apps.core.models.manual_message_controller import ManualMessageController
from apps.core.models.manual_message_history import ManualMessageHistory
from apps.core.models.tag import Tag


def send_message_to_tagged_user(request, tag_id_list, manual_message_overview, vendor_branch_id_list, send_test_flg):
    """  Send Manual Messages to Tagged Users  """
    args_list = [request, tag_id_list, manual_message_overview, vendor_branch_id_list, send_test_flg]

    t = threading.Thread(target=__send_message_to_tagged_user, args=args_list)
    t.setDaemon(True)
    t.start()


def __send_message_to_tagged_user(*arguments):
    request = arguments[0]
    tag_id_list = arguments[1]
    manual_message_overview = arguments[2]
    vendor_branch_id_list = arguments[3]
    send_test_flg = arguments[4]

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
        # Tag List > End User List
        tags = Tag.objects.filter(id__in=tag_id_list).all()
        tag_code_list = []
        for tag in tags:
            tag_code_list.append(tag.cd)

        end_users = EndUser.objects.filter(tag__name__in=tag_code_list, vendor_branch__in=vendor_branch_id_list, is_delete=0).distinct()

    # Send Messages by user
    manual_message_controllers = ManualMessageController.objects.filter(manual_message_overview=manual_message_overview, is_delete=0).order_by("run_order_num")

    try:
        for end_user in end_users:

            for manual_message_controller in manual_message_controllers:

                # convert json format
                param_dict = vendor_to_mesasge(manual_message_controller.messaging_api_param_json)

                if manual_message_controller.messaging_api_type.cd == "text":
                    text_send_message(end_user, param_dict)

                elif manual_message_controller.messaging_api_type.cd == "file":
                    file_send_message(end_user, param_dict)

                elif manual_message_controller.messaging_api_type.cd == "image":
                    file_send_message(end_user, param_dict)

                elif manual_message_controller.messaging_api_type.cd == "carousel":
                    carousel_send_message(end_user, param_dict)

                elif manual_message_controller.messaging_api_type.cd == "button_select":
                    button_select_message(end_user, param_dict)

    except Exception as e:
        print("messaging exception")
        print('%r' % e)

    # TODO: save History
    try:
        vendor_branch = None
        if request:
            user_obj = get_login_user_objects(request)
            vendor_branch = user_obj["vendor_branch"]

        end_user_id_list = []
        for end_user in end_users:
            end_user_id_list.append(end_user.id)
        send_user_id_csv = ",".join(map(str, end_user_id_list))
        selected_tag_csv = ",".join(map(str, tag_id_list))
        send_user_count = end_users.count()
        send_dt = datetime.datetime.now()

        manual_message_history = ManualMessageHistory()
        manual_message_history.vendor_branch = vendor_branch
        manual_message_history.manual_message_overview = manual_message_overview
        manual_message_history.send_dt = send_dt
        manual_message_history.send_user_count = send_user_count
        manual_message_history.send_user_id_csv = send_user_id_csv
        manual_message_history.selected_tag_csv = selected_tag_csv
        manual_message_history.save()

    except Exception as e:
        print("manual message exception")
        print('%r' % e)
