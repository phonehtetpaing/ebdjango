# -*- coding: utf-8 -*-
# import messaging
from apps.core.views.messaging_native_chat.fbms.quick_reply_message import *
from apps.core.views.messaging_native_chat.line.buttons_template_message import *
from apps.core.views.messaging_native_chat.contactchat.quick_reply_message import *


def button_select_message(end_user_info, param):
    if "fbms" in end_user_info["platform"]:
        fbms_quick_reply_message(end_user_info, param)

    elif "line" in end_user_info["platform"]:
        line_buttons_template_message(end_user_info, param)

    elif "contactchat" in end_user_info["platform"]:
        contactchat_quick_reply_message(end_user_info, param)

    else:
        pass
