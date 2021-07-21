# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
import time
import random
from django.conf import settings

import datetime
import boto3
import json, requests
from pytz import timezone

# [test]
# log_group_name = 'test-0001'
# log_stream_name_prefix = 'test-st-0001'

# [local]
# log_group_name = '/messaging_platform/local'
# log_stream_name_prefix = 'app_log'


# extends BaseCommand
class Command(BaseCommand):
    # python manage.py help count_entry
    help = 'Display the number of users'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):

        log_group_name = '/messaging_platform/local'
        log_stream_name_prefix = 'app_log'

        try:
            log_path = settings.BASE_DIR + "/logs/local/app.log"
            f = open(log_path)
            line = f.readline()
            while line:
                line = f.readline()
                print(line)
                message = line

                logs_client = boto3.client(
                    'logs',
                    aws_access_key_id=settings.AWS_CWLOGS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_CWLOGS_SECRET_ACCESS_KEY,
                    region_name='ap-northeast-1'
                )

                res = logs_client.describe_log_streams(
                    logGroupName=log_group_name,
                    logStreamNamePrefix=log_stream_name_prefix,
                )

                if "uploadSequenceToken" in res['logStreams'][0]:
                    print("token found")
                    ts = int(datetime.datetime.now(timezone('UTC')).timestamp()) * 1000
                    print(ts)
                    seq_token = res['logStreams'][0]['uploadSequenceToken']
                    res = logs_client.put_log_events(
                        logGroupName=log_group_name,
                        logStreamName=log_stream_name_prefix,
                        logEvents=[
                            {
                                'timestamp': ts,
                                # 'timestamp': int(time.time()) * 1000,
                                'message': message
                            },
                        ],
                        sequenceToken=seq_token
                    )

                else:
                    print("token NOT found")
                    ts = int(datetime.datetime.now(timezone('UTC')).timestamp()) * 1000
                    print(ts)
                    res = logs_client.put_log_events(
                        logGroupName=log_group_name,
                        logStreamName=log_stream_name_prefix,
                        logEvents=[
                            {
                                'timestamp': ts,
                                'message': message
                            }
                        ]
                    )

            f.close()

            if res:
                # self.stdout.write(self.style.SUCCESS('count = "%s"' % articles_count))
                self.stdout.write(self.style.SUCCESS('OK'))
            else:
                self.stdout.write(self.style.SUCCESS('NG'))

        except Exception as e:
            print("exception")
            print('%r' % e)
