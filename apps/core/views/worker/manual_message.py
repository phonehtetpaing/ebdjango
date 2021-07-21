import json
import datetime
from django.views.decorators.csrf import csrf_exempt

# import views
from apps.core.views.messaging_adapter_web.text_send_message import *
from apps.core.views.messaging_adapter_web.button_select_message import *
from apps.core.views.messaging_adapter_web.image_send_message import *
from apps.core.views.messaging_adapter_web.carousel_send_message import *
from apps.core.views.vendor_common.message_json_converter import *
from apps.core.views.vendor_common.login_user_info import *

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.manual_message_controller import ManualMessageController
from apps.core.models.manual_message_history import ManualMessageHistory
from apps.core.models.tag import Tag
from apps.core.models.manual_message_overview import ManualMessageOverview
from apps.core.models.message_status import MessageStatus
from apps.core.models.worker_sqs_status import WorkerSQSStatus


def send_manual_message(vendor_user_id, manual_message_overview_id, manual_message_history, worker_sqs_status):

    # Get vendor user and manual message object
    vendor_user = VendorUser.objects.filter(id=vendor_user_id).first()
    manual_message_overview = ManualMessageOverview.objects.filter(id=manual_message_overview_id,
                                                                   vendor_branch_id=vendor_user.vendor_branch.id,
                                                                   is_delete=0).first()

    # Get vendor branch id list
    vendor_branch_id_list = [vendor_user.vendor_branch.id]

    # Get tag list to send message
    if manual_message_overview.tags:
        tag_id_list = manual_message_overview.tags.split(",")
        # Tag List > End User List
        tags = Tag.objects.filter(id__in=tag_id_list).all()
    else:
        tag_id_list = []
        # Tag List > End User List
        tags = Tag.objects.filter(is_delete=False).all()

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
        # 3: ERROR
        worker_sqs_status.status = 3
        worker_sqs_status.error_text = str(e)
        worker_sqs_status.save()
        # Change Message Status (ERROR)
        message_status = MessageStatus.objects.filter(name="error", is_delete=False).first()
        manual_message_overview.message_status = message_status
        manual_message_overview.save()
        return "Message Send ERROR"

    # Save History
    try:
        end_user_id_list = []
        for end_user in end_users:
            end_user_id_list.append(end_user.id)
        send_user_id_csv = ",".join(map(str, end_user_id_list))
        selected_tag_csv = ",".join(map(str, tag_id_list))
        send_user_count = end_users.count()
        manual_message_history.send_user_count = send_user_count
        manual_message_history.send_user_id_csv = send_user_id_csv
        manual_message_history.selected_tag_csv = selected_tag_csv
        manual_message_history.save()

        worker_sqs_status.status = 2
        worker_sqs_status.save()

        # Change Message Status (Sent)
        message_status = MessageStatus.objects.filter(name="sent", is_delete=False).first()
        manual_message_overview.message_status = message_status
        manual_message_overview.save()

        return "Success"

    except Exception as e:
        print("manual message history exception")
        print('%r' % e)
        # 4: save history error
        worker_sqs_status.status = 4
        worker_sqs_status.error_text = str(e)
        worker_sqs_status.save()
        # return 200 : check the cause of error manually
        return "History Save ERROR"
