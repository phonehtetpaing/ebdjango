from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.utils import timezone

# import models
from apps.core.models.auto_message_trigger import AutoMessageTrigger
from apps.core.models.auto_message_controller import AutoMessageController
from apps.core.models.messaging_api_type import MessagingAPIType
from apps.core.models.auto_message_condition import AutoMessageCondition
from apps.core.models.message_status import MessageStatus

# import views
from apps.core.views.vendor_common.login_user_info import *
from apps.core.views.vendor_common.auto_messsage import *
from apps.core.views.vendor_common.message_json_converter import *

# import forms
from apps.core.forms.message import AutoMessageTriggerForm


@login_required
def edit(request, auto_message_id=None):
    user_obj = get_login_user_objects(request)
    # parse POST data to dict
    api_list = parse_messages(request.POST)

    auto_message_trigger = AutoMessageTrigger.objects.filter(id=auto_message_id).first()
    auto_message_condition = AutoMessageCondition.objects.filter(id=auto_message_trigger.auto_message_condition_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    if auto_message_condition:
        auto_message_trigger.auto_message_condition = auto_message_condition
        auto_message_trigger.save()

    trigger_form = AutoMessageTriggerForm(request.POST or None, instance=auto_message_trigger)
    context = {
        "title": "Message Details",
        "path": ["Message List", "Message Details"],
        "auto_message_id": auto_message_id,
        "auto_message_condition": auto_message_condition,
        "trigger_form": trigger_form,
        "api_list": api_list,
        "namespace": user_obj["service_namespace"]
    }

    if trigger_form.is_valid():
        trigger = trigger_form.save(commit=False)
        trigger.update_dt = timezone.now()
        trigger.save()

        # delete all previous message_controller instances
        auto_message_controller = AutoMessageController.objects.filter(auto_message_trigger=auto_message_trigger)
        if auto_message_controller:
            auto_message_controller.delete()

        message_order = 0
        # insert new message_controllers for each found JSON message
        for message in api_list:
            message_order += 1
            auto_message_controller = AutoMessageController()
            auto_message_controller.auto_message_trigger = auto_message_trigger
            auto_message_controller.messaging_api_type = MessagingAPIType.objects.filter(name=message['type']).first()
            auto_message_controller.messaging_api_param_json = message
            auto_message_controller.run_order_num = message_order
            auto_message_controller.save()

        context["title"] = "Confirm Changes"
        context["path"] = ["Message List", "Message Details", "Confirm Changes"]
        return render(request, "vendor/auto_message_confirm.html", context)

    return render(request, "vendor/auto_message_detail.html", context)


@login_required
def list(request):
    """ message send confirm  """
    user_obj = get_login_user_objects(request)

    auto_message_conditions = AutoMessageCondition.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).order_by('display_order_num')
    message_list = []

    for condition in auto_message_conditions:
        message_triggers = AutoMessageTrigger.objects.filter(auto_message_condition_id=condition.id, is_delete=False)
        page = request.GET.get('page'+condition.id.__str__(), 1)

        paginator = Paginator(message_triggers, settings.RESULTS_PER_PAGE)
        try:
            messages = paginator.page(page)
        except PageNotAnInteger:
            messages = paginator.page(1)
        except EmptyPage:
            messages = paginator.page(paginator.num_pages)

        messages = {
            'tab_id': condition.id,
            'tab_name': condition.name,
            'messages': messages,
        }
        message_list.append(messages)

    context = {
        "title": "Message List",
        "path": ["Message List"],
        "message_list": message_list,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/auto_message_list.html", context)


@login_required
def detail(request, auto_message_id=None):
    """ message completion """
    user_obj = get_login_user_objects(request)

    auto_message_trigger = AutoMessageTrigger.objects.filter(id=auto_message_id).first()
    if auto_message_trigger:
        auto_message_condition = AutoMessageCondition.objects.filter(id=auto_message_trigger.auto_message_condition_id, vendor_branch_id=user_obj["vendor_branch"].id).first()
        auto_message_controllers = AutoMessageController.objects.filter(auto_message_trigger=auto_message_trigger)

    api_list = []
    for controller in auto_message_controllers:
            api_list.append(ast.literal_eval(controller.messaging_api_param_json))

    trigger_form = AutoMessageTriggerForm(request.POST or None, instance=auto_message_trigger)

    context = {
        "title": "Message Details",
        "path": ["Message List", "Message Details"],
        "auto_message_id": auto_message_id,
        "auto_message_condition": auto_message_condition,
        "trigger_form": trigger_form,
        "api_list": api_list,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/auto_message_detail.html", context)


@login_required
def add(request, auto_message_condition_id=None):
    """ message create  """
    user_obj = get_login_user_objects(request)

    auto_message_condition = AutoMessageCondition.objects.filter(id=auto_message_condition_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).first()
    message_draft_status = MessageStatus.objects.filter(name='draft').first()

    auto_message_trigger = AutoMessageTrigger()
    auto_message_trigger.auto_message_condition_id = auto_message_condition_id
    auto_message_trigger.message_status_id = message_draft_status.id
    auto_message_trigger.save()
    trigger_form = AutoMessageTriggerForm(request.POST or None, instance=auto_message_trigger)

    auto_message_controllers = AutoMessageController.objects.filter(auto_message_trigger=auto_message_trigger)

    api_list = []
    for controller in auto_message_controllers:
        api_list.append(ast.literal_eval(controller.messaging_api_param_json))

    context = {
        "title": "Message Details",
        "path": ["Message List", "Message Details"],
        "auto_message_id": auto_message_trigger.id,
        "auto_message_condition": auto_message_condition,
        "trigger_form": trigger_form,
        "api_list": api_list,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/auto_message_detail.html", context)


@login_required
def confirm(request, auto_message_id=None):
    user_obj = get_login_user_objects(request)

    auto_message_trigger = AutoMessageTrigger.objects.filter(id=auto_message_id).first()
    auto_message_condition = AutoMessageCondition.objects.filter(id=auto_message_trigger.auto_message_condition_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    if auto_message_condition:
        message_status = MessageStatus.objects.filter(name='pending').first()
        auto_message_trigger.message_status_id = message_status.id
        auto_message_trigger.save()

    auto_message_conditions = AutoMessageCondition.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).order_by('display_order_num')
    message_list = []

    for condition in auto_message_conditions:
        message_triggers = AutoMessageTrigger.objects.filter(auto_message_condition_id=condition.id, is_delete=0)
        messages = {
            'tab_id': condition.id,
            'tab_name': condition.name,
            'messages': message_triggers,
        }
        message_list.append(messages)

    redirect_url = "/" + user_obj["service_url"] + "/auto/message/list/"
    return redirect(redirect_url)


@login_required
def delete(request):
    user_obj = get_login_user_objects(request)
    print(request.POST)
    if request.method == "POST":
        delete_ids = request.POST.getlist('select_item')
        print('delete ids', delete_ids)
        auto_message_trigger = AutoMessageTrigger.objects.filter(id__in=delete_ids)
        auto_message_trigger.update(is_delete=1)

    redirect_url = "/" + user_obj["service_url"] + "/auto/message/list/"
    return redirect(redirect_url)


@login_required
def inactive(request, auto_message_id=None):
    user_obj = get_login_user_objects(request)

    auto_message_trigger = AutoMessageTrigger.objects.filter(id=auto_message_id).first()
    message_draft_status = MessageStatus.objects.filter(name='draft').first()

    if auto_message_trigger:
        auto_message_trigger.message_status = message_draft_status
        auto_message_trigger.save()

    redirect_url = "/" + user_obj["service_url"] + "/auto/message/list/"
    return redirect(redirect_url)


@login_required
def active(request, auto_message_id=None):
    user_obj = get_login_user_objects(request)

    auto_message_trigger = AutoMessageTrigger.objects.filter(id=auto_message_id).first()
    message_draft_status = MessageStatus.objects.filter(name='pending').first()

    if auto_message_trigger:
        auto_message_trigger.message_status = message_draft_status
        auto_message_trigger.save()

    redirect_url = "/" + user_obj["service_url"] + "/auto/message/list/"
    return redirect(redirect_url)


@login_required
def send_test(request, auto_message_id=None):
    """ send test message to login-user """
    user_obj = get_login_user_objects(request)

    auto_message_trigger = AutoMessageTrigger.objects.filter(id=auto_message_id).first()
    if auto_message_trigger:
        send_unit_message(request, auto_message_trigger, None, True)
    
    redirect_url = "/" + user_obj["service_url"] + "/auto/message/list/"
    return redirect(redirect_url)
