from django.shortcuts import render
from copy import deepcopy
import re
import ast
import json
import deprecation

""" current parser version """
__version__ = 2.0


def vendor_to_mesasge(json_str):
    """  Vendor Message Data to Common JSON FORMAT"""

    json_str_org = json_str.replace("\'", "\"")
    json_org_dict = json.loads(json_str_org)
    message_dict = dict()

    if json_org_dict["type"] == "textsendmessage":

        message_dict = {
            "text": json_org_dict["payload"]
        }

    elif json_org_dict["type"] == "imagesendmessage":
        # TODO: check extension & set type (image or file)

        message_dict = {
            "type": "image",
            "url": json_org_dict["payload"],
        }

    elif json_org_dict["type"] == "carouselsendmessage":

        # TODO:
        button_title = "View on Web"

        element_list = []
        payload_list = json_org_dict["payload"]
        for payload in payload_list:
            element_dict = {
                "title": payload["title"],
                "url": payload["actions"],
                "image_url": payload["image_url"],
                "subtitle": payload["subtitle"],
                "buttons": [
                    {
                        "type": "url",
                        "title": button_title,
                        "data": payload["actions"]
                    }
                ]
            }
            element_list.append(element_dict)

        message_dict = {
            "elements": element_list
        }

    return message_dict


def parse_messages(data):
    print(data)
    # build a list of messages
    messages = []

    templateSend = {
        "type": "carouselsendmessage",
        "version": "1.0",
        "payload": {
            "elements": []
        }
    }

    templateSendElement = {
        "title": "",
        "image_url": "",
        "subtitle": "",
        "actions": []
    }

    # these are the expression used to determine how many of a given type there are
    message_exp = re.compile('(TextSendMessage_0_)')
    img_exp = re.compile('(ImageSendMessage_original_content_url_0)')
    file_exp = re.compile('(FileSendMessage_)')
    template_exp = re.compile('(CarouselTemplate_alt_text_0_)')
    tmpl_url_exp = re.compile('(column_thumbnail_image_url_)')
    tmpl_title_exp = re.compile('(column_title_)')
    tmpl_text_exp = re.compile('(column_text_)')
    tmpl_action_exp = re.compile('(column_action_json_)')
    quickreply_exp = re.compile('(QuickReplySendMessage_title_)')
    wait_exp = re.compile('(WaitSendMessage_)')
    tag_exp = re.compile('(TagSendMessage_)')
    todo_exp = re.compile('(TodoSendMessage_)')
    input_exp = re.compile('(InputSendMessage_)')
    form_exp = re.compile('(FormSendMessage_)')
    goto_exp = re.compile('(GoToMessage_)')

    # helper variables for template dict construction
    current_template = {}
    current_template_column_size = 0
    current_template_columns = []

    # add general message items to a list to maintain order
    for index, key in enumerate(data):
        if message_exp.match(key):
            messages.append(parse_text_message(index, key, data))

        elif img_exp.match(key):
            messages.append(parse_img_message(index, key, data))

        elif file_exp.match(key):
            messages.append(parse_file_message(index, key, data))

        # POST data is in order, we encounter only template related data before spotting another message type
        # ! template parsing start
        elif template_exp.match(key):
            tmp_obj = deepcopy(templateSend)
            current_template = tmp_obj
            # reset helper variables
            current_template_column_size = 0
            current_template_columns = []

        # first encounter of a column for current template
        # parse template column and img_url
        elif tmpl_url_exp.match(key):
            current_template_column_size = len(data.getlist(key))

            for x in range(current_template_column_size):
                tmp_obj = deepcopy(templateSendElement)
                tmp_obj['image_url'] = data.getlist(key)[x]
                current_template_columns.append(tmp_obj)

        # parse column title
        elif tmpl_title_exp.match(key):
            for x in range(0, current_template_column_size):
                tmp_obj = current_template_columns[x]
                tmp_obj['title'] = data.getlist(key)[x]

        # parse column subtitle
        elif tmpl_text_exp.match(key):
            for x in range(0, current_template_column_size):
                tmp_obj = current_template_columns[x]
                tmp_obj['subtitle'] = data.getlist(key)[x]

        # parse column json action
        elif tmpl_action_exp.match(key):
            for x in range(0, current_template_column_size):
                tmp_obj = current_template_columns[x]
                tmp_obj['actions'] = data.getlist(key)[x]

            current_template['payload'] = current_template_columns
            messages.append(current_template)
        # ! template parsing end

        # parse quickreplies
        elif quickreply_exp.match(key):
            messages.append(parse_quick_reply(index, key, data))

        # parse waits
        elif wait_exp.match(key):
            messages.append(parse_wait(index, key, data))

        # parse tag adding/deleting
        elif tag_exp.match(key):
            messages.append(parse_tag(index, key, data))

        # parse to-do adding
        elif todo_exp.match(key):
            messages.append(parse_todo(index, key, data))

        # parse raw input
        elif input_exp.match(key):
            messages.append(parse_input(index, key, data))

        # parse form definition
        elif form_exp.match(key):
            messages.append(parse_form(index, key, data))

        # parse goto
        elif goto_exp.match(key):
            messages.append(parse_goto(index, key, data))

    return messages


