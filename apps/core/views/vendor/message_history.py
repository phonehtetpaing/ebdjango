from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

# import models
from apps.core.models.auto_message_history import AutoMessageHistory
from apps.core.models.auto_message_trigger import AutoMessageTrigger
from apps.core.models.manual_message_history import ManualMessageHistory
from apps.core.models.end_user import EndUser

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def list(request):
    """ history list  """
    user_obj = get_login_user_objects(request)

    auto_msg_history = AutoMessageHistory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)
    page = request.GET.get('page1', 1)

    paginator = Paginator(auto_msg_history, settings.RESULTS_PER_PAGE)
    try:
        auto_message_history = paginator.page(page)
    except PageNotAnInteger:
        auto_message_history = paginator.page(1)
    except EmptyPage:
        auto_message_history = paginator.page(paginator.num_pages)

    manual_msg_history = ManualMessageHistory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)
    page = request.GET.get('page2', 1)

    paginator = Paginator(manual_msg_history, settings.RESULTS_PER_PAGE)
    try:
        manual_message_history = paginator.page(page)
    except PageNotAnInteger:
        manual_message_history = paginator.page(1)
    except EmptyPage:
        manual_message_history = paginator.page(paginator.num_pages)

    context = {
        "title": "AutoMessage History",
        "path": ["AutoMessage History"],
        "auto_message_history": auto_message_history,
        "manual_message_history": manual_message_history,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/message_history_list.html", context)


@login_required
def detail(request, auto_message_history_id=None):
    """ history detail  """
    user_obj = get_login_user_objects(request)

    auto_message_history = AutoMessageHistory.objects.filter(id=auto_message_history_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()

    user_list = []

    if auto_message_history:
        if auto_message_history.send_user_id_csv:
            user_id_list = auto_message_history.send_user_id_csv.split(",")
            for user_id in user_id_list:
                tmp_user = EndUser.objects.filter(id=user_id).first()
                if tmp_user:
                    user_list.append(tmp_user)

    context = {
        "title": "AutoMessage History",
        "path": ["AutoMessage History", "AutoMessage History Details"],
        "message_history_id": auto_message_history_id,
        "message_history": auto_message_history,
        "user_list": user_list,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/message_history_detail.html", context)


@login_required
def manual_detail(request, manual_message_history_id=None):
    """ history detail  """
    user_obj = get_login_user_objects(request)

    manual_message_history = ManualMessageHistory.objects.filter(id=manual_message_history_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()

    user_list = []

    if manual_message_history:
        if manual_message_history.send_user_id_csv:
            for user_id in manual_message_history.send_user_id_csv.split(","):
                tmp_user = EndUser.objects.filter(id=user_id).first()
                if tmp_user:
                    user_list.append(tmp_user)

    context = {
        "title": "AutoMessage History",
        "path": ["AutoMessage History", "AutoMessage History Details"],
        "manual_message_history_id": manual_message_history_id,
        "message_history": manual_message_history,
        "user_list": user_list,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/message_history_detail.html", context)
