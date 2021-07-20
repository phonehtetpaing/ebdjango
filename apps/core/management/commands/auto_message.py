# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
import datetime
import time
import random

# import models
from apps.core.models.auto_message_condition import AutoMessageCondition
from apps.core.models.auto_message_trigger import AutoMessageTrigger
from apps.core.models.auto_message_history import AutoMessageHistory
from apps.core.models.end_user_auto_message import EndUserAutoMessage
from apps.core.models.message_status import MessageStatus


# import views
from apps.core.views.vendor_common.auto_messsage import *
from apps.core.views.aws_utils.boto_sqs import *
from apps.core.views.aws_utils.simulator_sqs import *


# extends BaseCommand
class Command(BaseCommand):
    # python manage.py help count_entry
    help = 'Display the number of users'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        result = send_message()

        if result:
            # self.stdout.write(self.style.SUCCESS('count = "%s"' % articles_count))
            self.stdout.write(self.style.SUCCESS('OK'))
        else:
            self.stdout.write(self.style.SUCCESS('NG'))


def send_message():
    print("sending message")
    try:
        # Get current datetime and
        batch_buffer_min = 5
        batch_start_dt = datetime.datetime.now()
        batch_start_dt_gt = batch_start_dt + datetime.timedelta(minutes=batch_buffer_min)
        batch_start_dt_lt = batch_start_dt - datetime.timedelta(minutes=batch_buffer_min)
        batch_start_time_gt = batch_start_dt_gt.strftime('%H:%M:%S')
        batch_start_time_lt = batch_start_dt_lt.strftime('%H:%M:%S')

        # Get range of Today
        batch_start_yyyymmdd_str = batch_start_dt.strftime('%Y-%m-%d')
        target_dt_range_lt_str = batch_start_yyyymmdd_str + " 00:00:00"
        target_dt_range_gt = batch_start_dt + + datetime.timedelta(days=1)
        target_dt_range_gt_str = target_dt_range_gt.strftime('%Y-%m-%d') + " 00:00:00"

        # Get Target Auto Message Trigger Objects
        auto_message_triggers = AutoMessageTrigger.objects.filter(trigger_time__range=(batch_start_time_lt, batch_start_time_gt)).all()
        # auto_message_triggers = AutoMessageTrigger.objects.all()
        print("auto_message_triggers")

        # Push Message to SQS
        for auto_message_trigger in auto_message_triggers:
            # check if in-progress
            vendor_branch = auto_message_trigger.auto_message_condition.vendor_branch
            auto_message_condition = auto_message_trigger.auto_message_condition
            # Interval for DB Access
            sleep_sec = random.random()
            time.sleep(sleep_sec)
            print("sleep_sec")
            print(sleep_sec)
            auto_message_history = AutoMessageHistory.objects.filter(vendor_branch=vendor_branch, auto_message_condition=auto_message_condition,
                                                                     auto_message_trigger=auto_message_trigger, send_dt__range = (target_dt_range_lt_str, target_dt_range_gt_str)).order_by("-regist_dt").first()

            if not auto_message_history:
                # Create New History
                # get "In Queue" status (pending)
                message_status = MessageStatus.objects.filter(name="pending", is_delete=False).first()
                auto_message_history = AutoMessageHistory()
                auto_message_history.vendor_branch = vendor_branch
                auto_message_history.auto_message_condition = auto_message_condition
                auto_message_history.auto_message_trigger = auto_message_trigger
                auto_message_history.send_dt = batch_start_dt
                auto_message_history.message_status = message_status
                auto_message_history.save()
                print("push_auto_message ==== ")
                print(auto_message_trigger)

                # Push message to SQS
                if settings.MODE == "LOCAL":
                    push_sim_auto_message(auto_message_trigger.id, auto_message_history.id, batch_start_dt)

                else:
                    push_auto_message(auto_message_trigger.id, auto_message_history.id, batch_start_dt)

        return True

    except Exception as e:
        print("Auto Message Batch ERROR:" + e)
        return False
