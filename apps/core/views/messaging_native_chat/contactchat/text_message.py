# -*- coding: utf-8 -*-
import json, requests
from django.conf import settings
from apps.contactchat import ContactChatApi


def contactchat_text_message(end_user_info, param):
    try:
        verify_token = end_user_info["end_user_obj"].vendor_branch.vendor.contactchat_verify_token
        contactchat_api = ContactChatApi(end_user_info["contactchat_access_token"], verify_token, settings.CONTACTCHAT_BASE_URL)
        status = contactchat_api.push_message(
            end_user_info["user_id"],
            {"type": "text", "text": param["text"]}
        )
        print(status)
        return True
    except Exception as e:
        print("api exception")
        print(e)
        return True
