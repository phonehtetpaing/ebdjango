# -*- coding: utf-8 -*-
# import models
import ast

from django.http import HttpResponse

from apps.core.models.end_user import EndUser
from apps.qa.models.end_user_questionnaire import EndUserQuestionnaire
from apps.qa.models.questionnaire import Questionnaire
from apps.qa.models.questionnaire_question import QuestionnaireQuestion
from apps.qa.models.response import Response
from apps.qa.models.coupon_claim import CouponClaim

# import views
from apps.qa.views.utilities.send_message import questionnaire_command_message
from apps.qa.views.utilities.send_message import questionnaire_text_message
from apps.qa.views.utilities.send_message import questionnaire_question_message


def process_questionnaire_sequence(payload_dict, end_user_info):
    """
    Updates the questionnaire sequence state of the associated user with the provided message data.
    If no message sequence state could be found a new one is generated before processing the data.
    :param payload_dict: payload of incoming message
    :param text: plain text of incoming message
    :param end_user_info: information object of associated user
    """
    end_user = end_user_info["end_user_obj"]
    print('debugging questionnaire response ', payload_dict)
    if not payload_dict:
        raise AttributeError("no payload or text input was found, this message cannot be processed")

    # get questionnaire
    questionnaire_id = int(payload_dict['questionnaire_id'])
    end_user_questionnaire = get_or_create_user_questionnaire(end_user_info, questionnaire_id)

    # determine message type (start/response/ping/stop)
    if payload_dict['type']:
        message_type = payload_dict['type']

        if message_type == 'start':
            print('type start')
            process_start(end_user_info, end_user_questionnaire)
            return process_response(end_user_info, end_user_questionnaire, payload_dict)
        if message_type == 'stop':
            print('type stop')
            return process_stop(end_user_info, end_user_questionnaire)
        if message_type == 'ping':
            print('type ping')
            return process_ping()
        if message_type == 'response':
            print('type response')
            more_to_come = process_response(end_user_info, end_user_questionnaire, payload_dict)
            if not more_to_come:
                process_stop(end_user_info, end_user_questionnaire)
            return

    raise LookupError("the type of the message could not be determined or is unknown")


def process_start(end_user_info, end_user_questionnaire):
    """
    Register the start of a new questionnaire sequence and returns the intro text for
    the requested questionnaire
    :param end_user_questionnaire:
    :return:
    """
    questionnaire_text_message(end_user_info, end_user_questionnaire.questionnaire.intro)
    return end_user_questionnaire.questionnaire.intro


def process_stop(end_user_info, end_user_questionnaire):
    """
    Registers a stop event for the questionnaire either due to the user finishing the questionnaire, manually closing
    the window or a timeout event occurring.
    :param end_user_questionnaire:
    :return:
    """
    questionnaire_command_message(end_user_info, end_user_questionnaire.questionnaire.outro, "stop")

    """
        if we have an email address check if we have an end_user with that same email
        if so then merge the data with existing user and delete the new one.
        
        else do nothing.
    """
    end_user = end_user_info["end_user_obj"]
    end_user_email = end_user.email
    if end_user_email:
        end_users = EndUser.objects.filter(email=end_user_email).order_by('id')
        print('debugging user merging ', end_users)
        if end_users.count() > 1:
            main_user = end_users.first()

            for user in end_users.all():
                if main_user.id != user.id:
                    print('debugging main user', main_user.id, 'newer user', user.id)
                    merge_end_users(main_user, user)

    return end_user_questionnaire.questionnaire.outro


def process_ping():
    """
    Returns an OK response to keep connections alive
    """
    return HttpResponse(200)


def process_response(end_user_info, end_user_questionnaire, payload_dict):
    if payload_dict['response_id'] and payload_dict['response_content']:
        # determine which question is being answered
        response_question_id = int(payload_dict['response_id'])
        response_question = QuestionnaireQuestion.objects.filter(id=response_question_id,
                                                                 questionnaire_id=end_user_questionnaire.questionnaire.id).first()

        # store response for question
        set_question_response(end_user_info, end_user_questionnaire, response_question,
                              payload_dict['response_content'])

    # determine which question to return
    current_question = get_current_question(end_user_info, end_user_questionnaire)
    if current_question and not isinstance(current_question, bool):
        questionnaire_question_message(end_user_info, current_question)
    # return new question
    return current_question


def get_or_create_user_questionnaire(end_user_info, questionnaire_id):
    """
    Determines if there is an existing, unfinished questionnaire instance for the user and if so returns that.
    If it doesn't create and return a new instance.

    :param end_user_info:
    :param questionnaire_id:
    :return:
    """
    end_user = end_user_info["end_user_obj"]

    questionnaire = Questionnaire.objects.filter(id=questionnaire_id).first()
    if not questionnaire:
        raise LookupError("the specified questionnaire does not exist")

    end_user_questionnaire = EndUserQuestionnaire.objects.filter(end_user=end_user, questionnaire=questionnaire)
    if end_user_questionnaire:
        end_user_questionnaire = end_user_questionnaire.latest('regist_dt')
    else:
        end_user_questionnaire = EndUserQuestionnaire()
        end_user_questionnaire.end_user = end_user
        end_user_questionnaire.questionnaire = questionnaire
        end_user_questionnaire.save()

    return end_user_questionnaire


