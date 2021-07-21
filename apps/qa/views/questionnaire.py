# -*- coding: utf-8 -*-
import qrcode
import datetime
from django.http import JsonResponse, HttpResponseNotFound
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import timezone
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from copy import deepcopy
import re
import ast
import json

# import models
from apps.qa.models.questionnaire import Questionnaire
from apps.qa.models.end_user_questionnaire import EndUserQuestionnaire
from apps.qa.models.questionnaire_question import QuestionnaireQuestion
from apps.qa.models.question import Question
from apps.qa.models.question_type import QuestionType
from apps.qa.models.response import Response
from apps.core.models.end_user import EndUser
from apps.qa.models.questionnaire_template import QuestionnaireTemplate
from apps.qa.models.questionnaire_template_question import QuestionnaireTemplateQuestion

# import views
from apps.qa.views.common.login_user_info import *
from apps.qa.views.utilities.file_render import FileRender

# import forms
from apps.qa.forms.questionnaire import QuestionnaireForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='/qa/')
def list(request):
    """ QA Editor List """
    user_obj = get_login_user_objects(request)
    active_questionnaire_ids = [questionnaire.id for questionnaire in Questionnaire.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=False) if (questionnaire.status() != 'Completed')]
    questionnaires = Questionnaire.objects.filter(id__in=active_questionnaire_ids)
    templates = QuestionnaireTemplate.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(questionnaires, 20)
    try:
        questionnaires = paginator.page(page)
    except PageNotAnInteger:
        questionnaires = paginator.page(1)
    except EmptyPage:
        questionnaires = paginator.page(paginator.num_pages)

    context = {
        "title": "Questionnaire Editor",
        "namespace": user_obj["service_namespace"],
        "question_types": QuestionType.objects.all,
        "questionnaires": questionnaires,
        "templates": templates,
    }

    return render(request, "vendor/qa/qa_editor.html", context)


def get_summary_statistics(questionnaire_id=None):
    # Statistics
    # stats for current month instance of questionnaire
    # todo count end_user_questionnaire for questionnaire
    # todo count number for this month of validity
    current_month_start = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    curr_end_user_questionnaires = EndUserQuestionnaire.objects.filter(questionnaire_id=questionnaire_id,
                                                                       regist_dt__gte=current_month_start)
    # Total Views
    view_curr = curr_end_user_questionnaires.count()
    # Total respondent
    curr_end_user_questionnaires_ids = curr_end_user_questionnaires.values_list('id', flat=True).distinct()
    curr_responses = Response.objects.filter(
        end_user_questionnaire_id__in=curr_end_user_questionnaires_ids).values_list('id', flat=True).distinct()
    curr_total_respondent = curr_responses.count()
    # New Respondents
    curr_new_end_user_questionnaires = EndUserQuestionnaire.objects.filter(questionnaire_id=questionnaire_id,
                                                                           regist_dt__lt=current_month_start)
    curr_new_end_user_questionnaires_ids = curr_new_end_user_questionnaires.values_list('id', flat=True).distinct()
    curr_new_respondent = Response.objects.filter(
        end_user_questionnaire_id__in=curr_new_end_user_questionnaires_ids).values_list('id', flat=True).distinct()
    curr_new_respondents = curr_new_respondent.count()
    # Recurring Respondents
    curr_recurring_respondents = curr_total_respondent - curr_new_respondents

    # stats for previous month instance of questionnaire
    # todo count number for last month of validity
    previous_month_end = current_month_start - datetime.timedelta(days=1)
    previous_month_start = previous_month_end.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    prev_end_user_questionnaires = EndUserQuestionnaire.objects.filter(questionnaire_id=questionnaire_id,
                                                                       regist_dt__gte=previous_month_start,
                                                                       regist_dt__lt=current_month_start)
    # Total Views
    view_prev = prev_end_user_questionnaires.count()
    # Total respondent
    prev_end_user_questionnaires_ids = prev_end_user_questionnaires.values_list('id', flat=True).distinct()
    prev_responses = Response.objects.filter(
        end_user_questionnaire_id__in=prev_end_user_questionnaires_ids).values_list('id', flat=True).distinct()
    prev_total_respondent = prev_responses.count()
    # New Respondents
    prev_new_end_user_questionnaires = EndUserQuestionnaire.objects.filter(questionnaire_id=questionnaire_id,
                                                                           regist_dt__lt=current_month_start)
    prev_new_end_user_questionnaires_ids = prev_new_end_user_questionnaires.values_list('id', flat=True).distinct()
    prev_new_respondent = Response.objects.filter(
        end_user_questionnaire_id__in=prev_new_end_user_questionnaires_ids).values_list('id', flat=True).distinct()
    prev_new_respondents = prev_new_respondent.count()
    # Recurring Respondents
    prev_recurring_respondents = prev_total_respondent - prev_new_respondents

    # Total Views
    view_stat = {
        "prev": view_prev,
        "curr": view_curr,
        "change": get_diff_percentage(view_prev, view_curr)
    }

    # Total Respondents
    total_respondent_stat = {
        "prev": prev_total_respondent,
        "curr": curr_total_respondent,
        "change": get_diff_percentage(prev_total_respondent, curr_total_respondent),
    }

    # Recurring Respondents
    recurring_respondents_stat = {
        "prev": prev_recurring_respondents,
        "curr": curr_recurring_respondents,
        "change": get_diff_percentage(prev_recurring_respondents, curr_recurring_respondents),
    }

    # New Respondents
    new_respondents_stat = {
        "prev": prev_new_respondents,
        "curr": curr_new_respondents,
        "change": get_diff_percentage(prev_new_respondents, curr_new_respondents),
    }

    return {"view_stat": view_stat, "total_respondent_stat": total_respondent_stat, "recurring_respondents_stat": recurring_respondents_stat, "new_respondents_stat": new_respondents_stat}


