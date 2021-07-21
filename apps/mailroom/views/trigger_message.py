from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# import models
from apps.mailroom.models.trigger_type import MaTriggerType
from apps.mailroom.models.trigger import MaTrigger
from apps.mailroom.models.message import Message, MessageTemplate

# import usecase
from apps.mailroom.usecases.user import AuthorizeUser
from apps.mailroom.usecases.template import RetrieveTemplates

# import forms
from apps.mailroom.forms.message import MaTriggerForm
from apps.mailroom.forms.message import MaMessageForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.nchat.views.decorators import paid_up_account_required
from pprint import pprint

# @paid_up_account_required(payment_url='/nchat/payment/edit/')
@login_required()
def list(request, base_template='blank', template=None):
    print("This is the request for list: ", request.user)
    print("This is request.path: ", request.path)
    """ mailroom active triggers list """
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'trigger_list', base_template, template).execute()

    messages = Message.objects.filter(owner_id=service_info["owner_id"], app_id=service_info["app_id"]).values_list('id', flat=True)
    active_triggers = MaTrigger.objects.filter(message_id__in=messages).all().order_by("-id")

    page = request.GET.get('page', 1)
    paginator = Paginator(active_triggers, 10)
    try:
        active_triggers = paginator.page(page)
    except PageNotAnInteger:
        active_triggers = paginator.page(1)
    except EmptyPage:
        active_triggers = paginator.page(paginator.num_pages)

    context = {
        "title": "Active Triggers",
        "namespace": service_info["namespace"],
        "list": active_triggers,
        "list_type": "active_triggers",
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        }
    }

    return render(request, template_info['template'], context)


# @paid_up_account_required(payment_url='/nchat/payment/edit/')
@login_required()
def add(request):
    """ mailroom add trigger message """
    service_info = AuthorizeUser(request.user, request.path).execute()
    # create new message and trigger instances

    if request.POST['message_type'] == "trigger_message":
        if request.POST['template_id']:
            new_message = Message(owner_id=service_info["owner_id"], app_id=service_info["app_id"])
            new_message.save()
        else:
            message_template = MessageTemplate.objects.filter(id=request.POST['template_id']).first()
            new_message = Message(subject=message_template.message.subject, message_text=message_template.message.message_text, owner_id=service_info["owner_id"], app_id=service_info["app_id"])
            new_message.save()
        new_trigger = MaTrigger(message=new_message, trigger_type_id=1)
        new_trigger.save()
        redirect_url = "/" + service_info["namespace"] + "/mailroom/trigger/edit/" + str(new_trigger.id) + "/"
    elif request.POST['message_type'] == "direct_message":
        redirect_url = "/" + service_info["namespace"] + "/mailroom/direct/edit/1/"
    else:
        print("error unknown message type!!!")
        redirect_url = "/" + service_info["namespace"] + "/mailroom/direct/edit/1/"

    return redirect(redirect_url)


# @paid_up_account_required(payment_url='/nchat/payment/edit/')
@login_required()
def edit(request, trigger_id=None, base_template='blank', template=None):
    """ mailroom edit """

    # todo find out if there is a better alternative to the following
    from messaging_platform.settings.base import FROALA_EDITOR_OPTIONS
    FROALA_EDITOR_OPTIONS['language'] = str(_('en'))

    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'trigger', base_template, template).execute()

    messages = Message.objects.filter(owner_id=service_info["owner_id"],
                                      app_id=service_info["app_id"]).values_list('id',
                                      flat=True)

    triggers = MaTrigger.objects.filter(message_id__in=messages).all()

    page = request.GET.get('page', 1)
    paginator = Paginator(triggers, 5)
    try:
        triggers = paginator.page(page)
    except PageNotAnInteger:
        triggers = paginator.page(1)
    except EmptyPage:
        triggers = paginator.page(paginator.num_pages)

    trigger_types = MaTriggerType.objects.filter().all()
    # todo we are pronbably better off asigning the vendor branch to the trigger instead of the message
    selected_trigger = MaTrigger.objects.filter(id=trigger_id).first()
    # todo fix this if else after debugging
    if selected_trigger:
        selected_message = selected_trigger.message
    else:
        selected_message = None

    if request.POST:
        trigger_form = MaTriggerForm(request.POST, instance=selected_trigger)
        message_form = MaMessageForm(request.POST, instance=selected_message)
        if trigger_form.is_valid() and message_form.is_valid():
            selected_trigger = trigger_form.save()
            selected_message = message_form.save()
    else:
        trigger_form = MaTriggerForm(instance=selected_trigger)
        message_form = MaMessageForm(instance=selected_message)

    messages = Message.objects.filter(owner_id=service_info["owner_id"], app_id=service_info["app_id"]).values_list('id',
                                                                                                            flat=True)
    active_triggers = MaTrigger.objects.filter(message_id__in=messages).all().order_by("-id")

    page = request.GET.get('page', 1)
    paginator = Paginator(active_triggers, 10)
    try:
        active_triggers = paginator.page(page)
    except PageNotAnInteger:
        active_triggers = paginator.page(1)
    except EmptyPage:
        active_triggers = paginator.page(paginator.num_pages)
    context = {
        "title": "Mail Room",
        "namespace": service_info["namespace"],
        "trigger_types": trigger_types,
        "trigger_form": trigger_form,
        "message_form": message_form,
        "triggers": triggers,
        "selected_trigger": selected_trigger,
        "list": active_triggers,
        "list_type": "active_triggers",
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        },
        "mail_type": "trigger"
    }

    return render(request, template_info['template'], context)


# @paid_up_account_required(payment_url='/nchat/payment/edit/')
@login_required()
def delete(request):
    """ Delete existing mailroom trigger message """
    service_info = AuthorizeUser(request.user, request.path).execute()

    delete_list = request.POST.getlist("item-selection")

    selected_trigger = MaTrigger.objects.filter(id__in=delete_list)

    for trigger in selected_trigger:
        trigger.message.delete()

    redirect_url = "/" + service_info["namespace"] + "/mailroom/trigger/list"
    return redirect(redirect_url)


# @paid_up_account_required(payment_url='/nchat/payment/edit/')
@login_required()
def toggle(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    trigger_id = request.GET.get('trigger_id', None)

    """ this seems insecure """''
    messages = Message.objects.filter(owner_id=service_info["owner_id"], app_id=service_info["app_id"]).values_list('id', flat=True)
    selected_trigger = MaTrigger.objects.filter(id=trigger_id, message_id__in=messages).first()

    selected_trigger.is_active = not selected_trigger.is_active

    is_active = selected_trigger.is_active

    selected_trigger.save()

    # return JSON response here...see chat quest questionnaire
    if True:
        return JsonResponse({"status": "success", "is_active": is_active})
    else:
        return HttpResponseNotFound()
