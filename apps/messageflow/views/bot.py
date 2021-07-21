from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# import models
from apps.messageflow.models.bot import Bot, BotScenario, Scenario

# import forms
from apps.messageflow.forms.bot import BotForm, ScenarioFormSet

# import usecase
from apps.messageflow.usecases.user import AuthorizeUser
from apps.messageflow.usecases.template import RetrieveTemplates


@login_required()
def list(request, base_template=None, template=None):
    print('debugging list', base_template, template)
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'bot/bot_list', base_template, template).execute()

    bot_list = []

    bots = Bot.objects.filter(owner_id=service_info['owner_id'], app_id=service_info['app_id']).all().values()

    for bot in bots:
        scenarios = BotScenario.objects.filter(bot=bot['id']).all().values()
        bot.update({'scenarios': []})
        for scenario in scenarios:
            scenario_name = Scenario.objects.filter(id=scenario['scenario_id']).first().name
            scenario.update({'name': scenario_name})
            bot['scenarios'].append(scenario)
        bot_list.append(bot)

    print('base template', template_info['base_template'])
    context = {
        'bot_list': bot_list,
        'namespace': service_info['namespace'],
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        }
    }

    return render(request, template_info['template'], context)


@login_required()
def edit(request, bot_id=None, base_template=None, template=None):
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'bot/bot_edit', base_template, template).execute()

    if bot_id:
        bot = get_object_or_404(Bot, pk=bot_id)
        if bot.owner_id != service_info['owner_id'] or bot.app_id != service_info['app_id']:
            return HttpResponseForbidden()
    else:
        bot = Bot(owner_id=service_info['owner_id'], app_id=service_info['app_id'])

    bot_form = BotForm(request.POST or None, instance=bot)
    scenario_form = ScenarioFormSet(request.POST or None, instance=bot)
    if request.POST and bot_form.is_valid() and scenario_form.is_valid():
        bot = bot_form.save()
        scenario_form.save()

        # take care of deleting items
        for scenario_obj in scenario_form.deleted_objects:
            scenario_obj.delete()

        view_name = '{0}:messageflow:bot_list'.format(service_info['app_id'])
        return redirect(view_name, base_template=base_template)

    context = {
        'bot_form': bot_form,
        'scenario_form': scenario_form,
        'namespace': service_info['namespace'],
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        }
    }

    return render(request, template_info['template'], context)


@login_required()
def delete(request, bot_id=None, base_template=None, template=None):
    service_info = AuthorizeUser(request.user, request.path).execute()

    bot = Bot.objects.filter(id=bot_id, owner_id=service_info['owner_id'], app_id=service_info['app_id']).first()
    if bot:
        bot.delete()

    view_name = '{0}:messageflow:bot_list'.format(service_info['app_id'])
    return redirect(view_name, base_template=base_template)


@login_required()
def toggle(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    bot_id = request.GET.get('bot_id', None)

    selected_bot = Bot.objects.filter(id=bot_id).first()

    selected_bot.is_active = not selected_bot.is_active

    is_active = selected_bot.is_active

    selected_bot.save()

    # return JSON response here...see chat quest questionnaire
    if True:
        return JsonResponse({"status": "success", "is_active": is_active})
    else:
        return HttpResponseNotFound()
