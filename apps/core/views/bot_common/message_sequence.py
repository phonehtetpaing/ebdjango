# -*- coding: utf-8 -*-
import ast
import json
import itertools
import time
from copy import deepcopy

# import models
from apps.core.models.message_sequence import MessageSequence
from apps.core.models.message_block import MessageBlock
from apps.core.models.end_user_sequence_state import EndUserSequenceState
from apps.core.models.todo import Todo
from apps.core.models.end_user_state import EndUserState

# import views
from apps.core.views.bot_common.end_user_story_history import *
from apps.core.views.messaging_adapter_chat.text_send_message import *
from apps.core.views.messaging_adapter_chat.image_send_message import *
from apps.core.views.messaging_adapter_chat.carousel_send_message import *
from apps.core.views.messaging_adapter_chat.button_select_message import *
from apps.core.views.messaging_adapter_chat.input_request_message import *
from apps.core.views.messaging_adapter_chat.bot_animation import *
from apps.core.views.bot_common.tag_settings import *
from apps.core.views.vendor_common.message_json_converter import *
from apps.core.views.logging.end_user_logging import end_user_logger_ms


def update_message_sequence(payload_text, text, end_user_info):
    """
    Updates the message sequence state of the associated user with the provided message data.
    If no message sequence state could be found a new one is generated before processing the data.
    :param payload_text: payload of incoming message
    :param text: plain text of incoming message
    :param end_user_info: information object of associated user
    """
    end_user = end_user_info["end_user_obj"]
    print('== UPDATE ', payload_text, text)

    # text input
    if text:
        if process_input(end_user_info, text):
            return update_message_sequence(None, None, end_user_info)
        else:
            return True

    # payload
    else:
        # go to a specified block directly
        if payload_text and payload_text.isdigit():
            goto_step(end_user_info, int(payload_text), 0)
            return update_message_sequence(None, None, end_user_info)

        # get sequence state to determine what can be done with this payload
        sequence_state = get_or_create_user_sequence_state(end_user_info)

        # todo find a better way
        # temporary reset method
        if payload_text and payload_text == 'GET_STARTED_PAYLOAD':
            goto_step(end_user_info, int(sequence_state.sequence.start_block.id), 0)
            return update_message_sequence(None, None, end_user_info)

        message_block = sequence_state.message_block
        steps = ast.literal_eval(message_block.messaging_api_param_json)

        # iterate over each step in a message block
        for step in steps[sequence_state.step:]:
            sequence_state.step = sequence_state.step + 1

            # log step processing
            log_process_step(end_user_info, message_block.id, sequence_state, steps, step)

            # stop iterating when process_step returns False
            if not process_step(end_user_info, step):
                if step['type'] == 'gotomessage':
                    # since we can jump to the middle of a message block we need to restart the message update
                    # process from the beginning and calculate the available number of steps
                    update_message_sequence(None, None, end_user_info)
                    break
                else:
                    sequence_state.save()
                    break

    return False


def get_or_create_user_sequence_state(end_user_info):
    """
        return the sequence state associated with the end_user_info
        or creates a new one if it did not already exist.
        :param end_user_info: information object of associated user
        :return message sequence state for end_user_info
    """
    end_user = end_user_info["end_user_obj"]

    message_sequence = MessageSequence.objects.filter(vendor_branch=end_user_info["vendor_branch"]).first()
    sequence_state = EndUserSequenceState.objects.filter(user=end_user, sequence=message_sequence.id).first()

    # create a new sequence state for the user in the event it did not exist
    if not sequence_state:
        sequence_state = EndUserSequenceState()
        sequence_state.user = end_user
        sequence_state.sequence = message_sequence
        sequence_state.message_block = message_sequence.start_block
        sequence_state.step = 0
        sequence_state.save()

    return sequence_state


def log_process_step(end_user_info, message_block_id, sequence_state, steps, step):
    """
    Logs the processing of a step for later statistical analysis.
    :param end_user_info: information object of associated user.
    :param message_block_id: Id of of current message_block.
    :param sequence_state: current state of the sequence.
    :param steps: Array of all steps withing this message_block.
    :param step: Current step being processed.
    """
    message_progress = str(sequence_state.step) + "/" + str(len(steps))

    param_dict = {
        "function_name": "process_step",
        "step": step,
        "end_user_info": end_user_info,
        "message": {
            "message_block_id": message_block_id,
            "message_progress": message_progress
        }
    }
    end_user_logger_ms(param_dict)


