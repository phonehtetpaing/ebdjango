from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# import models
from django.template.loader import render_to_string

from apps.core.models.file import File
from apps.core.models.message_block import MessageBlock
from apps.core.models.message_sequence import MessageSequence

# import views
from apps.core.views.vendor_common.login_user_info import *
from apps.core.views.vendor_common.message_json_converter import *


@login_required
def add(request, message_block_id=None):
    user_obj = get_login_user_objects(request)

    block_message = MessageBlock()
    block_message.vendor_branch_id = user_obj["vendor_branch"].id
    block_message.messaging_api_param_json = []
    block_message.save()

    redirect_url = "/" + user_obj["service_url"] + "/block/message/detail/" + str(block_message.id) + "/"
    return redirect(redirect_url)


@login_required
def detail(request, message_block_id=None):
    user_obj = get_login_user_objects(request)

    message_sequences = MessageSequence.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)
    message_blocks = MessageBlock.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)

    if message_block_id:
        message_block = MessageBlock.objects.filter(id=message_block_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    else:
        message_block = MessageBlock.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()

    messages = ast.literal_eval(message_block.messaging_api_param_json)
    files = File.objects.filter(vendor_branch=user_obj["vendor_branch"])

    context = {
        "title": "User Story",
        "path": ["User Story"],
        "message_block_id": message_block.id,
        "message_block": message_block,
        "message_sequences": message_sequences,
        "message_blocks": message_blocks,
        "api_list": messages,
        "files": files,
        "namespace": user_obj["service_namespace"],
    }

    return render(request, "vendor_contactchat/block_message.html", context)


@login_required
def edit(request, message_block_id=None):
    user_obj = get_login_user_objects(request)

    data = request.POST
    messages = parse_messages(data)

    message_block = MessageBlock.objects.filter(id=message_block_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    if message_block:
        message_block.messaging_api_param_json = messages
        message_block.admin_text = request.POST['admin_text']
        message_block.save()

    redirect_url = "/" + user_obj["service_url"] + "/block/message/detail/" + str(message_block_id) + "/"
    return redirect(redirect_url)


@login_required
def delete(request, message_block_id=None):
    user_obj = get_login_user_objects(request)

    # the message block in question
    message_block = MessageBlock.objects.filter(id=message_block_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    # the message sequence (if any) that has this block as a start block
    message_sequence = MessageSequence.objects.filter(start_block=message_block, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    if message_block and not message_sequence:
        message_block.is_delete = 1
        message_block.save()
    # cannot delete start block but you can clear it
    else:
        message_block.messaging_api_param_json = []
        message_block.save()

    redirect_url = "/" + user_obj["service_url"] + "/block/message/"
    return redirect(redirect_url)


@login_required
def get_message_template(request):
    """
    Returns a message template formatted with the provided query parameters
    or returns a 404
    :param request: expected parameters include type_name and display_order
    :return: JsonResponse containing html template
    """
    user_obj = get_login_user_objects(request)

    if request.GET:
        message_type = request.GET.get('type_name', None)
        display_order = request.GET.get('display_order', 0)

        if message_type == 'text_message' or message_type == 'carousel_message' or message_type == 'input_message':
            html = render_to_string('forms/messages/{0}.html'.format(message_type), {"message": {}, "message_counter": display_order}, request)
            return JsonResponse({'template': html})
        elif message_type == 'image_message' or message_type == 'file_message':
            files = File.objects.filter(vendor_branch=user_obj["vendor_branch"])
            html = render_to_string('forms/messages/{0}.html'.format(message_type),
                                    {"message": {}, "message_counter": display_order, "files": files}, request)
            return JsonResponse({'template': html})
        elif message_type == 'quickreply_message' or message_type == 'form_message':
            # QuickReply relies on at least one child existing (even if empty)
            html = render_to_string('forms/messages/{0}.html'.format(message_type),
                                    {"message": {"payload": [{}]}, "message_counter": display_order}, request)
            return JsonResponse({'template': html})
        elif message_type == 'wait_message':
            html = render_to_string('forms/messages/{0}.html'.format(message_type),
                                    {"message": {"payload": 100 }, "message_counter": display_order}, request)
            return JsonResponse({'template': html})
        elif message_type == 'tag_message':
            html = render_to_string('forms/messages/{0}.html'.format(message_type),
                                    {"message": {"payload": {}}, "message_counter": display_order}, request)
            return JsonResponse({'template': html})
        elif message_type == 'goto_message':
            message_blocks = MessageBlock.objects.filter(vendor_branch=user_obj["vendor_branch"])
            html = render_to_string('forms/messages/{0}.html'.format(message_type),
                                    {"message": {"payload": [0, 0]}, "message_counter": display_order, "message_blocks": message_blocks}, request)
            return JsonResponse({'template': html})

    return HttpResponseNotFound()
