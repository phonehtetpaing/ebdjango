# -*- coding: utf-8 -*-
from django.conf import settings
import time
import json

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *


def line_image_send_message(end_user_line, param):
    line_bot_api = LineBotApi(end_user_line.end_user.vendor_branch.vendor.line_access_token)

    url = param["url"]
    if ".JPEG" in url or ".jpeg" in url or ".JPG" in url or ".jpg" in url:
        image_message = ImageSendMessage(
            original_content_url=param["url"],
            preview_image_url=param["url"]
        )

    else:
        image_message = TemplateSendMessage(
            alt_text='File View',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=settings.LINE_DEFAULT_IMG_URL,
                        title='File',
                        text='-',
                        actions=[
                            URITemplateAction(
                                label='View on Web',
                                uri=param["url"],
                            )
                        ]
                    )
                ]
            )
        )

    try:
        line_bot_api.push_message(
            end_user_line.user_id,
            image_message
        )

    except LineBotApiError as e:
        print('DEBUG LINE BOT API IMAGE MESSAGE ERROR')
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)