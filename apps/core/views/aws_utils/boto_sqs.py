import boto3
import json
from django.conf import settings


def push_manual_message(manual_message_overview_id, vendor_user_id, manual_message_history_id):
    # Create SQS client
    sqs = boto3.client(
        'sqs',
        aws_access_key_id=settings.AWS_SQS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SQS_SECRET_ACCESS_KEY,
        region_name='ap-northeast-1'
    )

    queue_url = settings.SQS_QUEUE_URL

    message_dict = {
        "message_type": "MANUAL",
        "manual_message_overview_id": manual_message_overview_id,
        "vendor_user_id": vendor_user_id,
        "manual_message_history_id": manual_message_history_id,
    }

    try:
        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageAttributes={
                'Title': {
                    'DataType': 'String',
                    'StringValue': 'Manual Message'
                },
                'VendorUserID': {
                    'DataType': 'String',
                    'StringValue': str(vendor_user_id)
                },
            },
            MessageBody=(
                json.dumps(message_dict)
            )
        )

        print(response['MessageId'])

    except Exception as e:
        print("SQS Send: Manual Message Error")
        print('%r' % e)


def push_auto_message(auto_message_trigger_id, auto_message_history_id, batch_start_dt):
    # Create SQS client
    sqs = boto3.client(
        'sqs',
        aws_access_key_id=settings.AWS_SQS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SQS_SECRET_ACCESS_KEY,
        region_name='ap-northeast-1'
    )

    queue_url = settings.SQS_QUEUE_URL

    message_dict = {
        "message_type": "AUTO",
        "auto_message_trigger_id": str(auto_message_trigger_id),
        "auto_message_history_id": str(auto_message_history_id),
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
                    'StringValue': 'Auto Message'
                },
                'VendorUserID': {
                    'DataType': 'String',
                    'StringValue': str(auto_message_trigger_id)
                },
            },
            MessageBody=(
                json.dumps(message_dict)
            )
        )

        print(response['MessageId'])

    except Exception as e:
        print("SQS Send: Auto Message Error")
        print('%r' % e)
