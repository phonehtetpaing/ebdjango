# -*- coding: utf-8 -*-
import json, requests
from django.conf import settings

# import models
from apps.core.models.end_user_facebook import EndUserFacebook

# import views
from apps.core.views.messaging_native_web.fbms.domain_whitelist import *


def fbms_carousel_send_message(end_user_info, param):
    print('test')
    end_user = end_user_info["end_user_obj"]
    end_user_facebook = EndUserFacebook.objects.filter(end_user=end_user).first()
    post_message_url = settings.FB_MESSAGE_URL + end_user_info["fbms_access_token"]

    element_list = []
    elements = param["elements"]
    for element in elements:
        element_dict = {
            "title": element["title"],
            "image_url": element["image_url"],
            "subtitle": element["subtitle"],
            "default_action": {
                "type": "web_url",
                "url": element["url"],
                "messenger_extensions": True,
                "webview_height_ratio": "tall",
            },
            "buttons": None
        }

        button_list = []
        for button in element["buttons"]:

            if button["type"] == "url":
                type = "web_url"

            button_dict = {
                "type": type,
                "url": button["data"],
                "title": button["title"]
            }

            button_list.append(button_dict)

        element_dict["buttons"] = button_list
        element_list.append(element_dict)

        # Add Whitelist
        add_whitelist(end_user_facebook, element["url"])

    msg_data = {
        "recipient": {"id": end_user_info["sender_id"]},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": element_list
                }
            }
        }
    }

    response_msg = json.dumps(msg_data)
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    print("[debug] ===================== ")
    print(msg_data)
    print(status.json())
    return True
