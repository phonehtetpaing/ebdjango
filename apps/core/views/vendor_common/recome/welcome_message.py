# -*- coding: utf-8 -*-
import json, requests
from django.conf import settings
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_line import EndUserLINE


def send_welcome_message(end_user_id):

    # Fixed Welcome Message
    end_user = EndUser.objects.filter(id=end_user_id).first()
    end_user_line = EndUserLINE.objects.filter(end_user=end_user).first()
    line_bot_api = LineBotApi(end_user_line.end_user.vendor_branch.vendor.line_access_token)

    first_message = "WELCOME!"

    # Create Registration URL
    registration_check_url = "/recome/registration/line/check/" + str(end_user_line.end_user.id) + "/" + "?openExternalBrowser=1"
    if settings.MODE == "LOCAL":
        registration_url = settings.ROOT_URL_PUBLIC + registration_check_url
    else:
        registration_url = settings.ROOT_URL + registration_check_url

    carousel_template_message = TemplateSendMessage(
        alt_text='Welcome! ',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=settings.LINE_DEFAULT_IMG_URL,
                    title='Click URL',
                    text='user registration',
                    actions=[
                        URITemplateAction(
                            label='Register Now',
                            uri=registration_url
                        )
                    ]
                )
            ]
        )
    )

    try:
        line_bot_api.push_message(
            end_user_line.user_id,
            TextSendMessage(text=first_message)
        )

        line_bot_api.push_message(
            end_user_line.user_id,
            carousel_template_message
        )

    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)


def thankyou_message(end_user_id):

    # Fixed Welcome Message
    end_user = EndUser.objects.filter(id=end_user_id).first()
    end_user_line = EndUserLINE.objects.filter(end_user=end_user).first()
    line_bot_api = LineBotApi(end_user_line.end_user.vendor_branch.vendor.line_access_token)

    first_message = "Thank you!"

    try:
        line_bot_api.push_message(
            end_user_line.user_id,
            TextSendMessage(text=first_message)
        )

    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)


def sorry_message(end_user_id):

    # Fixed Welcome Message
    end_user = EndUser.objects.filter(id=end_user_id).first()
    end_user_line = EndUserLINE.objects.filter(end_user=end_user).first()
    line_bot_api = LineBotApi(end_user_line.end_user.vendor_branch.vendor.line_access_token)

    first_message = "Sorry.. Please try it again."

    try:
        line_bot_api.push_message(
            end_user_line.user_id,
            TextSendMessage(text=first_message)
        )

    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)