def parse_text_message(index, key, data):
    """ Parses a text message from raw POST data"""
    text_send = {
        "type": "textsendmessage",
        "version": "1.0",
        "payload": ""
    }

    tmp_obj = deepcopy(text_send)
    tmp_obj['payload'] = data[key]

    return tmp_obj


def parse_img_message(index, key, data):
    """ Parses an image message from raw POST data """
    image_send = {
        "type": "imagesendmessage",
        "version": "1.0",
        "payload": ""
    }

    tmp_obj = deepcopy(image_send)
    tmp_obj['payload'] = data[key]

    return tmp_obj


def parse_file_message(index, key, data):
    """ Parses a file message from raw POST data """
    image_send = {
        "type": "filesendmessage",
        "version": "1.0",
        "payload": ""
    }

    tmp_obj = deepcopy(image_send)
    tmp_obj['payload'] = data[key]

    return tmp_obj


def parse_quick_reply(index, key, data):
    """
    Parses a quick reply message object from raw POST data

    The parse function relies heavily on the structure of the form,
    in this case the parser assumes that a QuickReply consists of two components:
    an array of labels for each option button, an array of block identifiers for each option button
    that indicates which message block to proceed to upon taking that option.

    Parameters
    ----------
    index : int
        The index of the current key in the greater iteration loop.
    key : str
        The current key that is being evaluated.
    data : dict
        The data dictionary that is being iterated over.

    Returns
    -------
    dict
        Dictionary describing the parsed QuickReply message.

    """

    template_quick_reply = {
        "type": "quickreplysendmessage",
        "version": "1.0",
        "question": "",
        "payload": []
    }

    template_quick_reply_element = {
        "title": "",
        "payload": ""
    }

    quick_reply_message = deepcopy(template_quick_reply)
    header_text = data.get(list(data.keys())[index - 1])
    label_list = list(data.getlist(key))
    goto_list = list(data.getlist(list(data.keys())[index + 1]))

    for x in range(len(label_list)):
        tmp_obj = deepcopy(template_quick_reply_element)
        tmp_obj['title'] = label_list[x]
        tmp_obj['payload'] = goto_list[x]
        quick_reply_message['payload'].append(tmp_obj)

    quick_reply_message['question'] = header_text
    return quick_reply_message


