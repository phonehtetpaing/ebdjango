# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
import datetime
import time
import random

# import models
from apps.core.models.manual_message_overview import ManualMessageOverview
from apps.core.models.manual_message_history import ManualMessageHistory
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
    print("sending manual message")
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

        """ send message to tagged end_user """
        message_status = MessageStatus.objects.filter(name="scheduled", is_delete=False).first()
        manual_message_overviews = ManualMessageOverview.objects.filter(message_status=message_status, push_dt__range=(target_dt_range_lt_str, target_dt_range_gt_str), is_delete=False).all()

        for manual_message_overview in manual_message_overviews:
            # Create a new History
            vendor_branch = manual_message_overview.vendor_branch
            send_dt = datetime.datetime.now()
            manual_message_history = ManualMessageHistory()
            manual_message_history.vendor_branch = vendor_branch
            manual_message_history.manual_message_overview = manual_message_overview
            manual_message_history.send_dt = send_dt
            manual_message_history.save()

            # Change Status
            message_status = MessageStatus.objects.filter(name="sending", is_delete=False).first()
            manual_message_overview.message_status = message_status
            manual_message_overview.save()

            # Push message to SQS
            if settings.MODE == "LOCAL":
                print("local sqs=====")
                print(manual_message_overview.id)
                print(manual_message_overview.vendor_branch.id)
                print(manual_message_history.id)
                push_sim_manual_message(manual_message_overview.id, manual_message_overview.vendor_branch.id, manual_message_history.id)

            else:
                push_manual_message(manual_message_overview.id, manual_message_overview.vendor_branch.id, manual_message_history.id)

        return True

    except Exception as e:
        print("Auto Message Batch ERROR:" + e)
        return False
