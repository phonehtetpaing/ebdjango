# -*- coding: utf-8 -*-
from django.conf import settings
import mimetypes
import traceback
import time
import json

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *


def line_image_send_message(end_user_info, param):
    line_bot_api = LineBotApi(end_user_info["line_access_token"])

    url = param["url"]
    mimetype, encoding = mimetypes.guess_type(url)

    # if ".JPEG" in url or ".jpeg" in url or ".JPG" in url or ".jpg" in url:
    # LINE doesn't directly support animated image types and will parse them as static instead
    if mimetype and mimetype.startswith('image'):
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
    else:
        image_message = TemplateSendMessage(
            alt_text='File View',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url=url,
                        action=
                            URITemplateAction(
                                label='View on Web',
                                uri=param["url"],
                            )

                    )
                ]
            )
        )

    try:
        line_bot_api.push_message(
            end_user_info["user_id"],
            image_message
        )

    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)
        print(traceback.format_exc())