# -*- coding: utf-8 -*-
# import messaging
from apps.core.views.messaging_native_chat.fbms.text_send_message import *
from apps.core.views.messaging_native_chat.line.text_send_message import *
from apps.core.views.messaging_native_chat.contactchat.text_message import *


def text_send_message(end_user_info, param):
    if "fbms" in end_user_info["platform"]:
        fbms_text_send_message(end_user_info, param)

    elif "line" in end_user_info["platform"]:
        line_text_send_message(end_user_info, param)

    elif "contactchat" in end_user_info["platform"]:
        contactchat_text_message(end_user_info, param)

    else:
        pass
