# -*- coding: utf-8 -*-
import json, requests
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *


def line_text_send_message(end_user_line, param):
    line_bot_api = LineBotApi(end_user_line.end_user.vendor_branch.vendor.line_access_token)

    try:
        line_bot_api.push_message(
            end_user_line.user_id,
            TextSendMessage(text=param["text"])
        )

    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)
