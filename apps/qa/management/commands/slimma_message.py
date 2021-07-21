# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand

# import models
from apps.qa.models.ma_trigger_type import MaTriggerType


# import views
from apps.core.views.vendor_common.auto_messsage import *
from apps.qa.views.utilities.boto_sqs import push_slimma_message


# extends BaseCommand
class Command(BaseCommand):
    # python manage.py help count_entry
    help = 'Display the number of users'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        result = send_message()

        if result:
            self.stdout.write(self.style.SUCCESS('OK'))
        else:
            self.stdout.write(self.style.SUCCESS('NG'))


def send_message():
    print("sending slimma message")
    try:
        # Get current datetime and
        batch_buffer_min = 30
        batch_start_dt = datetime.datetime.now()

        # Push message to SQS
        trigger_types = MaTriggerType.objects.all()
        for t_type in trigger_types:
            push_slimma_message(t_type.id, batch_start_dt)

        return True

    except Exception as e:
        print("SLIMMA Message Batch ERROR:" + e)
        return False
