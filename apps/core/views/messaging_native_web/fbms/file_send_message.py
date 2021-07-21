# -*- coding: utf-8 -*-
import json, requests
from django.conf import settings

# import views
from apps.core.views.messaging_native_web.fbms.domain_whitelist import *


def fbms_file_send_message(end_user_facebook, param):
    try:
        fbms_access_token = end_user_facebook.end_user.vendor_branch.vendor.fbms_access_token
        post_message_url = settings.FB_MESSAGE_URL + fbms_access_token

        msg_data = {
            "recipient": {"id": end_user_facebook.sender_id},
            "message": {
                "attachment": {
                  "type": param["type"],
                  "payload": {
                    "url": param["url"],
                    "is_reusable": True
                  }
                }
            }
        }

        add_whitelist(end_user_facebook, param["url"])

        response_msg = json.dumps(msg_data)
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
        print("[fbms_file_send_message] ===================== ")
        print(status.json())
        return True

    except Exception as e:
        print("fbms_file_send_message exception")
        print('%r' % e)
        return False
