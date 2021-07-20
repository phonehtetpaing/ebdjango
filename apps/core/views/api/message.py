from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from copy import deepcopy

# import Models
from apps.core.models import MessageBlock, MessageSequence

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def get_message_blocks(request, *args, **kwargs):
    """ Returns a flattened list of all message blocks for this vendor user"""
    user_obj = get_login_user_objects(request)

    message_blocks = MessageBlock.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).all()

    data = []
    data_object = {
        "name": "",
        "id": ""
    }

    for block in message_blocks:
        tmp = deepcopy(data_object)
        tmp["name"] = block.admin_text
        tmp["id"] = block.id
        data.append(tmp)

    return JsonResponse({"data": data})


@login_required
def get_message_sequences(request, *args, **kwargs):
    """ Returns a flattened list of all message sequences for this vendor user"""
    user_obj = get_login_user_objects(request)

    message_sequences = MessageSequence.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).all()

    data = []
    data_object = {
        "name": "",
        "id": ""
    }

    for sequence in message_sequences:
        tmp = deepcopy(data_object)
        tmp["name"] = sequence.admin_text
        tmp["id"] = sequence.id
        data.append(tmp)

    return JsonResponse({"data": data})
