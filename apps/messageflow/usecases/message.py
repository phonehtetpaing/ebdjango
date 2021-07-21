# -*- coding: utf-8 -*-
# import models
import random

from django.http import HttpResponse

# import models
from apps.messageflow.models.bot import Bot, BotScenario
from apps.messageflow.models.message import MessageBlock, Message, EndUserBotScenario, LogLine
from apps.messageflow.usecases.line import *
from apps.messageflow.usecases.line import _line_send_bulk_message
from apps.messageflow.usecases.line import line_text_send_message, line_image_send_message, \
    line_option_send_message
from apps.messageflow.usecases.settings import get_line_token_dict_from_request


class MessageFLowStateError(Exception):
    pass


class MessageFlowPayloadError(Exception):
    pass


class SendDirectMessage:
    """
       Use case for sending a direct message through LINE
       """

    def __init__(
            self,
            request,
            recipient,
            message,
    ):
        # Set the internal state for the operation
        self._request = request
        self._recipient = recipient
        self._message = message

    def execute(self):
        self.valid_data()
        return self._send_direct_message()

    def valid_data(self):
        if not self._recipient or self._recipient == "":
            raise MessageFlowPayloadError(
                "no recipient was found, this request cannot be processed"
            )

        if not self._message or self._message == "":
            raise MessageFlowPayloadError(
                "no message was found, this request cannot be processed"
            )
        return True

    def _send_direct_message(self):
        token_dict = get_line_token_dict_from_request(self._request)

        logline = LogLine(
            message=self._message,
            user_id=self._recipient.id,
            owner_id=self._request.user.id,
            app_id='nchat',
            is_user_message=False
        )
        logline.save()

        return line_text_send_message(token_dict['line_channel_access_token'], self._recipient, self._message)


# todo this should be seperated into two parts: creating chunks and sending a multicast for a specific chunk

def process_user_bot_scenario_sequence(payload_dict, end_user_info):
    """
    Updates the end_user_bot_scenario sequence state of the associated user with the provided message data.
    If no end user bot scenario could be found a new one is generated before processing the data.
    :param payload_dict: payload of incoming message
    :param text: plain text of incoming message
    :param end_user_info: information object of associated user
    """
    if not payload_dict or (not payload_dict['text'] and not payload_dict['payload']):
        raise AttributeError("no payload or text input was found, this message cannot be processed")

    end_user = end_user_info["end_user_obj"]
    token_dict = end_user_info["line_token_dict"]
    end_user_bot_scenario = get_or_create_user_bot_scenario(end_user_info, int(token_dict['bot_id']))

    # log user response
    if payload_dict['text']:
        write_log(end_user_bot_scenario, payload_dict['text'], True)

    # check payload
    if payload_dict['payload'] and payload_dict['payload'] == 'GET_STARTED_PAYLOAD':
        reset_end_user_bot_scenario(end_user_bot_scenario)

    # process received message with flow
    return process_response(end_user_info, end_user_bot_scenario, payload_dict)


def reset_end_user_bot_scenario(end_user_bot_scenario):
    start_message = end_user_bot_scenario.start_block.start_message
    end_user_bot_scenario.current_message = start_message
    end_user_bot_scenario.sate = 'INITIAL'
    end_user_bot_scenario.save()


def process_response(end_user_info, end_user_bot_scenario, payload_dict):
    print('debug', end_user_bot_scenario)
    if end_user_bot_scenario.state == 'INITIAL':
        current_message = Message.objects.filter(
            message_block=end_user_bot_scenario.current_message.message_block,
            display_order=end_user_bot_scenario.current_message.display_order).first()
    elif end_user_bot_scenario.state == 'WAITING' and not payload_dict['payload'] == 'continue':
        current_message = process_wait_state(end_user_bot_scenario, payload_dict)
    else:
        current_message = Message.objects.filter(
            message_block=end_user_bot_scenario.current_message.message_block,
            display_order=end_user_bot_scenario.current_message.display_order + 1).first()

    # if this was the last message the scenario is done
    if not current_message:
        return HttpResponse(200)

    # log the bot response
    write_log(end_user_bot_scenario, current_message.json_content, False)

    line_token_dict = end_user_info["line_token_dict"]
    channel_access_token = line_token_dict["line_channel_access_token"]
    end_user = end_user_info["end_user_obj"]
    message_type = current_message.type

    # if text message send and loop to next message
    if message_type.name == 'text':
        line_text_send_message(channel_access_token, end_user, current_message.json_content)
        end_user_bot_scenario.current_message = current_message
        end_user_bot_scenario.state = 'CONT'
        end_user_bot_scenario.save()
        return process_response(end_user_info, end_user_bot_scenario, payload_dict)
    if message_type.name == 'image':
        line_image_send_message(channel_access_token, end_user, current_message.json_content)
        end_user_bot_scenario.current_message = current_message
        end_user_bot_scenario.state = 'CONT'
        end_user_bot_scenario.save()
        return process_response(end_user_info, end_user_bot_scenario, payload_dict)
    if message_type.name == 'file':
        line_file_send_message(channel_access_token, end_user, current_message.json_content)
        end_user_bot_scenario.current_message = current_message
        end_user_bot_scenario.state = 'CONT'
        end_user_bot_scenario.save()
        return process_response(end_user_info, end_user_bot_scenario, payload_dict)
    if message_type.name == 'option':
        line_option_send_message(channel_access_token, end_user, current_message.json_content, current_message.options_dict)
        end_user_bot_scenario.current_message = current_message
        end_user_bot_scenario.state = 'WAITING'
        end_user_bot_scenario.save()

    return HttpResponse(200)


