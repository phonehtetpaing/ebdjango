# -*- coding: utf-8 -*-
# import messaging
from apps.core.views.messaging_native_chat.fbms.file_send_message import *
from apps.core.views.messaging_native_chat.line.image_send_message import *
from apps.core.views.messaging_native_chat.contactchat.file_message import *


def file_send_message(end_user_info, param):
    if "fbms" in end_user_info["platform"]:
        fbms_file_send_message(end_user_info, param)

    elif "line" in end_user_info["platform"]:
        line_image_send_message(end_user_info, param)

    elif "contactchat" in end_user_info["platform"]:
        contactchat_file_send_message(end_user_info, param)

    else:
        pass
