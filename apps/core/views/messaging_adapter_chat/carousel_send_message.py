# -*- coding: utf-8 -*-
# import messaging
from apps.core.views.messaging_native_chat.fbms.carousel_send_message import *
from apps.core.views.messaging_native_chat.line.carousel_template_message import *
from apps.core.views.messaging_native_chat.contactchat.carousel_message import *


def carousel_send_message(end_user_info, param):
    if "fbms" in end_user_info["platform"]:
        fbms_carousel_send_message(end_user_info, param)

    elif "line" in end_user_info["platform"]:
        line_carousel_template_message(end_user_info, param)

    elif "contactchat" in end_user_info["platform"]:
        contactchat_carousel_send_message(end_user_info, param)

    else:
        pass
