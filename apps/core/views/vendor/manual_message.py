from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext
from django.conf import settings

# import models
from apps.core.models.manual_message_overview import ManualMessageOverview
from apps.core.models.manual_message_controller import ManualMessageController
from apps.core.models.message_status import MessageStatus
from apps.core.models.messaging_api_type import MessagingAPIType
from apps.core.models.tag_category import TagCategory
from apps.core.models.tag import Tag

# import views
from apps.core.views.vendor_common.login_user_info import *
from apps.core.views.vendor_common.messsage_tagged_user import *
from apps.core.views.aws_utils.boto_sqs import *
from apps.core.views.aws_utils.simulator_sqs import *
from apps.core.views.vendor_common.message_json_converter import *


@login_required
def list(request):
    """ list """
    user_obj = get_login_user_objects(request)

    message_status = MessageStatus.objects.filter(name__in=["draft", "pending", "scheduled"], is_delete=False).all()

    message_list = ManualMessageOverview.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, message_status__in=message_status, is_delete=0).order_by("message_status")
    page = request.GET.get('page', 1)

    paginator = Paginator(message_list, settings.RESULTS_PER_PAGE)
    try:
        messages = paginator.page(page)
    except PageNotAnInteger:
        messages = paginator.page(1)
    except EmptyPage:
        messages = paginator.page(paginator.num_pages)

    context = {
        "title": "Message List",
        "path": ["Message List"],
        "messages": messages,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/manual_message_list.html", context)


@login_required
def detail(request, message_id=None):
    """ detail """
    user_obj = get_login_user_objects(request)

    manual_message_overview = ManualMessageOverview.objects.filter(id=message_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    manual_message_controllers = ManualMessageController.objects.filter(manual_message_overview_id=manual_message_overview.id)

    tag_categories = TagCategory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)
    tag_list = Tag.objects.filter(tag_category_id__in=tag_categories, is_delete=0)

    api_list = []
    for controller in manual_message_controllers:
        api_list.append(ast.literal_eval(controller.messaging_api_param_json))

    selected_tag_list = []
    if manual_message_overview.tags:
        selected_tag_list = [int(x) for x in manual_message_overview.tags.split(',') if x.strip().isdigit()]

    context = {
        "title": "Message Details",
        "path": ["Message List", "Message Details"],
        "message_id": message_id,
        "manual_message_overview": manual_message_overview,
        "api_list": api_list,
        "tag_list": tag_list,
        "selected_tag_list": selected_tag_list,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/manual_message_detail.html", context)


@login_required
def edit(request, message_id=None):
    user_obj = get_login_user_objects(request)

    manual_message_overview = ManualMessageOverview.objects.filter(id=message_id).first()
    if manual_message_overview:
        manual_message_overview.name = request.POST['name']
        selected_tags = ','.join(request.POST.getlist('tag_id', []))
        manual_message_overview.tags = selected_tags
        message_status = MessageStatus.objects.filter(name="pending").first()
        manual_message_overview.message_status = message_status

        # get push_dt
        push_date = request.POST["push_date"]
        push_time = request.POST["push_time"]
        if push_date != "" and push_time != "":
            push_dt_str = push_date + " " + push_time + ":00"
            push_dt = datetime.datetime.strptime(push_dt_str, '%Y-%m-%d %H:%M:%S')
            manual_message_overview.push_dt = push_dt
            message_status = MessageStatus.objects.filter(name="scheduled").first()
            manual_message_overview.message_status = message_status

        else:
            manual_message_overview.push_dt = None

        manual_message_overview.save()

        # parse POST data to dict
        parsed_data = parse_messages(request.POST)

        # delete all previous message_controller instances
        manual_message_controller = ManualMessageController.objects.filter(manual_message_overview=manual_message_overview)
        if manual_message_controller:
            manual_message_controller.delete()

        message_order = 0
        api_list = []
        # insert new message_controllers for each found JSON message
        for message in parsed_data:
            message_order += 1
            api_list.append(message)
            manual_message_controller = ManualMessageController()
            manual_message_controller.manual_message_overview = manual_message_overview
            manual_message_controller.messaging_api_type = MessagingAPIType.objects.filter(name=message['type']).first()
            manual_message_controller.messaging_api_param_json = message
            manual_message_controller.run_order_num = message_order
            manual_message_controller.save()

    redirect_url = "/" + user_obj["service_url"] + "/manual/message/list/"
    return redirect(redirect_url)


def add(request):
    """ message create  """
    user_obj = get_login_user_objects(request)

    manual_message_overview = ManualMessageOverview()
    manual_message_overview.vendor_branch_id = user_obj["vendor_branch"].id
    message_draft_status = MessageStatus.objects.filter(name='draft').first()

    manual_message_overview.message_status_id = message_draft_status.id
    manual_message_overview.save()

    manual_message_controllers = ManualMessageController.objects.filter(manual_message_overview=manual_message_overview)

    api_list = []
    for controller in manual_message_controllers:
        api_list.append(ast.literal_eval(controller.messaging_api_param_json))

    redirect_url = "/" + user_obj["service_url"] + "/manual/message/detail/" + str(manual_message_overview.id) + "/"
    return redirect(redirect_url)


@login_required
def delete(request):
    user_obj = get_login_user_objects(request)

    if request.method == "POST":
        delete_ids = request.POST.getlist('select_item')
        manual_message_overview = ManualMessageOverview.objects.filter(id__in=delete_ids)
        manual_message_overview.update(is_delete=1)

    redirect_url = "/" + user_obj["service_url"] + "/manual/message/list/"
    return redirect(redirect_url)


@login_required
def send_test(request, message_id=None):
    """ send test message to login-user """
    user_obj = get_login_user_objects(request)

    manual_message_overview = ManualMessageOverview.objects.filter(id=message_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    send_message_to_tagged_user(request, None, manual_message_overview, None, True)

    redirect_url = "/" + user_obj["service_url"] + "/manual/message/list/"
    return redirect(redirect_url)


@login_required
def send_message(request, message_id=None):
    """ send message to tagged end_user """
    user_obj = get_login_user_objects(request)

    manual_message_overview = ManualMessageOverview.objects.filter(id=message_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()

    # tag_id_list = manual_message_overview.tags.split(",")
    # vendor_branch_id_list = [user_obj["vendor_branch"].id]
    # send_message_to_tagged_user(request, tag_id_list, manual_message_overview, vendor_branch_id_list, False)

    # Create a new History
    vendor_branch = manual_message_overview.vendor_branch
    send_dt = datetime.datetime.now()
    manual_message_history = ManualMessageHistory()
    manual_message_history.vendor_branch = vendor_branch
    manual_message_history.manual_message_overview = manual_message_overview
    manual_message_history.send_dt = send_dt
    manual_message_history.save()

    # Change Status
    message_status = MessageStatus.objects.filter(name="sending", is_delete=False).first()
    manual_message_overview.message_status = message_status
    manual_message_overview.save()

    # Push message to SQS
    if settings.MODE == "LOCAL":
        push_sim_manual_message(manual_message_overview.id, user_obj["vendor_user"].id, manual_message_history.id)

    else:
        push_manual_message(manual_message_overview.id, user_obj["vendor_user"].id, manual_message_history.id)

    redirect_url = "/" + user_obj["service_url"] + "/auto/message/history/list/"
    return redirect(redirect_url)


@login_required
def send_confirm(request, message_id=None):
    """ confirm message """
    user_obj = get_login_user_objects(request)

    manual_message_overview = ManualMessageOverview.objects.filter(id=message_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    manual_message_controllers = ManualMessageController.objects.filter(manual_message_overview_id=manual_message_overview.id)

    tag_categories = TagCategory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)
    tag_list = Tag.objects.filter(tag_category_id__in=tag_categories, is_delete=0)

    api_list = []
    for controller in manual_message_controllers:
        api_list.append(ast.literal_eval(controller.messaging_api_param_json))

    selected_tag_list = []
    if manual_message_overview.tags:
        selected_tag_list = [int(x) for x in manual_message_overview.tags.split(',') if x.strip().isdigit()]

    # Get total number of users
    end_user_count = EndUser.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=False).count()
    # Get Selected Tag users
    tags = Tag.objects.filter(id__in=selected_tag_list).all()
    tag_code_list = []
    for tag in tags:
        tag_code_list.append(tag.cd)
    tagged_user_count = EndUser.objects.filter(tag__name__in=tag_code_list, is_delete=0).distinct().count()
    # Get Percentage of tagged users
    user_ratio = round(tagged_user_count / end_user_count * 100)

    print(selected_tag_list)
    print(user_ratio)

    context = {
        "title": "Message Details",
        "path": ["Message List", "Message Details"],
        "message_id": message_id,
        "manual_message_overview": manual_message_overview,
        "api_list": api_list,
        "tag_list": tag_list,
        "selected_tag_list": selected_tag_list,
        "end_user_count": end_user_count,
        "tagged_user_count": tagged_user_count,
        "user_ratio": user_ratio,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/manual_message_confirm.html", context)
