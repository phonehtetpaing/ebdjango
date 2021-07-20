from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# import models
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

    context = {
        "title": "User Story",
        "path": ["User Story"],
        "message_block_id": message_block.id,
        "message_block": message_block,
        "message_sequences": message_sequences,
        "message_blocks": message_blocks,
        "api_list": messages,
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

    message_block = MessageBlock.objects.filter(id=message_block_id).first()
    message_sequence = MessageSequence.objects.filter(start_block=message_block).first()
    if message_block and not message_sequence:
        message_block.is_delete = 1
        message_block.save()
    # cannot delete start block but you can clear it
    else:
        message_block.messaging_api_param_json = []
        message_block.save()

    redirect_url = "/" + user_obj["service_url"] + "/block/message/detail/" + str(1) + "/"
    return redirect(redirect_url)
