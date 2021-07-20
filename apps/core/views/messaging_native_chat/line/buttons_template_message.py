# -*- coding: utf-8 -*-
from django.conf import settings
import time
import json

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *


def line_buttons_template_message(end_user_info, param):
    line_bot_api = LineBotApi(end_user_info["line_access_token"])

    action_list = []
    actions = param["quick_replies"]
    for action in actions:
        action_obj = PostbackTemplateAction(
                        label=action["title"],
                        text=action["title"],
                        data=action["payload"]
                    )
        action_list.append(action_obj)

    if len(action_list) >= 4:
        action_list = action_list[0:4]

    buttons_template_message = TemplateSendMessage(
        alt_text='SELECT Button',
        template=ButtonsTemplate(
            text=param["text"],
            actions=action_list
        )
    )

    try:
        line_bot_api.push_message(
            end_user_info["user_id"],
            buttons_template_message
        )
    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)