from django.shortcuts import render, redirect

# import models
from apps.mailroom.models.message_history import MessageHistory

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.mailroom.forms.message import MessageHistoryForm

# import usecase
from apps.mailroom.usecases.user import AuthorizeUser
from apps.mailroom.usecases.template import RetrieveTemplates

@login_required()
def list(request, base_template='blank', template=None):
    """ mailroom message history list """
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'history_list', base_template, template).execute()

    message_history = MessageHistory.objects.filter(owner_id=service_info["owner_id"],
                                                    app_id=service_info["app_id"]).all().order_by("-id")

    page = request.GET.get('page', 1)
    paginator = Paginator(message_history, 10)
    try:
        message_history = paginator.page(page)
    except PageNotAnInteger:
        message_history = paginator.page(1)
    except EmptyPage:
        message_history = paginator.page(paginator.num_pages)

    context = {
        "title": "Message History",
        "namespace": service_info["namespace"],
        "list": message_history,
        "list_type": "message_history",
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        }
    }

    return render(request, template_info['template'], context)

@login_required()
def detail(request, trigger_id=None, base_template='blank', template=None):
    """ mailroom message history list """
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'message_history_detail', base_template, template).execute()

    message_history = MessageHistory.objects.filter(owner_id=service_info["owner_id"],
                                                    app_id=service_info["app_id"]).all().order_by("-id")

    message = MessageHistory.objects.filter(owner_id=service_info["owner_id"],
                                                    app_id=service_info["app_id"],
                                                    id=trigger_id).first()

    form = MessageHistoryForm(instance=message)

    page = request.GET.get('page', 1)
    paginator = Paginator(message_history, 10)
    try:
        message_history = paginator.page(page)
    except PageNotAnInteger:
        message_history = paginator.page(1)
    except EmptyPage:
        message_history = paginator.page(paginator.num_pages)

    context = {
        "title": "Message History",
        "namespace": service_info["namespace"],
        "list": message_history,
        "list_type": "message_history",
        "form": form,
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        }
    }

    return render(request, template_info['template'], context)

@login_required()
def delete(request):
    """ Delete existing mailroom message history """
    service_info = AuthorizeUser(request.user, request.path).execute()

    delete_list = request.POST.getlist("item-selection")

    MessageHistory.objects.filter(id__in=delete_list).delete()

    redirect_url = "/" + service_info["namespace"] + "/mailroom/message_history/list/"
    return redirect(redirect_url)
