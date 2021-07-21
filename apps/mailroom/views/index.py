from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# import models
from apps.mailroom.models.trigger_type import MaTriggerType
from apps.mailroom.models.trigger import MaTrigger
from apps.mailroom.models.message import Message

# import usecase
from apps.mailroom.usecases.user import AuthorizeUser

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required()
def index(request):
    """ mailroom """
    service_info = AuthorizeUser(request.user, request.path).execute()
    messages = Message.objects.filter(owner_id=service_info["owner_id"], app_id=service_info["app_id"]).values_list('id',
                                                                                                            flat=True)
    triggers = MaTrigger.objects.filter(message_id__in=messages).all()
    trigger_types = MaTriggerType.objects.filter().all()

    page = request.GET.get('page', 1)
    paginator = Paginator(triggers, 5)
    try:
        triggers = paginator.page(page)
    except PageNotAnInteger:
        triggers = paginator.page(1)
    except EmptyPage:
        triggers = paginator.page(paginator.num_pages)

    context = {
        "title": "Messenger",
        "namespace": service_info["namespace"],
        "trigger_types": trigger_types,
        "triggers": triggers,
    }

    return render(request, "mailroom/index.html", context)
