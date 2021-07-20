# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
import datetime
import time
import random

# import models
from apps.core.models.tmp_entry import TmpEntry
from apps.core.models.tmp_registration_entry import TmpRegistrationEntry
from apps.core.models.end_user_contactchat import EndUserContactChat
from apps.core.models.todo import Todo
from apps.core.models.end_user import EndUser


# extends BaseCommand
class Command(BaseCommand):
    # python manage.py help count_entry
    help = 'Display the number of users'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        result = clear_data()

        if result:
            self.stdout.write(self.style.SUCCESS('OK'))
        else:
            self.stdout.write(self.style.SUCCESS('NG'))


def clear_data():
    try:

        # Get current datetime and
        batch_buffer_min = 5
        batch_start_dt = datetime.datetime.now()
        # batch_start_dt_gt = batch_start_dt + datetime.timedelta(minutes=batch_buffer_min)
        batch_start_dt_lt = batch_start_dt - datetime.timedelta(minutes=batch_buffer_min)
        TmpEntry.objects.filter(access_dt__lt=batch_start_dt_lt).delete()
        TmpRegistrationEntry.objects.filter(access_dt__lt=batch_start_dt_lt).delete()

        # Delete EndUserContactChat
        delete_weeks = 4
        delete_dt_lt = batch_start_dt - datetime.timedelta(weeks=delete_weeks)
        end_user_contactchats = EndUserContactChat.objects.filter(regist_dt__lte=delete_dt_lt)

        # EndUser_ID in EndUserContactChat_model
        delete_end_user_id_list = []
        for end_user_contactchat in end_user_contactchats:
            delete_end_user_id_list.append(end_user_contactchat.end_user_id)

        # Get EndUser_ID in TODO_model
        todos = Todo.objects.filter(is_delete=False).all()
        for todo in todos:
            if todo.end_user.id in delete_end_user_id_list:
                delete_end_user_id_list.remove(todo.end_user.id)

        # Delete EndUser
        print("debug: delete_end_user_id_list")
        print(delete_end_user_id_list)
        EndUser.objects.filter(id__in=delete_end_user_id_list).delete()

        return True

    except Exception as e:
        print("Data Cleaning Batch ERROR:" + e)
        return False