def get_diff_percentage(prev, curr):
    # calculate difference between percentages of recurring_respondents
    change = 0

    if prev > curr:
        diff = prev - curr
        if prev == curr:
            change = 0
        elif prev == 0:
            change = 100
        else:
            change = round(diff / prev * 100)

    elif prev < curr:
        diff = curr - prev
        if prev == curr:
            change = 0
        elif prev == 0:
            change = 100
        else:
            change = round(diff / prev * 100)

    return change


@login_required(login_url='/qa/')
def summary(request, questionnaire_id=None):
    """ QA Editor Summary """
    user_obj = get_login_user_objects(request)
    completed_questionnaire_ids = [questionnaire.id for questionnaire in Questionnaire.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=False) if (questionnaire.status() == 'Completed')]
    questionnaires = Questionnaire.objects.filter(id__in=completed_questionnaire_ids)

    page = request.GET.get('page', 1)
    paginator = Paginator(questionnaires, 20)
    try:
        questionnaires = paginator.page(page)
    except PageNotAnInteger:
        questionnaires = paginator.page(1)
    except EmptyPage:
        questionnaires = paginator.page(paginator.num_pages)

    if not questionnaire_id:
        context = {
            "title": "Questionnaire Summary",
            "namespace": user_obj["service_namespace"],
            "questionnaires": questionnaires,
        }

        return render(request, "vendor/qa/qa_summary.html", context)

    elif questionnaire_id:
        selected_questionnaire = Questionnaire.objects.filter(id=questionnaire_id, vendor_branch=user_obj["vendor_branch"], is_delete=False).first()

        # get a list of all users who answered this questionnaire
        end_user_questionnaires = EndUserQuestionnaire.objects.filter(questionnaire_id=questionnaire_id)

        # cumulative stats for all versions of a specific questionnaire
        total_respondents = Response.objects.filter(end_user_questionnaire__in=end_user_questionnaires).order_by('end_user_id').values('end_user_id').distinct().count()
        total_views = end_user_questionnaires.count()
        # users for who this questionnaire was their first point of contact
        participant_ids = end_user_questionnaires.values('end_user_id').distinct()
        participants = EndUser.objects.filter(id__in=participant_ids).all()

        # new participants is end_users whose first questionnaire was this one
        """
            for each user in respondents
                find oldest end_user_questionnaire
                    if questionnaire is this questionnaire then user is new participant 
        """
        new_participants = []
        for participant in participants.iterator():
            oldest_questionnaire = EndUserQuestionnaire.objects.filter(end_user=participant).order_by('regist_dt').first()
            if oldest_questionnaire.id == questionnaire_id:
                new_participants.append(participant)

        summary_statistics = get_summary_statistics()

        context = {
            "title": "Questionnaire Summary",
            "namespace": user_obj["service_namespace"],
            "selected_questionnaire": selected_questionnaire,
            "questionnaires": questionnaires,
            "total_respondents": total_respondents,
            "total_views": total_views,
            "view_stat": summary_statistics['view_stat'],
            "total_respondent_stat": summary_statistics['total_respondent_stat'],
            "recurring_respondents_stat": summary_statistics['recurring_respondents_stat'],
            "new_respondents_stat": summary_statistics['new_respondents_stat'],
            "questionnaires": questionnaires,
            "participants": participants,
            "new_participants": len(new_participants),
        }

        return render(request, "vendor/qa/qa_summary.html", context)


