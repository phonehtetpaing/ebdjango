from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
import json

# import models
from apps.mailroom.models.trigger import MaTrigger
from apps.mailroom.models.message import Message

# import forms
from apps.mailroom.forms.message import MaDirectMessageForm

# import usecase
from apps.mailroom.usecases.user import AuthorizeUser
from apps.mailroom.usecases.template import RetrieveTemplates
from apps.mailroom.usecases.mail import SendMail

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.nchat.views.decorators import paid_up_account_required


# @paid_up_account_required(payment_url='/nchat/payment/edit/')


@login_required()
def add(request, template_id=None):
    """ mailroom add trigger message """
    service_info = AuthorizeUser(request.user, request.path).execute()

    # create new message and trigger instances
    new_message = Message(owner_id=service_info["owner_id"], app_id=service_info["app_id"])
    new_message.save()
    new_trigger = MaTrigger(message=new_message, trigger_type_id=1)
    new_trigger.save()

    redirect_url = "/" + service_info["namespace"] + "/mailroom/direct/edit/1/"
    return redirect(redirect_url)


# @paid_up_account_required(payment_url='/nchat/payment/edit/')
@login_required()
def edit(request, message_id=None, base_template='blank', template=None):
    """
        mailroom direct message
        Sends message directly to a selected group of users
     """

    # todo find out if there is a better alternative to the following
    from messaging_platform.settings.base import FROALA_EDITOR_OPTIONS
    FROALA_EDITOR_OPTIONS['language'] = str(_('en'))

    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'direct', base_template, template).execute()

    messages = Message.objects.filter(owner_id=service_info["owner_id"], app_id=service_info["app_id"]).values_list('id',
                                                                                                            flat=True)
    triggers = MaTrigger.objects.filter(message_id__in=messages).all()

    if request.POST:
        message_form = MaDirectMessageForm(request.POST)
        if message_form.is_valid():
            SendMail(service_info, message_form).execute()
            redirect_url = "/" + service_info["namespace"] + "/mailroom/message_history/list/"
            return redirect(redirect_url)
    else:
        message_form = MaDirectMessageForm()

    email_recipients = []
    if request.POST.get('email_recipients'):
        email_recipients.extend([request.POST.get('email_recipients')])
    email_recipients_json = json.dumps(email_recipients)

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
        "message_form": message_form,
        "triggers": triggers,
        "list": active_triggers,
        "list_type": "active_triggers",
        "email_recipients": email_recipients_json,
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        },
        "mail_type": "direct"
    }

    return render(request, template_info['template'], context)
