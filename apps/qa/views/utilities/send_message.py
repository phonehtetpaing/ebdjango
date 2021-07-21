# -*- coding: utf-8 -*-
import ast
import json, requests
import traceback
from django.conf import settings
from django.http import HttpResponse

from apps.contactchat import ContactChatApi


def questionnaire_text_message(end_user_info, text):
    """
    Sends a text message to the referenced user using the contactchat api
    :param end_user_info: User to send to
    :param text: text message to send
    :return:
    """
    try:
        verify_token = end_user_info["end_user_obj"].vendor_branch.vendor.contactchat_verify_token
        contactchat_api = ContactChatApi(end_user_info["contactchat_access_token"], verify_token, settings.CONTACTCHAT_BASE_URL)
        status = contactchat_api.push_question(
            end_user_info["user_id"],
            {
                "type": "message",
                "question_text": text,
            }
        )
        print(status)
        return HttpResponse(200)
    except Exception as e:
        print("api exception")
        print(e, traceback.format_exc())
        return HttpResponse(500)


def questionnaire_command_message(end_user_info, text, opt):
    """
    Sends a text message with server command to the referenced user using the contactchat api
    :param end_user_info: User to send to
    :param text: text message to send
    :return:
    """
    try:
        verify_token = end_user_info["end_user_obj"].vendor_branch.vendor.contactchat_verify_token
        contactchat_api = ContactChatApi(end_user_info["contactchat_access_token"], verify_token, settings.CONTACTCHAT_BASE_URL)
        status = contactchat_api.push_question(
            end_user_info["user_id"],
            {
                "type": "message",
                "question_text": text,
                "question_opt": opt,
            }
        )
        print(status)
        return HttpResponse(200)
    except Exception as e:
        print("api exception")
        print(e, traceback.format_exc())
        return HttpResponse(500)


def questionnaire_question_message(end_user_info, question):
    """
    Sends a questionnaire question to the referenced user using the contactchat api
    :param end_user_info: User to send to
    :param question: Question to ask
    """
    try:
        verify_token = end_user_info["end_user_obj"].vendor_branch.vendor.contactchat_verify_token
        contactchat_api = ContactChatApi(end_user_info["contactchat_access_token"], verify_token, settings.CONTACTCHAT_BASE_URL)

        status = contactchat_api.push_question(
            end_user_info["user_id"],
            {
                "type": question.question.type.name,
                "question_text": question.question.question_text,
                "question_opt": convert_opts_to_json(question.question.question_options),
                "question_id": question.id,
            }
        )
        print(status)
        return HttpResponse(200)
    except Exception as e:
        print("api exception")
        print(e, traceback.format_exc())

        return HttpResponse(500)


def convert_opts_to_json(opts):
    """
    Takes a JSON like string or dictionary and converts it into a JSON object
    :param opt:
    """
    if not opts or opts is None:
        return
    eval_opts = ast.literal_eval(opts)
    return eval_opts