@login_required(login_url='/qa/')
def add(request, template_id=None):
    """ QA add questionnaire """
    user_obj = get_login_user_objects(request)

    questionnaire = Questionnaire()
    questionnaire.vendor_branch = user_obj['vendor_branch']
    questionnaire.save()

    print('have template_id', template_id)
    if template_id:

        template = QuestionnaireTemplate.objects.filter(id=template_id).first()
        template_questions = QuestionnaireTemplateQuestion.objects.filter(questionnaire_template=template).all()
        for index, template_question in enumerate(template_questions):
            print('enumerating template questions', template_question.question.question_text)
            new_question = Question(vendor_branch=user_obj['vendor_branch'], type=template_question.question.type,
                                    question_text=template_question.question.question_text, question_options=template_question.question.question_options)
            new_question.save()
            new_qq = QuestionnaireQuestion(questionnaire=questionnaire, question=new_question, display_order=template_question.display_order)
            new_qq.save()

    redirect_url = "/" + user_obj["service_url"] + "/questionnaire/edit/" + str(questionnaire.id) + "/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def edit(request, questionnaire_id=None):
    """ QA edit questionnaire """
    user_obj = get_login_user_objects(request)

    active_questionnaire_ids = [questionnaire.id for questionnaire in Questionnaire.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=False).all() if (questionnaire.status() != 'Completed')]
    questionnaires = Questionnaire.objects.filter(id__in=active_questionnaire_ids)

    templates = QuestionnaireTemplate.objects.all()
    vendor_token = user_obj["vendor_branch"].vendor.contactchat_access_url_part

    page = request.GET.get('page', 1)
    paginator = Paginator(questionnaires, 20)
    try:
        questionnaires = paginator.page(page)
    except PageNotAnInteger:
        questionnaires = paginator.page(1)
    except EmptyPage:
        questionnaires = paginator.page(paginator.num_pages)

    selected_questionnaire = Questionnaire.objects.filter(id=questionnaire_id, vendor_branch=user_obj["vendor_branch"], is_delete=False).first()
    questionnaire_questions = QuestionnaireQuestion.objects.filter(questionnaire=selected_questionnaire).order_by('display_order').all()

    questionnaire_url = "{0}v2/form/{1}/{2}/".format(settings.CONTACTCHAT_BASE_URL, vendor_token, questionnaire_id)
    widget_embed_code = '''
               <div id="contactchat-widget"></div>
                <script  src="{0}widget/loader/?docked=true"></script> 
            '''.format(questionnaire_url)
    try:
        if request.POST:
            form = QuestionnaireForm(request.POST, instance=selected_questionnaire)
            if form.is_valid():
                selected_questionnaire = form.save(commit=False)
                selected_questionnaire.update_dt = timezone.now()
                selected_questionnaire.save()

                # save questionnaire questions
                parse_questionnaire_questions(request, questionnaire_id)
        else:
            form = QuestionnaireForm(instance=selected_questionnaire)
    except LookupError as e:
        print('Error occurred saving questionnaire questions ', e)
        form = QuestionnaireForm(instance=selected_questionnaire)

    context = {
        "title": "Questionnaire Editor",
        "namespace": user_obj["service_namespace"],
        "selected_questionnaire": selected_questionnaire,
        "questionnaire_questions": questionnaire_questions,
        "question_types": QuestionType.objects.all,
        "questionnaires": questionnaires,
        "templates": templates,
        "form": form,
        "questionnaire_url": questionnaire_url,
        "widget_embed_code": widget_embed_code,
    }

    return render(request, "vendor/qa/qa_editor.html", context)


