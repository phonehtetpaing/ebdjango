# -*- coding: utf-8 -*-
# import messaging
from apps.core.views.messaging_native_web.fbms.quick_reply_message import *
from apps.core.views.messaging_native_web.line.buttons_template_message import *

# import models
from apps.core.models.end_user_facebook import EndUserFacebook
from apps.core.models.end_user_line import EndUserLINE


def button_select_message(end_user, param):
    end_user_facebook = EndUserFacebook.objects.filter(end_user=end_user).first()
    end_user_line = EndUserLINE.objects.filter(end_user=end_user).first()

    if end_user_facebook:
        fbms_quick_reply_message(end_user_facebook, param)

    else:
        line_buttons_template_message(end_user_line, param)

    return True
