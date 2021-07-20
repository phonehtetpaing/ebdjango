# -*- coding: utf-8 -*-
import json
# import models
from apps.core.models.end_user_story import EndUserStory
from apps.core.models.payload import Payload

# import views
from apps.core.views.bot_common.end_user_story_history import *
from apps.core.views.messaging_adapter_chat.text_send_message import *
from apps.core.views.messaging_adapter_chat.image_send_message import *
from apps.core.views.messaging_adapter_chat.carousel_send_message import *
from apps.core.views.messaging_adapter_chat.button_select_message import *
from apps.core.views.bot_common.tag_settings import *


def start_end_user_story(payload_text, text, end_user_info):
    end_user = end_user_info["end_user_obj"]

    # text input
    if text:
        payload = Payload.objects.filter(value="__text_input", vendor_branch=end_user_info["vendor_branch"]).first()

    # payload
    else:
        payload = Payload.objects.filter(value=payload_text, vendor_branch=end_user_info["vendor_branch"]).first()

    if payload:
        end_user_stories = EndUserStory.objects.filter(payload_id=payload.id, end_user_state=end_user.end_user_state_id, is_delete=0).order_by('run_order_num')

        for end_user_story in end_user_stories:
            param_dict = json.loads(end_user_story.messaging_api_param_json)

            if end_user_story.messaging_api_type.cd == "text":
                text_send_message(end_user_info, param_dict)

            elif end_user_story.messaging_api_type.cd == "file":
                file_send_message(end_user_info, param_dict)

            elif end_user_story.messaging_api_type.cd == "carousel":
                carousel_send_message(end_user_info, param_dict)

            elif end_user_story.messaging_api_type.cd == "button_select":
                button_select_message(end_user_info, param_dict)

            # update payload / text in latest history record
            if text:
                update_payload_history(text, end_user_info)
            else:
                update_payload_history(payload_text, end_user_info)

            # set end_user_story_history
            set_end_user_history(end_user_info, end_user_story)

        # TODO: set tag data
        set_tag(end_user, payload)

        # Set user state
        end_user_story = EndUserStory.objects.filter(payload_id=payload.id, end_user_state=end_user.end_user_state_id, is_delete=0).order_by('-run_order_num').first()
        end_user.end_user_state_id = end_user_story.next_end_user_state_id
        end_user.save()
        return True

    return False
