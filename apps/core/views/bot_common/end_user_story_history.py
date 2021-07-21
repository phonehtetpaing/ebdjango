# -*- coding: utf-8 -*-
import json
# import models
from apps.core.models.end_user_story_history import EndUserStoryHistory
from apps.core.models.todo_action_status import TodoActionStatus

# import views


def set_end_user_history(end_user_info, end_user_story):

    try:
        end_user_story_history = EndUserStoryHistory()
        end_user_story_history.vendor_branch_id = end_user_info["vendor_branch_id"]
        end_user_story_history.end_user_story = end_user_story
        end_user_story_history.end_user = end_user_info["end_user_obj"]

        if end_user_story.is_todo:
            todo_action_status = TodoActionStatus.objects.filter(name="NEW").first()
            end_user_story_history.is_todo = True
            end_user_story_history.todo_action_status = todo_action_status

        else:
            todo_action_status = TodoActionStatus.objects.filter(name="None").first()
            end_user_story_history.is_todo = False
            end_user_story_history.todo_action_status = todo_action_status

        end_user_story_history.save()

        return end_user_story_history

    except Exception as e:
        print('%r' % e)
        return None


def update_payload_history(payload_text, end_user_info):

    try:
        end_user_story_history = EndUserStoryHistory.objects.filter(vendor_branch_id=end_user_info["vendor_branch_id"], end_user=end_user_info["end_user_obj"]).order_by('-update_dt').first()
        if end_user_story_history:
            end_user_story_history.end_user_reply = payload_text
            end_user_story_history.save()

            return end_user_story_history

        return None

    except Exception as e:
        print('%r' % e)
        return None