def parse_wait(index, key, data):
    """
    Parses a wait command from raw POST data

    Wait commands instruct the bot to wait a specified amount of ms before proceeding with the next action. If the
    recipient is using Facebook Messenger a (...) animation will appear to indicate someone is typing a new reply.

    Parameters
    ----------
    index : int
        The index of the current key in the greater iteration loop.
    key : str
        The current key that is being evaluated.
    data : dict
        The data dictionary that is being iterated over.

    Returns
    -------
    dict
        Dictionary describing the parsed wait command.

    """
    template_wait = {
        "type": "waitsendmessage",
        "version": "1.0",
        "payload": ""
    }

    tmp_obj = deepcopy(template_wait)
    tmp_obj['payload'] = data[key]

    return tmp_obj


def parse_tag(index, key, data):
    """ Parses a tag message from raw POST data"""
    template_tag = {
        "type": "tagsendmessage",
        "version": "1.0",
        "payload": {
            "mode": "",
            "tag": ""
        }
    }

    tag_data = list(data.getlist(key))
    tmp_obj = deepcopy(template_tag)
    tmp_obj['payload']['mode'] = tag_data[0]
    tmp_obj['payload']['tag'] = tag_data[1]

    return tmp_obj


# @deprecation.deprecated(deprecated_in="2.0", removed_in="3.0",
#                         current_version=__version__,
#                         details="Use the parse_form function instead to achieve similar functionality")
def parse_todo(index, key, data):
    """ Parses a to-do item from raw POST data"""
    template_todo = {
        "type": "todosendmessage",
        "version": "1.0",
        "payload": {
            "question": "",
            "title": "",
            "memo": ""
        }
    }

    todo_data = list(data.getlist(key))
    tmp_obj = deepcopy(template_todo)
    tmp_obj["payload"]["question"] = todo_data[0]
    tmp_obj["payload"]["title"] = todo_data[1]
    tmp_obj["payload"]["memo"] = todo_data[2]

    return tmp_obj


# @deprecation.deprecated(deprecated_in="2.0", removed_in="3.0",
#                         current_version=__version__,
#                         details="Use the parse_form function instead to achieve similar functionality")
def parse_input(index, key, data):
    """ Parses an input item from raw POST data """
    template_input = {
        "type": "inputsendmessage",
        "version": "1.0",
        "payload": {
            "question": "",
            "attribute": ""
        }
    }

    input_data = list(data.getlist(key))
    tmp_obj = deepcopy(template_input)
    tmp_obj["payload"]["question"] = input_data[0]
    tmp_obj["payload"]["attribute"] = input_data[1]

    return tmp_obj

# ---------
# Message API v2.0 only features
# ---------


def parse_form(index, key, data):
    """ Parses a form item from raw POST data """
    template_form = {
        "type": "formsendmessage",
        "version": "2.0",
        "title": "",
        "memo": "",
        "todo": False,
        "payload": []
    }

    template_form_child = {
        "question": "",
        "attribute": ""
    }

    form_data = list(data.getlist(key))
    tmp_obj = deepcopy(template_form)

    tmp_obj["title"] = form_data[0]
    tmp_obj["memo"] = form_data[1]

    # we verify if the 3 element indicates an to-do item or indicates the start of the attribute/question list
    child_start_index = 2
    if form_data[2] == "todo":
        tmp_obj["todo"] = True
        child_start_index = 3

    questions = form_data[child_start_index::]

    # attributes and questions are alternated in the form data so we parse them one by one
    for count, question in enumerate(questions):
        if not count % 2 == 1:
            tmp_child = deepcopy(template_form_child)
            tmp_child["attribute"] = question
        else:
            tmp_child["question"] = question
            tmp_obj["payload"].append(tmp_child)

    return tmp_obj


def parse_goto(index, key, data):
    """ Parses a goto action from raw POST data"""
    template_goto = {
        "type": "gotomessage",
        "version": "2.0",
        "payload": []
    }

    goto_data = list(data.getlist(key))
    tmp_obj = deepcopy(template_goto)
    # add block_id
    tmp_obj['payload'].append(goto_data[0])
    # add step_id
    tmp_obj['payload'].append(goto_data[1])

    return tmp_obj
