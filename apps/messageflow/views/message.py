import traceback

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from apps.messageflow.views import message as message_url
from django.http import JsonResponse

# import models
from django.template.loader import render_to_string
from apps.messageflow.models.bot import Scenario
from apps.messageflow.models.message import MessageBlock

# import forms
from apps.messageflow.models.end_user import EndUser
from apps.messageflow.forms.message import TargetedMessageFilterForm
from apps.messageflow.forms.scenario import ScenarioForm, MessageFormSet

# import usecase
from apps.messageflow.usecases.user import AuthorizeUser
from apps.messageflow.usecases.template import RetrieveTemplates, RetrieveMessageTemplate
from apps.messageflow.usecases.message import filter_targeted_message_recipients, send_targeted_message


@login_required()
def targeted(request, base_template='blank', template=None):
    """
        Sends message directly to a selected group of users
    """

    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'scenario/scenario_list', base_template, template).execute()

    print("owner id: ", service_info["owner_id"])

    scenario = Scenario.objects.filter(owner_id=-1).first()

    message_block = MessageBlock.objects.filter(scenario=scenario).first()
    if not message_block:
        message_block = MessageBlock(scenario=scenario)
        message_block.save()

    message_formset = MessageFormSet(None, instance=message_block)

    if request.POST:
        recipients = EndUser.objects.filter(owner_id=service_info["owner_id"], is_delete=0)
        recipients = filter_targeted_message_recipients(request, recipients)

        message_formset = MessageFormSet(request.POST, instance=message_block)
        if message_formset.is_valid():
            message_formset.save(commit=False)

            send_targeted_message(request, message_formset, recipients)

            view_name = '{0}:messageflow:targeted_message'.format(service_info['app_id'])
            return redirect(view_name, base_template=base_template)

    end_users = EndUser.objects.filter(owner_id=service_info["owner_id"], is_delete=0)
    user_filter = TargetedMessageFilterForm(request.GET, queryset=end_users, request=request)

    context = {
        "title": "Direct Message",
        'namespace': service_info['namespace'],
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        },
        'message_forms': message_formset,
        'target_form': user_filter.form
    }

    return render(request, "messageflow/targeted_message.html", context)


def targeted_count(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    recipients = EndUser.objects.filter(owner_id=service_info["owner_id"], is_delete=0)
    recipients = filter_targeted_message_recipients(request, recipients)

    return JsonResponse({"status": "success", "recipientCount": recipients.count()})
