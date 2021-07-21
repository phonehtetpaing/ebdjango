# -*- coding: utf-8 -*-
import json, requests
from django.conf import settings
from apps.contactchat import ContactChatApi


def contactchat_quick_reply_message(end_user_info, param):
    try:
        verify_token = end_user_info["end_user_obj"].vendor_branch.vendor.contactchat_verify_token
        contactchat_api = ContactChatApi(end_user_info["contactchat_access_token"], verify_token, settings.CONTACTCHAT_BASE_URL)

        quick_reply_list = []
        quick_replies = param["quick_replies"]
        for quick_reply in quick_replies:
            quick_reply_dict = {
                "title": quick_reply["title"],
                "payload": quick_reply["payload"],
            }
            quick_reply_list.append(quick_reply_dict)

        status = contactchat_api.push_message(
            end_user_info["user_id"],
            {"type": "quick_reply", "text": param["text"], "quick_replies": quick_reply_list}
        )
        print(status)
        return True
    except Exception as e:
        print("api exception")
        print(e)
        return True