@login_required(login_url='/qa/')
def delete(request, questionnaire_id=None):
    user_obj = get_login_user_objects(request)

    questionnaire = Questionnaire.objects.filter(id=questionnaire_id, vendor_branch=user_obj["vendor_branch"], is_delete=False).first()

    if questionnaire:
        questionnaire.is_delete = True
        questionnaire.save()

    redirect_url = "/" + user_obj["service_url"] + "/questionnaire/list/"
    return redirect(redirect_url)

# Helper functions


@login_required(login_url='/qa/')
def get_respondent_report(request, questionnaire_id=None):
    user_obj = get_login_user_objects(request)
    questionnaire = Questionnaire.objects.filter(id=questionnaire_id, vendor_branch=user_obj["vendor_branch"],is_delete=False).first()
    user_questionnaires = EndUserQuestionnaire.objects.filter(questionnaire=questionnaire).all()

    today = timezone.now()
    params = {
        'today': today,
        'questionnaire': questionnaire,
        'user_questionnaires': user_questionnaires,
        'user': user_obj['vendor_user'],
    }
    return FileRender.render_pdf('vendor/qa/qa_respondent_report.html', params)


@login_required(login_url='/qa/')
def get_respondent_responses(request, questionnaire_id=None, end_user_id=None):
    user_obj = get_login_user_objects(request)
    questionnaire = Questionnaire.objects.filter(id=questionnaire_id, vendor_branch=user_obj["vendor_branch"],is_delete=False).first()

    # users can take a questionnaire multiple times so having more than one entry is always possible
    user_questionnaires = EndUserQuestionnaire.objects.filter(questionnaire=questionnaire, end_user_id=end_user_id).all()
    for user_questionnaire in user_questionnaires:
        responses = Response.objects.filter(end_user_questionnaire=user_questionnaire, end_user_id=end_user_id).all()
        user_questionnaire.responses = responses

    today = timezone.now()
    params = {
        'today': today,
        'questionnaire': questionnaire,
        'user_questionnaires': user_questionnaires,
        'user': user_obj['vendor_user'],
    }
    return FileRender.render_pdf('vendor/qa/qa_respondent_responses.html', params)


@login_required(login_url='/qa/')
def get_question_template(request):
    """
    Returns a question template formatted with the provided query parameters
    or returns a 404
    :param request: expected parameters include question_id, display_id, type_id
    :return: JsonResponse containing html template
    """
    if request.GET:
        question_type = request.GET.get('type_id', None)

        if question_type == '1':
            html = render_to_string('forms/question_text.html', get_question_template_context(request), request)
            return JsonResponse({'template': html})
        elif question_type == '2':
            html = render_to_string('forms/question_option.html', get_question_template_context(request), request)
            return JsonResponse({'template': html})
        elif question_type == '3':
            html = render_to_string('forms/question_registration.html', get_question_template_context(request), request)
            return JsonResponse({'template': html})
        elif question_type == '4':
            html = render_to_string('forms/question_multi_option.html', get_question_template_context(request), request)
            return JsonResponse({'template': html})

    return HttpResponseNotFound()


@login_required(login_url='/qa/')
def get_question_template_context(request):
    """ QA creates context to feed to question template """
    user_obj = get_login_user_objects(request)

    if request.GET:
        question_id = request.GET.get('question_id', None)
        display_id = request.GET.get('display_id', None)

        question = None
        if question_id:
            question = QuestionnaireQuestion.objects.filter(id=question_id).first()

    if not question:
        question = {
            "id": question_id,
            "display_order": display_id,
            "question": {
                "id": question_id,
                "question_text": "",
                "question_options": "",
            }
        }

    context = {
        "question": question,
        "question_types": QuestionType.objects.all,
    }

    return context


@login_required(login_url='/qa/')
def get_qr_code(request, questionnaire_id):
    user_obj = get_login_user_objects(request)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data("{0}/v2/form/{1}/".format(settings.CONTACTCHAT_BASE_URL, user_obj["vendor_branch"].vendor.contactchat_access_url_part))
    qr.make(fit=True)

    img = qr.make_image()
    return img