def process_step(end_user_info, step):
    """
    Process a message sequence step. Depending on the type of the step different actions will be performed that either
    send messages to external messaging services or updates the current message sequence_state.
    :param end_user_info: information object of associated user.
    :param step: Current step being processed.
    :return: True if the message sequence should proceed, False if it should halt.
    """
    end_user = end_user_info["end_user_obj"]
    # intentionally slow down message delivery to prevent a jarring user experience.
    time.sleep(0.5)
    if step['type'] == 'textsendmessage':
        text_send_message(end_user_info, {'text': step['payload']})
        return True
    elif step['type'] == 'imagesendmessage':
        file_send_message(end_user_info, {'type': 'image', 'url': step['payload']})
        return True
    elif step['type'] == 'filesendmessage':
        file_send_message(end_user_info, {'type': 'file', 'url': step['payload']})
        return True
    elif step['type'] == 'waitsendmessage':
        animation_typing(end_user_info, {})
        wait_time = float(step['payload'])
        wait_time = wait_time / 100
        time.sleep(wait_time)
        print('debugging sleep function, somebody used sleep!', wait_time)
        return True
    elif step['type'] == 'carouselsendmessage':
        param_dict = vendor_to_mesasge(str(step))
        carousel_send_message(end_user_info, param_dict)

        return True
    elif step['type'] == 'tagsendmessage':
        tag_payload = step['payload']
        if step['payload']['mode'] == 'add':
            set_tag(end_user, tag_payload)
        else:
            remove_tag(end_user, tag_payload)
        return True
    elif step['type'] == 'inputsendmessage':
        # Pose question
        input_request_message(end_user_info, {'attribute': step['payload']['attribute'], 'text': step['payload']['question']})

        # Set user status and wait for input
        user_waiting_state = EndUserState.objects.filter(cd="WAIT_INPUT").first()
        end_user.end_user_state = user_waiting_state
        end_user.save()

        return False
    elif step['type'] == 'formsendmessage':
        # find the current step inside the form
        form_step = int(end_user.get_attribute_json('_form_step') or 0)

        # update user form attribute
        end_user.set_attribute_json('_form_length', len(step['payload']))
        end_user.set_attribute_json('_form_step', form_step)

        # find the current question
        question = step['payload'][form_step]['question']
        attribute = step['payload'][form_step]['attribute']
        # Pose question
        input_request_message(end_user_info, {'attribute': attribute, 'text': question})

        # Set user status and attributes and wait for input
        user_waiting_state = EndUserState.objects.filter(cd="WAIT_INPUT").first()
        end_user.end_user_state = user_waiting_state
        end_user.save()
        return False
    elif step['type'] == 'quickreplysendmessage':
        # todo optimize message design at some point to avoid this pointless loop
        tmp_dict = deepcopy(step)
        for reply in tmp_dict['payload']:
            reply['content_type'] = 'text'

        button_select_message(end_user_info, {'text': tmp_dict['question'], 'quick_replies': tmp_dict['payload']})

        return False
    elif step['type'] == 'gotomessage':
        block_id = int(step['payload'][0])
        step_id = int(step['payload'][1])
        goto_step(end_user_info, block_id, step_id)

        return False

    else:
        return False


def goto_step(end_user_info, block_id, step_id):
    """
        Updates the message sequence state associated with the end_user_info
        and sets it to the specified step within the specified block.
        :param end_user_info: information object of associated user.
        :param block_id: Id of the message_block to go to.
        :param step_id: Index of step within message_block to go to.
    """
    end_user = end_user_info["end_user_obj"]

    message_sequence = MessageSequence.objects.filter(vendor_branch=end_user_info["vendor_branch"]).first()
    sequence_state = EndUserSequenceState.objects.filter(user=end_user, sequence=message_sequence.id).first()

    message_block = MessageBlock.objects.filter(id=block_id, vendor_branch=end_user_info["vendor_branch"]).first()
    steps = ast.literal_eval(message_block.messaging_api_param_json)

    sequence_state.message_block = message_block
    if step_id < len(steps):
        sequence_state.step = step_id
    else:
        sequence_state.step = 0
    sequence_state.save()


