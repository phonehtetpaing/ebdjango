# -*- coding: utf-8 -*-
import boto3
import json
from django.conf import settings


def push_slimma_message(trigger_type_id, batch_start_dt):
    # Create SQS client
    sqs = boto3.client(
        'sqs',
        aws_access_key_id=settings.AWS_SQS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SQS_SECRET_ACCESS_KEY,
        region_name='ap-northeast-1'
    )

    queue_url = settings.SQS_QUEUE_URL

    message_dict = {
        "message_type": "SLIMMA",
        "trigger_type_id": str(trigger_type_id),
        "batch_start_dt": batch_start_dt.strftime('%Y-%m-%d %H:%M:%S'),
    }

    try:
        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageAttributes={
                'Title': {
                    'DataType': 'String',
                    'StringValue': 'SlimMA Message'
                },
            },
            MessageBody=(
                json.dumps(message_dict)
            )
        )

        print(response['MessageId'])

    except Exception as e:
        print("SQS Send: SLIMMA Message Error")
        print('%r' % e)