"""
Questionnaire Question edit helper functions
"""

@login_required(login_url='/qa/')
def delete_question(request, questionnaire_id=None, question_id=None):
    user_obj = get_login_user_objects(request)
    if question_id and questionnaire_id:
        # delete the questionnaire question
        questionnaire_question = QuestionnaireQuestion.objects.filter(id=question_id, questionnaire_id=questionnaire_id).first()
        question = Question.objects.filter(id=questionnaire_question.question_id).first()
        questionnaire_question.delete()

        # if no questionnaire question remain related to a question then delete that too
        remaining_questions = QuestionnaireQuestion.objects.filter(question_id=question.id).count()
        if remaining_questions <= 0:
            question.delete()
    return


@login_required(login_url='/qa/')
def parse_questionnaire_questions(request, questionnaire_id):
    """ Parses questionnaire questions from POST data for a specified questionnaire id."""
    post_data = request.POST
    # detect how many questions we need to parse
    exp_question_id = re.compile('(question_(-)?\d+_id)')

    found_id_list = []
    for index, key in enumerate(post_data):
        if exp_question_id.match(key):
            question_id = int(extract_id(key))
            found_id_list.append(question_id)
            question = save_questionnaire_question(request, questionnaire_id, question_id)
            found_id_list.append(question.id)

    # delete any questionnare questions that are no longer associated with this questionnaire
    existing_questions = QuestionnaireQuestion.objects.filter(questionnaire_id=questionnaire_id, id__in=found_id_list).values_list('id', flat=True)
    questionnaire_questions_to_remove = QuestionnaireQuestion.objects.filter(questionnaire_id=questionnaire_id)
    questionnaire_questions_to_remove= questionnaire_questions_to_remove.exclude(id__in=existing_questions)
    for item in questionnaire_questions_to_remove:
        delete_question(request, questionnaire_id, item.id)

    return


def extract_id(key):
    """ Dissects a string to find the singular numeric id contained within.
    This assumes the numeric id is always prefixed by one word followed by an underscore."""
    key_parts = key.split('_')
    return key_parts[1]


@login_required(login_url='/qa/')
def save_questionnaire_question(request, questionnaire_id, question_id):
    """ save a questionnaire question for the specific questionnaire """
    # if id is a negative number OR the id doesn't exist then create a new question else override existing question
    existing_question = QuestionnaireQuestion.objects.filter(id=question_id).first()
    if not existing_question:
        existing_question = QuestionnaireQuestion()

    post_data = request.POST
    prefix_match = f'question_{question_id}'

    # questionnaire question properties
    existing_question.questionnaire_id = questionnaire_id
    question_display_order = post_data[f'{prefix_match}_display_order']
    existing_question.display_order = int(question_display_order)

    # save template question properties
    template_question = save_question(request, question_id)

    # save both questionnaire question and template question in response to possible changes
    existing_question.question = template_question
    existing_question.save()

    return existing_question


@login_required(login_url='/qa/')
def save_question(request, questionnaire_question_id):
    """ Save an existing question or create a new one and then return it """
    user_obj = get_login_user_objects(request)
    post_data = request.POST
    prefix_match = f'question_{questionnaire_question_id}'

    # get the question if it exists or create a new one
    template_question_id = int(post_data[f'{prefix_match}_template_id'])
    template_question = Question.objects.filter(id=template_question_id).first()
    if not template_question:
        print('template question not found! making new one!')
        template_question = Question()
        template_question.vendor_branch = user_obj['vendor_branch']

    # get question type if it exists, else raise an error
    question_type = QuestionType.objects.filter(name=post_data[f'{prefix_match}_type']).first()
    if not question_type:
        print('question type not found!')
        raise LookupError('tried to save unknown question type ', post_data[f'{prefix_match}_type'])

    # save template question properties
    template_question.type = question_type
    template_question.question_text = post_data[f'{prefix_match}_question_text']
    if question_type.name == 'option' or question_type.name == 'multioption':
        opt_list = post_data.getlist(f'{prefix_match}_options', None)
        if opt_list:
            template_question.question_options = json.dumps(opt_list)
    else:
        opts = post_data.get(f'{prefix_match}_options', None)
        if opts:
            template_question.question_options = json.dumps(opts)
    template_question.save()

    return template_question
