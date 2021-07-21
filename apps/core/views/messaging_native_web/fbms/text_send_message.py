# -*- coding: utf-8 -*-
import json, requests
from django.conf import settings


def fbms_text_send_message(end_user_facebook, param):
    try:
        fbms_access_token = end_user_facebook.end_user.vendor_branch.vendor.fbms_access_token
        post_message_url = settings.FB_MESSAGE_URL + fbms_access_token

        msg_data = {
            "recipient": {"id": end_user_facebook.sender_id},
            "message": {"text": param["text"]}
        }

        response_msg = json.dumps(msg_data)
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
        print("[fbms_text_send_message] ===================== ")
        print(status.json())
        return True

    except Exception as e:
        print("fbms_text_send_message exception")
        print('%r' % e)
        return False
