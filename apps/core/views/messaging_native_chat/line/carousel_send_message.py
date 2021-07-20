# -*- coding: utf-8 -*-
from django.conf import settings
import time
import json

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *


def line_carousel_template_message(end_user_line, param):
    end_user = end_user_line["end_user_obj"]
    line_bot_api = LineBotApi(end_user.vendor_branch.vendor.line_access_token)

    columns_list = []
    colums = param["elements"]
    for colum in colums:
        action_list = []

        for button in colum["buttons"]:
            uri_template_action = URITemplateAction(
                label=button["title"],
                uri=button["data"]
            )
            action_list.append(uri_template_action)

        carousel_column = CarouselColumn(
            thumbnail_image_url=colum["image_url"],
            title=colum["title"],
            text=colum["subtitle"],
            actions=action_list
        )
        columns_list.append(carousel_column)

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel',
        template=CarouselTemplate(
            columns=columns_list
        )
    )

    try:
        line_bot_api.push_message(
            end_user.id,
            carousel_template_message
        )
    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)
