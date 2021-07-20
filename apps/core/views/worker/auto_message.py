# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
import datetime

# import models
from apps.core.models.auto_message_condition import AutoMessageCondition
from apps.core.models.auto_message_trigger import AutoMessageTrigger
from apps.core.models.auto_message_history import AutoMessageHistory
from apps.core.models.end_user_auto_message import EndUserAutoMessage
from apps.core.models.message_status import MessageStatus
from apps.core.models.end_user import EndUser


# import views
from apps.core.views.vendor_common.auto_messsage import *


def send_auto_message(auto_message_trigger_id, auto_message_history_id, batch_start_dt, worker_sqs_status):
    print("sending auto message")
    auto_message_trigger = AutoMessageTrigger.objects.filter(id=auto_message_trigger_id).first()
    auto_message_type = auto_message_trigger.auto_message_condition.auto_message_type
    auto_message_history = AutoMessageHistory.objects.filter(id=auto_message_history_id).first()

    # check datetime for target datetime
    batch_buffer_min = 4
    batch_start_dt_gt = batch_start_dt + datetime.timedelta(minutes=batch_buffer_min)
    batch_start_dt_lt = batch_start_dt - datetime.timedelta(minutes=batch_buffer_min)

    # End user Auto Message
    # # end_user in vendor branch
    vendor_branch = auto_message_trigger.auto_message_condition.vendor_branch
    end_users_vb = EndUser.objects.filter(vendor_branch=vendor_branch, is_delete=False)
    end_user_auto_messages = EndUserAutoMessage.objects.filter(end_user__in=end_users_vb, auto_message_type=auto_message_type, is_delete=False).all()

    try:
        # Send Auto Message
        send_user_id_list = []

        for end_user_auto_message in end_user_auto_messages:
            message_target_yyyymmdd_str = end_user_auto_message.message_target_dt.strftime('%Y-%m-%d')
            auto_message_trigger_hhmmss_str = auto_message_trigger.trigger_time.strftime('%H:%M:%S')
            message_target_dt_str = message_target_yyyymmdd_str + " " + auto_message_trigger_hhmmss_str
            message_target_dt = datetime.datetime.strptime(message_target_dt_str, '%Y-%m-%d %H:%M:%S')

            if auto_message_trigger.is_trigger_after:
                # user_datetime + trigger_days
                tmp_dt = message_target_dt + datetime.timedelta(
                    days=auto_message_trigger.trigger_days_num)
            else:
                tmp_dt = message_target_dt - datetime.timedelta(
                    days=auto_message_trigger.trigger_days_num)

            print('send_auto_message tmp_dt = ', tmp_dt)
            if (batch_start_dt_lt <= tmp_dt) and (tmp_dt <= batch_start_dt_gt):
                send_user_id_list.append(end_user_auto_message.end_user.id)
                send_unit_message(None, auto_message_trigger, [end_user_auto_message.end_user.id], False)

        # Update History
        # worker
        worker_sqs_status.status = 4
        worker_sqs_status.save()
        # history
        send_user_count = len(send_user_id_list)
        send_user_id_csv = ",".join(map(str, send_user_id_list))
        message_status = MessageStatus.objects.filter(name="sent", is_delete=False).first()

        print("send_user_count")
        print(send_user_count)

        if send_user_count == 0:
            AutoMessageHistory.objects.filter(id=auto_message_history.id).delete()

        else:
            auto_message_history.send_user_count = send_user_count
            auto_message_history.send_user_id_csv = send_user_id_csv
            auto_message_history.message_status = message_status
            auto_message_history.save()

        return "Success"

    except Exception as e:
        print("auto messaging exception")
        print('%s (%s)' % (e.message, type(e)))
        # 3: ERROR
        worker_sqs_status.status = 3
        worker_sqs_status.error_text = str(e)
        worker_sqs_status.save()
        # Change Message Status (ERROR)
        message_status = MessageStatus.objects.filter(name="error", is_delete=False).first()
        auto_message_history.message_status = message_status
        auto_message_history.save()
        return "Message Send ERROR"