def process_input(end_user_info, text):
    """
    Handles raw text input from incomming messages and updates the user's sequence_state according to the input.
    If the current sequence_state is not expecting raw input the message is ignored and False is returned.
    :param end_user_info: information object of associated user.
    :param text: raw text to process.
    :return: False if not ready for input, else True
    """
    end_user = end_user_info["end_user_obj"]

    user_waiting_state = EndUserState.objects.filter(cd="WAIT_INPUT").first()
    user_normal_state = EndUserState.objects.filter(cd="INITIAL").first()

    # only try to parse input if we are waiting for it
    if end_user.end_user_state.id != user_waiting_state.id:
        print("=== DEBUG we were not waiting for input but got it ===")
        return False

    # remove waiting state from user
    end_user.end_user_state = user_normal_state
    end_user.save()

    # fetch message sequence to see if input can be processed
    sequence_state = get_or_create_user_sequence_state(end_user_info)
    message_block = MessageBlock.objects.filter(id=sequence_state.message_block.id, vendor_branch=end_user_info["vendor_branch"]).first()
    steps = ast.literal_eval(message_block.messaging_api_param_json)

    # input relates to previous message step
    step = steps[(int(sequence_state.step) - 1):][0]

    # finally check message type
    if step['type'] == 'inputsendmessage':
        attribute = step['payload']['attribute']
        if attribute == 'email':
            end_user.email = text
        elif attribute == 'tel1':
            end_user.tel1 = text
        elif attribute == 'address1':
            end_user.address1 = text
        elif attribute == 'first_name':
            end_user.first_name = text
        elif attribute == 'last_name':
            end_user.last_name = text
        elif attribute == 'business_name':
            end_user.business_name = text
        elif attribute == 'instagram_id':
            end_user.instagram_id = text

        end_user.save()
    elif step['type'] == 'formsendmessage':
        process_form(end_user_info, sequence_state, step, text)

    return True


def process_form(end_user_info, sequence_state, step, text):
    """
    Handles raw text input from incoming messages related to ongoing form steps inside a message_block.
    :param end_user_info: information object of associated user.
    :param sequence_state: state of the message_sequence for the associated user.
    :param step: Current form step that is being evaluated.
    :param text: raw text to process.
    """
    end_user = end_user_info["end_user_obj"]

    # first fetch user attributes
    form_step = int(end_user.get_attribute_json('_form_step'))
    form_length = int(end_user.get_attribute_json('_form_length'))
    form_step_attribute = step['payload'][form_step]['attribute']

    # split operations depending on if to-do or not
    if step['todo']:
        status_hidden = TodoActionStatus.objects.filter(name='Hidden').first()
        todo, created = Todo.objects.get_or_create(end_user=end_user, vendor_branch=end_user_info["vendor_branch"], todo_action_status=status_hidden)

        if form_step == 0:
            todo.is_delete = False
            todo.title = step['title']
            todo.memo = step['memo']
            todo.end_user_reply = [{"attribute": form_step_attribute, "value": text}]
        else:
            end_user_replies = ast.literal_eval(todo.end_user_reply)
            end_user_replies.append({"attribute": form_step_attribute, "value": text})
            todo.end_user_reply = end_user_replies

        # make the to-do visible once fully filled in
        if form_step >= (form_length - 1):
            todo.todo_action_status = TodoActionStatus.objects.filter(name='Pending').first()
        todo.save()
    else:
        # when dealing with non to-do we save attributes directly onto the user
        end_user.set_attribute_json(form_step_attribute, text)

    if form_step >= (form_length - 1):
        # if this was the last step in the form reset the step counter and form length
        end_user.set_attribute_json('_form_step', 0)
        end_user.set_attribute_json('_form_length', 0)
    else:
        # update form step
        end_user.set_attribute_json('_form_step', (form_step + 1))

        # if this wasn't the last step in the form ensure the sequence does not proceed
        sequence_state.step = sequence_state.step - 1
        sequence_state.save()

    end_user.save()
