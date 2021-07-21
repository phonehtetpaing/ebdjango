import json
import datetime
import string
import requests
from django.conf import settings

WORKER_URL = settings.ROOT_URL + "smartsec/worker/send/message/"


def push_sim_manual_message(manual_message_overview_id, vendor_user_id, manual_message_history_id):
    # Create json data
    now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sqs_message_id = "MANUAL_message_id" + now_str
    message_body_dict = {
        "HTTP_X_AWS_SQSD_MSGID": sqs_message_id,
        "HTTP_X_AWS_SQSD_FIRST_RECEIVED_AT": now_str,
        "message_type": "MANUAL",
        "manual_message_overview_id": str(manual_message_overview_id),
        "vendor_user_id": str(vendor_user_id),
        "manual_message_history_id": str(manual_message_history_id),
    }

    message_body_json = json.dumps(message_body_dict)
    requests.post(WORKER_URL, headers={"Content-Type": "application/json"}, data=message_body_json)


def push_sim_auto_message(auto_message_trigger_id, auto_message_history_id, batch_start_dt):
    # Create json data
    now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sqs_message_id = "MANUAL_message_id" + now_str
    message_body_dict = {
        "HTTP_X_AWS_SQSD_MSGID": sqs_message_id,
        "HTTP_X_AWS_SQSD_FIRST_RECEIVED_AT": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "message_type": "AUTO",
        "auto_message_trigger_id": str(auto_message_trigger_id),
        "auto_message_history_id": str(auto_message_history_id),
        "batch_start_dt": batch_start_dt.strftime('%Y-%m-%d %H:%M:%S'),
    }

    message_body_json = json.dumps(message_body_dict)
    requests.post(WORKER_URL, headers={"Content-Type": "application/json"}, data=message_body_json)
