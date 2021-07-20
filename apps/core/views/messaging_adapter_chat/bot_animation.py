# -*- coding: utf-8 -*-
# import messaging
from apps.core.views.messaging_native_chat.fbms.bot_animation import *


def animation_typing(end_user_info, param):
    if "fbms" in end_user_info["platform"]:
        fbms_animation_typing(end_user_info, param)

    # TODO support line when possible
    else:
        pass
