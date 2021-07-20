# -*- coding: utf-8 -*-
# import messaging
from apps.core.views.messaging_native_web.fbms.text_send_message import *
from apps.core.views.messaging_native_web.line.text_send_message import *

# import models
from apps.core.models.end_user_facebook import EndUserFacebook
from apps.core.models.end_user_line import EndUserLINE


def text_send_message(end_user, param):
    end_user_facebook = EndUserFacebook.objects.filter(end_user=end_user).first()
    end_user_line = EndUserLINE.objects.filter(end_user=end_user).first()

    if end_user_facebook:
        fbms_text_send_message(end_user_facebook, param)

    if end_user_line:
        line_text_send_message(end_user_line, param)

    return True
