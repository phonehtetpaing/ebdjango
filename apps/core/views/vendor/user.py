from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from django.conf import settings

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_facebook import EndUserFacebook
from apps.core.models.end_user_line import EndUserLINE
from apps.core.models.end_user_auto_message import EndUserAutoMessage
from apps.core.models.tag_category import TagCategory
from apps.core.models.tag import Tag
from apps.core.models.auto_message_condition import AutoMessageCondition

# import views
from apps.core.views.vendor_common.login_user_info import *
from apps.core.views.api.tagged_end_users import *

# import filters
from apps.core.filters.filters import UserFilter

# import forms
from apps.core.forms.end_user import EndUserForm


@login_required
def list(request):
    """ User Index """
    user_obj = get_login_user_objects(request)

    tag_categories = TagCategory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)
    tag_users = Tag.objects.filter(tag_category_id__in=tag_categories, is_delete=0).values_list('cd', flat=True)
    end_users = EndUser.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)
    user_filter = UserFilter(request.GET, queryset=end_users, request=request)

    context = {
        "title": "User List",
        "path": ["User List"],
        "end_users": end_users,
        "tag_users": tag_users,
        "filter": user_filter,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/user_list.html", context)


@login_required
def detail(request, end_user_id=None):
    """ User Index """
    user_obj = get_login_user_objects(request)
    end_user = EndUser.objects.filter(id=end_user_id, vendor_branch_id=user_obj["vendor_branch"].id).first()
    end_user_facebook = EndUserFacebook.objects.filter(end_user_id=end_user_id).first()
    end_user_line = EndUserLINE.objects.filter(end_user_id=end_user_id).first()
    end_user_attributes = end_user.get_attribute_json()

    # Get Tag Data
    tag_codes = end_user.tag.all()
    tag_code_list = []
    for tag_code in tag_codes:
        tag_code_list.append(tag_code.name)

    tag_categories = TagCategory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).all()
    tag_category_list = []
    for tag_category in tag_categories:
        tag_category_list.append(tag_category.id)

    tags = Tag.objects.filter(tag_category_id__in=tag_category_list, is_delete=False).order_by('display_order_num')

    # Datetime for Auto Message
    auto_message_conditions = AutoMessageCondition.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=False).all()
    end_user_auto_messages = EndUserAutoMessage.objects.filter(end_user=end_user, is_delete=False).all()

    if request.method == "POST":
        form = EndUserForm(request.POST, instance=end_user)
        if form.is_valid():
            end_user = form.save(commit=False)
            end_user.update_dt = timezone.now()
            end_user.save()
    else:
        form = EndUserForm(instance=end_user)

    context = {
        "title": "User Details",
        "path": ["User List", "User Details"],
        "end_user": end_user,
        "end_user_attributes": end_user_attributes,
        "end_user_facebook": end_user_facebook,
        "end_user_line": end_user_line,
        "tags": tags,
        "form": form,
        "tag_code_list": tag_code_list,
        "auto_message_conditions": auto_message_conditions,
        "end_user_auto_messages": end_user_auto_messages,
        "namespace": user_obj["service_namespace"],
    }

    return render(request, "vendor/user_detail.html", context)


@login_required
def edit(request, end_user_id=None):
    user_obj = get_login_user_objects(request)

    end_user = EndUser.objects.filter(id=end_user_id, vendor_branch_id=user_obj["vendor_branch"].id).first()
    end_user_facebook = EndUserFacebook.objects.filter(end_user_id=end_user_id).first()
    end_user_line = EndUserLINE.objects.filter(end_user_id=end_user_id).first()

    # Reset Tags
    tag_id_list_string = request.POST.getlist('tag_id[]')
    tag_id_list = []
    for tag_id_string in tag_id_list_string:
        tag_id_list.append(int(tag_id_string))

    tag_categories = TagCategory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).all()
    tag_category_list = []
    for tag_category in tag_categories:
        tag_category_list.append(tag_category.id)

    tags = Tag.objects.filter(tag_category_id__in=tag_category_list, id__in=tag_id_list).order_by('display_order_num')
    end_user.tag.clear()
    for tag in tags:
        end_user.tag.add(tag.cd)

    # Auto Message Conditions
    auto_message_conditions = AutoMessageCondition.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=False)
    for auto_message_condition in auto_message_conditions:
        type_name = auto_message_condition.name
        if (type_name + "_date" in request.POST) and (type_name + "_time" in request.POST):
            yyyymmdd = request.POST[type_name + "_date"]
            hhmm = request.POST[type_name + "_time"]
            if len(yyyymmdd) !=0 and len(hhmm) !=0:
                if hhmm == "" or hhmm is None:
                    hhmmss = "00:00:00"
                else:
                    hhmmss = hhmm + ":00"
                yyyymmddhhmm = yyyymmdd + " " + hhmmss

                end_user_auto_message = EndUserAutoMessage.objects.filter(end_user=end_user, auto_message_type=auto_message_condition.auto_message_type).first()
                end_user_auto_message.message_target_dt = datetime.datetime.strptime(yyyymmddhhmm, '%Y-%m-%d %H:%M:%S')
                end_user_auto_message.save()

    end_user_auto_messages = EndUserAutoMessage.objects.filter(end_user=end_user, is_delete=False).all()

    # Get Tag Data
    tag_codes = end_user.tag.all()
    tag_code_list = []
    for tag_code in tag_codes:
        tag_code_list.append(tag_code.name)

    if request.method == "POST":
        form = EndUserForm(request.POST, instance=end_user)
        if form.is_valid():
            end_user = form.save(commit=False)
            end_user.update_dt = timezone.now()
            end_user.save()

            redirect_url = "/" + user_obj["service_url"] + "/user/list/"
            return redirect(redirect_url)
    else:
        form = EndUserForm(instance=end_user)

    context = {
        "title": "User Details",
        "path": ["User List", "User Details"],
        "end_user": end_user,
        "end_user_facebook": end_user_facebook,
        "end_user_line": end_user_line,
        "tags": tags,
        "form": form,
        "tag_code_list": tag_code_list,
        "auto_message_conditions": auto_message_conditions,
        "end_user_auto_messages": end_user_auto_messages,
        "namespace": user_obj["service_namespace"],
    }

    return render(request, "vendor/user_detail.html", context)


@login_required
def delete(request):
    user_obj = get_login_user_objects(request)

    if request.method == "POST":
        delete_ids = request.POST.getlist('select_item')
        end_users = EndUser.objects.filter(id__in=delete_ids, vendor_branch_id=user_obj["vendor_branch"].id)
        end_users.update(is_delete=1)

    redirect_url = "/" + user_obj["service_url"] + "/user/list/"
    return redirect(redirect_url)
