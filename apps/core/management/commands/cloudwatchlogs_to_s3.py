# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
import time
import random
from django.conf import settings

import datetime
import boto3
import json, requests


# extends BaseCommand
class Command(BaseCommand):
    # python manage.py help count_entry
    help = 'Display the number of users'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):

        try:

            lambda_name = 'test-error'
            # log_group_name = '/aws/rds/instance/development-rds/' + lambda_name
            log_group_name = "/aws/rds/instance/production-new-rds/error"
            s3_bucket_name = 'cloudwatchlogs.test.smartby.ai'
            s3_prefix = lambda_name + '/%s' % (datetime.date.today() - datetime.timedelta(days=1))
            api_logs_url = "http://0.0.0.0:8888/api/stats/logs/insert/"

            res = requests.get(api_logs_url)
            result = res.json()
            from_ts = result["event_start_dt"]
            to_ts = result["event_end_dt"]
            print("debug: result")
            print(result)

            client = boto3.client(
                'logs',
                aws_access_key_id=settings.AWS_CWLOGS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_CWLOGS_SECRET_ACCESS_KEY,
                region_name='ap-northeast-1'
            )

            # client = boto3.client('logs')
            response = client.create_export_task(
                logGroupName=log_group_name,
                fromTime=from_ts * 1000,
                to=to_ts * 1000,
                destination=s3_bucket_name,
                destinationPrefix=s3_prefix
            )

            if response:
                # self.stdout.write(self.style.SUCCESS('count = "%s"' % articles_count))
                self.stdout.write(self.style.SUCCESS('OK'))
            else:
                self.stdout.write(self.style.SUCCESS('NG'))

        except Exception as e:
            print('%r' % e)
