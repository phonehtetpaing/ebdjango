# -*- coding: utf-8 -*-
import json, requests
from django.conf import settings


def fbms_text_send_message(end_user_info, param):
    post_message_url = settings.FB_MESSAGE_URL + end_user_info["fbms_access_token"]

    msg_data = {
        "recipient": {"id": end_user_info["sender_id"]},
        "message": {"text": param["text"]}
    }

    response_msg = json.dumps(msg_data)
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    print(status.json())
    return True