def process_wait_state(end_user_bot_scenario, payload_dict):
    # make sure that either payload or text is set when processing WAITING state
    if not payload_dict['payload'] and not payload_dict['text']:
        raise MessageFLowStateError(
            "no payload or text input was found, while state was WAITING, this message cannot be processed"
        )

    # if option type check if payload contains one of the options
    if not end_user_bot_scenario.current_message.type.name == 'option':
        raise MessageFLowStateError(
            "invalid message type, {} for WAITING state".format(end_user_bot_scenario.current_message.type.name)
        )

    if not payload_dict['payload'].isdigit():
        raise MessageFlowPayloadError(
            "Unknown payload, {} during WAITING state".format(payload_dict['payload'])
        )

    message_block = MessageBlock.objects.filter(
        id=int(payload_dict['payload']),
        scenario=end_user_bot_scenario.scenario
    ).first()

    # this is a debugging safeguard with a fallback in case of invalid state switches
    if not message_block:
        print('DEBUG ERROR message block not found', payload_dict['payload'], end_user_bot_scenario.scenario.id)
        current_message = end_user_bot_scenario.current_message
    else:
        current_message = message_block.start_message

    return current_message


def write_log(end_user_bot_scenario, message, is_user_message=True):
    """
    Writes a a log entry for this message
    :param end_user_bot_scenario:
    :param message:
    :param is_user_message: a value of False implies the message came from a vendor or bot
    """
    new_response = LogLine(
        end_user_bot_scenario=end_user_bot_scenario,
        message=message,
        user_id=end_user_bot_scenario.user_id,
        owner_id=end_user_bot_scenario.owner_id,
        app_id=end_user_bot_scenario.app_id,
        is_user_message=is_user_message
    )
    new_response.save()


def process_ping():
    """
    Returns an OK response to keep connections alive
    """
    return HttpResponse(200)


def get_or_create_user_bot_scenario(end_user_info, bot_id):
    """
    Determines if there is an existing, unfinished bot scenario instance for the user and if so returns that.
    If it doesn't, create and return a new instance.

    :param end_user_info:
    :param bot_id:
    :return:
    """
    end_user = end_user_info["end_user_obj"]

    bot = Bot.objects.filter(id=bot_id).first()
    if not bot:
        raise LookupError("the specified bot does not exist")

    # check if we have an ongoing bot scenario for this user if so continue from there
    user_scenario = EndUserBotScenario.objects.filter(bot=bot, user_id=end_user.id)
    if user_scenario:
        user_scenario = user_scenario.latest('regist_dt')
    # if not use the bot scenario weights to determine which scenario to return
    else:
        user_scenario = create_user_bot_scenario(bot, end_user)

    return user_scenario


def create_user_bot_scenario(bot, end_user):
    bot_scenarios = BotScenario.objects.filter(bot=bot)
    scenario_list = []
    weight_list = []
    for bot_scenario in bot_scenarios:
        scenario_list.append(bot_scenario.scenario)
        weight_list.append(bot_scenario.weight)
    new_scenario = random.choices(
        population=scenario_list,
        weights=weight_list,
        k=1
    )
    new_scenario = new_scenario[0]
    print('debugging new scenario', new_scenario.message_block_set.all())
    user_scenario = EndUserBotScenario(
        bot=bot,
        scenario=new_scenario,
        current_message=new_scenario.start_block.start_message,
        user_id=end_user.id,
        owner_id=new_scenario.owner_id,
        app_id=new_scenario.app_id
    )
    user_scenario.save()
    return user_scenario


def filter_targeted_message_recipients(request, recipients):
    if request.POST:
        request_type = request.POST
    else:
        request_type = request.GET

    filter_birth_month = request_type.get('filter_birth_month', None)
    filter_birth_year_min = request_type.get('filter_birth_year_min', None)
    filter_birth_year_max = request_type.get('filter_birth_year_max', None)
    filter_regist_dt_min = request_type.get('filter_regist_dt_min', None)
    filter_regist_dt_max = request_type.get('filter_regist_dt_max', None)
    filter_gender = request_type.get('filter_gender', None)

    if filter_birth_month and filter_birth_month != 'any':
        recipients = recipients.filter(birth_date__month=filter_birth_month)
    if filter_gender and filter_gender != 'any':
        recipients = recipients.filter(gender=filter_gender)
    recipients = filter_date_range(recipients, "birth_date", filter_birth_year_min, filter_birth_year_max)
    recipients = filter_date_range(recipients, "regist_dt", filter_regist_dt_min, filter_regist_dt_max)

    return recipients


def filter_date_range(date_set, field, date_min=None, date_max=None):
    from datetime import date
    filter_field = field + "__range"
    print("filter_field: ", filter_field)
    if date_min or date_max:
        if date_min:
            filter_date_min = str(date_min)
        else:
            filter_date_min = "1900-1-1"
        if date_max:
            filter_date_max = str(date_max)
        else:
            filter_date_max = str(date.today())
        date_set = date_set.filter(**{filter_field: [filter_date_min, filter_date_max]})
    return date_set


def send_targeted_message(request, message_formset, recipients):
    token_dict = get_line_token_dict_from_request(request)
    message_list = []
    for message_form in message_formset.forms:
        if not message_formset._should_delete_form(message_form):
            message_form.save(commit=False)
            message_list.append({"display_order": message_form.instance.display_order,
                                 "json_content": message_form.instance.json_content,
                                 "type": message_form.instance.type})

    for message in sorted(message_list, key=lambda i: i['display_order']):
        _line_send_bulk_message(token_dict['line_channel_access_token'], recipients, message["json_content"], message["type"])
