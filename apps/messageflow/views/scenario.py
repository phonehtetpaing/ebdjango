import traceback

from django.db import transaction
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required

# import models
from django.template.loader import render_to_string

from apps.messageflow.models.bot import Scenario
from apps.messageflow.models.message import MessageType, Message, MessageBlock

# import forms
from apps.messageflow.forms.scenario import ScenarioForm, MessageFormSet

# import usecase
from apps.messageflow.usecases.user import AuthorizeUser
from apps.messageflow.usecases.template import RetrieveTemplates, RetrieveMessageTemplate
from apps.nchat.models.file import File


@login_required()
def list(request, base_template=None, template=None):
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'scenario/scenario_list', base_template, template).execute()

    scenarios = Scenario.objects.filter(owner_id=service_info['owner_id'], app_id=service_info['app_id']).all()

    context = {
        'object_list': scenarios,
        'namespace': service_info['namespace'],
        'base_template': template_info['base_template'],
        'template': template_info['template'],
        'args': {
            'base_template': base_template,
            'template': template,
        }
    }

    return render(request, template_info['template'], context)


@login_required()
def add(request, base_template=None, template=None):
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'scenario/scenario_edit', base_template, template,).execute()
    scenario = Scenario(name='new', owner_id=service_info['owner_id'], app_id=service_info['app_id'])
    scenario.save()
    message_block = MessageBlock(scenario=scenario, display_order=1).save()

    view_name = '{0}:messageflow:scenario_edit'.format(service_info['app_id'])
    return redirect(view_name, base_template=base_template, scenario_id=scenario.id)


@login_required()
def edit(request, base_template=None, template=None, scenario_id=None):
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'scenario/scenario_edit', base_template, template,).execute()

    scenario = get_object_or_404(Scenario, pk=scenario_id)
    if scenario.owner_id != service_info['owner_id'] or scenario.app_id != service_info['app_id']:
        return HttpResponseForbidden()

    message_blocks = MessageBlock.objects.filter(scenario=scenario)
    message_block = message_blocks.first()
    if request.POST:
        block_id = request.POST.get('block_id', None)
        if block_id:
            message_block = get_object_or_404(MessageBlock, pk=block_id)
            message_formset = MessageFormSet(request.POST, instance=message_block)

        else:
            message_formset = MessageFormSet(None, instance=message_block)
    else:
        message_formset = MessageFormSet(None, instance=message_block)

    scenario_form = ScenarioForm(request.POST or None, instance=scenario)

    if request.POST and scenario_form.is_valid() and message_formset.is_valid():
        print('==== PASSED VALIDATION ====')
        print(request.POST)
        # make sure that ALL forms are valid before saving anything, else rollback any changes that were made
        with transaction.atomic():
            scenario.save()

            message_formset.save(commit=False)
            for message_form in message_formset.forms:
                message_form.save(commit=False)
                message_form.instance.owner_id = service_info['owner_id']
                message_form.instance.app_id = service_info['app_id']
                message_form.save()
            # take care of deleting items
            for message_obj in message_formset.deleted_objects:
                message_obj.delete()

            view_name = '{0}:messageflow:scenario_edit'.format(service_info['app_id'])
            return redirect(view_name, base_template=base_template, scenario_id=scenario.id)
    elif not scenario_form.is_valid() or not message_formset.is_valid():
        print('formset errors: ', message_formset.errors)
    elif scenario_form.is_valid() and message_formset.is_valid():
        print('valid but no post')
    else:
        print('not post')

    context = {
        'form': scenario_form,
        'message_forms': message_formset,
        'message_blocks': message_blocks,
        'namespace': service_info['namespace'],
        'base_template': template_info['base_template'],
        'template': template_info['template'],
        'args': {
            'base_template': base_template,
            'template': template,
        }
    }

    return render(request, template_info['template'], context)


@login_required()
def delete(request, scenario_id=None, base_template=None, template=None):
    service_info = AuthorizeUser(request.user, request.path).execute()

    scenario = get_object_or_404(Scenario, pk=scenario_id)
    if scenario.owner_id != service_info['owner_id'] or scenario.app_id != service_info['app_id']:
        return HttpResponseForbidden()

    scenario.delete()

    view_name = '{0}:messageflow:bot_list'.format(service_info['app_id'])
    return redirect(view_name, base_template=base_template, template=template)


