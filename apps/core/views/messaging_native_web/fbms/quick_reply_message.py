# -*- coding: utf-8 -*-
import json, requests
from django.conf import settings


def fbms_quick_reply_message(end_user_facebook, param):
    try:
        fbms_access_token = end_user_facebook.end_user.vendor_branch.vendor.fbms_access_token
        post_message_url = settings.FB_MESSAGE_URL + fbms_access_token

        quick_reply_list = []
        quick_replies = param["quick_replies"]
        for quick_reply in quick_replies:
            quick_reply_dict = {
                "content_type": quick_reply["content_type"],
                "title": quick_reply["title"],
                "payload": quick_reply["payload"],
            }
            quick_reply_list.append(quick_reply_dict)

        msg_data = {
            "recipient": {"id": end_user_facebook.sender_id},
            "message": {
                "text": param["text"],
                "quick_replies": quick_reply_list
            }
        }

        response_msg = json.dumps(msg_data)
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
        print("[debug] ===================== ")
        print(status.json())
        return True

    except Exception as e:
        print("messaging exception")
        print('%r' % e)
        return False