def get_current_question(end_user_info, end_user_questionnaire):
    """
    Returns the first question associated with the questionnaire that does not have a registered response.
    If no questions can be found a LookupError is raised.
    :param end_user_info:
    :param end_user_questionnaire:
    :return:
    """
    end_user = end_user_info["end_user_obj"]

    questions = QuestionnaireQuestion.objects.filter(questionnaire_id=end_user_questionnaire.questionnaire.id)
    responses = Response.objects.filter(end_user_questionnaire=end_user_questionnaire)

    # catch possible errors
    if not questions or questions.count() == 0:
        raise LookupError("the specified questionnaire does not have any questions associated with it")

    # if we have responses for all questions we have no questions to answer
    if responses.count() >= questions.count():
        return False

    # if we have no responses return the first question
    if responses.count() == 0:
        current_question = QuestionnaireQuestion.objects.filter(questionnaire_id=end_user_questionnaire.questionnaire.id, display_order=1).first()
        return current_question
    # if we have registered responses for this user questionnaire pick the first question without a response
    if responses.count() < questions.count():
        current_question = QuestionnaireQuestion.objects.filter(questionnaire_id=end_user_questionnaire.questionnaire.id, display_order=(responses.count() + 1)).first()
        return current_question


def set_question_response(end_user_info, end_user_questionnaire, questionnaire_question, response):
    """
    Stores the response to a questionnaire question if the question and questionnaire exist, else a LookupError is thrown.
    :param end_user_info:
    :param end_user_questionnaire:
    :param questionnaire_question:
    :param response:
    """
    end_user = end_user_info["end_user_obj"]

    # catch possible errors
    if not end_user_questionnaire or not questionnaire_question:
        raise LookupError("attempted to store response for unspecified questionnaire or question")

    question_response = Response.objects.filter(end_user=end_user, end_user_questionnaire=end_user_questionnaire, questionnaire_question=questionnaire_question).first()
    if not question_response:
        question_response = Response()
        question_response.end_user = end_user
        question_response.end_user_questionnaire = end_user_questionnaire
        question_response.questionnaire_question = questionnaire_question
    question_response.content = response
    question_response.save()

    # todo rework this into a more general solution for other attribute types too
    if questionnaire_question.question.type.name == 'registration':
        eval_opts = ast.literal_eval(questionnaire_question.question.question_options)
        print('debugging registration type message', eval_opts, response)
        if eval_opts == 'email':
            end_user.email = response
        if eval_opts == 'tel1':
            end_user.tel1 = response
        if eval_opts == 'address1':
            end_user.address1 = response
        if eval_opts == 'first_name':
            end_user.first_name = response
        if eval_opts == 'last_name':
            end_user.last_name = response

        end_user.save()


def merge_end_users(main_user, duplicate_user):
    """
    Merges two EndUser model instances into one.
    This is mainly usefull to transfer new data to an older instance when we discover it is the same person
    using email.
    :param main_user:
    :param duplicate_user:
    :return:
    """

    # copy all properties from the duplicate user to the main user
    if duplicate_user.first_name and not duplicate_user.first_name in [None, '']:
        main_user.first_name = duplicate_user.first_name

    if duplicate_user.last_name and not duplicate_user.last_name in [None, '']:
        main_user.last_name = duplicate_user.last_name

    if duplicate_user.email and not duplicate_user.email in [None, '']:
        main_user.email = duplicate_user.email

    if duplicate_user.tel1 and not duplicate_user.tel1 in [None, '']:
        main_user.tel1 = duplicate_user.tel1

    if duplicate_user.prefecture and not duplicate_user.prefecture in [None, '']:
        main_user.prefecture = duplicate_user.prefecture

    if duplicate_user.zip_code and not duplicate_user.zip_code in [None, '']:
        main_user.zip_code = duplicate_user.zip_code

    if duplicate_user.birth_date and not duplicate_user.birth_date in [None, '']:
        main_user.birth_date = duplicate_user.birth_date

    # change user references on questionnaires from the duplicate user to the main user
    new_questionnaires = EndUserQuestionnaire.objects.filter(end_user=duplicate_user).update(end_user=main_user)
    new_responses = Response.objects.filter(end_user=duplicate_user).update(end_user=main_user)
    new_coupon_cliams = CouponClaim.objects.filter(end_user=duplicate_user).update(end_user=main_user)

    # delete the duplicate user since it is no longer needed
    main_user.save()
    duplicate_user.delete()