@login_required()
def get_message_template(request):
    """
    Returns a message template formatted with the provided query parameters
    or returns a 404
    :param request: expected parameters include message_set_id, block_id, type, display_order
    :return: JsonResponse containing html template
    """

    if request.GET:
        service_info = AuthorizeUser(request.user, request.path).execute()
        message_set_id = request.GET.get('message_set_id', None)
        block_id = request.GET.get('block_id', None)
        message_type = request.GET.get('type', None)
        display_order = request.GET.get('display_order', None)

        try:
            message_template = RetrieveMessageTemplate(
                service_info,
                message_set_id,
                block_id,
                message_type,
                display_order,
            ).execute()
            return JsonResponse({'template': message_template})
        except Exception as e:
            print(e)
            print(traceback.format_exc())

    return HttpResponseNotFound()


@login_required()
def add_message_block(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    if request.GET:
        scenario_id = request.GET.get('scenario_id', None)
        display_order = request.GET.get('display_order', None)

        # ensure the scenario exists and belongs to the requesting user
        scenario = get_object_or_404(Scenario, pk=scenario_id)
        if scenario.owner_id != service_info['owner_id'] or scenario.app_id != service_info['app_id']:
            return HttpResponseForbidden()

        block = MessageBlock(name='', scenario=scenario, display_order=display_order).save()
        # return the block template
        context = {
            "block": block,
        }
        block_template = render_to_string('messageflow/messages/message_block.html', context)
        return JsonResponse({'template': block_template})

    return HttpResponseNotFound()


@login_required()
def update_message_block_display_order(request):
    service_info = AuthorizeUser(request.user, request.path).execute()

    if request.GET:
        block_ids = request.GET.getlist('block_ids[]', None)
        # ensure the scenario exists and belongs to the requesting user
        blocks = get_list_or_404(MessageBlock, id__in=block_ids)
        for index, block in enumerate(blocks):
            block.display_order = index
            block.save()

        return HttpResponse(200)

    return HttpResponseNotFound()


@login_required()
def get_message_block_message_set(request):
    service_info = AuthorizeUser(request.user, request.path).execute()

    if request.GET:
        block_id = request.GET.get('block_id', None)
        # ensure the scenario exists and belongs to the requesting user
        block = get_object_or_404(MessageBlock, pk=block_id)
        if block.scenario.owner_id != service_info['owner_id'] or block.scenario.app_id != service_info['app_id']:
            return HttpResponseForbidden()
        message_blocks = MessageBlock.objects.filter(scenario=block.scenario).all()
        files = File.objects.filter(app_id=service_info['app_id'], owner_id=service_info['owner_id']).all()
        message_formset = MessageFormSet(instance=block)
        # return the template
        context = {
            'block_id': block_id,
            'message_forms': message_formset,
            'message_blocks': message_blocks,
            'files': files,
        }
        block_template = render_to_string('messageflow/messages/block_management.html', context)
        return JsonResponse({'template': block_template})

    return HttpResponseNotFound()


@login_required()
def get_message_option_template(request):
    """
    Get an empty template for an option message option.
    The template will be bound to the specified message set and contain data to link to a list of existing
    message blocks.

    :param request object containing the request user and GET data:
    :param request.GET object containing the following keys;
        block_id of the currently selected message block,
        set_id of the current message formset,
        option_id for the new option message option:
    :return JSON response containing an html template:
    """
    service_info = AuthorizeUser(request.user, request.path).execute()

    if request.GET:
        block_id = request.GET.get('block_id', None)
        set_id = request.GET.get('set_id', None)
        option_id = request.GET.get('option_id', None)

        # ensure all parameters are provided
        if not block_id or not set_id or not option_id:
            return HttpResponseNotFound()

        # ensure the scenario exists and belongs to the requesting user
        block = get_object_or_404(MessageBlock, pk=block_id)
        if block.scenario.owner_id != service_info['owner_id'] or block.scenario.app_id != service_info['app_id']:
            return HttpResponseForbidden()

        message_blocks = MessageBlock.objects.filter(scenario=block.scenario).all()
        context = {
            'block_id': block_id,
            'message_counter': set_id,
            'option_id': option_id,
            'option': {'title': None, 'payload': None},
            'message_blocks': message_blocks,
        }
        block_template = render_to_string('messageflow/messages/option_message_option.html', context)
        return JsonResponse({'template': block_template})

    return HttpResponseNotFound()