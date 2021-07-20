import json
import string
import random

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
# import models

from apps.core.models.affiliate import Affiliate


# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def list(request):
    """ list """
    user_obj = get_login_user_objects(request)

    affiliate_list = Affiliate.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).order_by("name").all()
    page = request.GET.get('page', 1)

    paginator = Paginator(affiliate_list, settings.RESULTS_PER_PAGE)
    try:
        affiliates = paginator.page(page)
    except PageNotAnInteger:
        affiliates = paginator.page(1)
    except EmptyPage:
        affiliates = paginator.page(paginator.num_pages)

    context = {
        "title": "Affiliate List",
        "path": ["Affiliate", "List"],
        "affiliates": affiliates,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/affiliate_list.html", context)


@login_required
def detail(request, affiliate_id=None):
    """ detail """
    user_obj = get_login_user_objects(request)

    if affiliate_id == 0:
        affiliate = {"id": 0}
    else:
        affiliate = Affiliate.objects.filter(id=affiliate_id, vendor_branch_id=user_obj["vendor_branch"].id).first()

    context = {
        "title": "Affiliate Details",
        "path": ["Affiliate", "Details"],
        "affiliate": affiliate,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/affiliate_detail.html", context)


@login_required
def edit(request, affiliate_id=None):
    """ Update Affiliate """
    user_obj = get_login_user_objects(request)

    affiliate = Affiliate.objects.filter(id=affiliate_id, vendor_branch_id=user_obj["vendor_branch"].id).first()

    affiliate.name = request.POST["name"]
    affiliate.tag_name = request.POST["tag_name"]

    if affiliate.url_part is None or affiliate.url_part == "":
        affiliate.url_part = random_number(12)

    affiliate.save()

    redirect_url = "/" + user_obj["service_url"] + "/affiliate/list/"
    return redirect(redirect_url)


@login_required
def add(request):
    """ Add EventCategory """
    user_obj = get_login_user_objects(request)

    affiliate = Affiliate()
    affiliate.vendor_branch = user_obj["vendor_branch"]
    affiliate.name = request.POST["name"]
    affiliate.tag_name = request.POST["tag_name"]
    affiliate.is_active = 1

    if affiliate.url_part is None or affiliate.url_part == "":
        affiliate.url_part = random_number(12)

    affiliate.save()

    redirect_url = "/" + user_obj["service_url"] + "/affiliate/list/"
    return redirect(redirect_url)


@login_required
def delete(request, affiliate_id=None):
    """ Delete """
    user_obj = get_login_user_objects(request)

    affiliate = Affiliate.objects.filter(id=affiliate_id, vendor_branch_id=user_obj["vendor_branch"].id).first()
    affiliate.is_delete = 1
    affiliate.save()

    redirect_url = "/" + user_obj["service_url"] + "/affiliate/list/"
    return redirect(redirect_url)


@login_required
def activate(request, affiliate_id=None):
    """ Delete """
    user_obj = get_login_user_objects(request)

    affiliate = Affiliate.objects.filter(id=affiliate_id, vendor_branch_id=user_obj["vendor_branch"].id).first()
    affiliate.is_active = 1
    affiliate.save()

    redirect_url = "/" + user_obj["service_url"] + "/affiliate/list/"
    return redirect(redirect_url)


@login_required
def deactivate(request, affiliate_id=None):
    """ Delete """
    user_obj = get_login_user_objects(request)

    affiliate = Affiliate.objects.filter(id=affiliate_id, vendor_branch_id=user_obj["vendor_branch"].id).first()
    affiliate.is_active = 0
    affiliate.save()

    redirect_url = "/" + user_obj["service_url"] + "/affiliate/list/"
    return redirect(redirect_url)


@login_required
def user_list(request, affiliate_id=None):
    """ Affiliate User List """
    user_obj = get_login_user_objects(request)

    affiliate = Affiliate.objects.filter(id=affiliate_id).first()
    end_user_id_list = get_end_user_id_list_from_affiliate(affiliate_id)
    end_users_list = EndUser.objects.filter(id__in=end_user_id_list).order_by("-regist_dt").all()
    # Get Summary
    end_user_sum_list = []
    for end_user in end_users_list:
        regist_yyyymm = end_user.regist_dt.strftime('%Y-%m')
        tmp_end_user_sum_list = end_user_sum_list

        if len(end_user_sum_list) == 0:
            tmp_user_dict = {
                "regist_yyyymm": regist_yyyymm,
                "user_id_list": [end_user.id]
            }

            end_user_sum_list.append(tmp_user_dict)

        else:
            is_new_regist_yyyymm = True
            for i, end_user_sum_dict in enumerate(tmp_end_user_sum_list):
                if end_user_sum_dict["regist_yyyymm"] == regist_yyyymm:
                    end_user_sum_dict["user_id_list"].append(end_user.id)
                    end_user_sum_list[i] = end_user_sum_dict
                    is_new_regist_yyyymm = False

            if is_new_regist_yyyymm:
                tmp_user_dict = {
                    "regist_yyyymm": regist_yyyymm,
                    "user_id_list": [end_user.id]
                }
                end_user_sum_list.append(tmp_user_dict)

    page = request.GET.get('page', 1)
    paginator = Paginator(end_users_list, settings.RESULTS_PER_PAGE)
    try:
        end_users = paginator.page(page)
    except PageNotAnInteger:
        end_users = paginator.page(1)
    except EmptyPage:
        end_users = paginator.page(paginator.num_pages)

    context = {
        "title": "Affiliate User List",
        "path": ["Affiliate", "User", "List"],
        "affiliate": affiliate,
        "end_users": end_users,
        "end_user_sum_list": end_user_sum_list,
        "end_users_total": end_users_list.count(),
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/affiliate_user_list.html", context)


def random_number(n):
    c = string.digits
    return ''.join([random.choice(c) for i in range(n)])


def get_end_user_id_list_from_affiliate(affiliate_id):

    affiliate = Affiliate.objects.filter(id=affiliate_id).first()
    vendor_branch = affiliate.vendor_branch
    end_users = EndUser.objects.filter(vendor_branch=vendor_branch, is_delete=False).all()

    end_user_id_list = []
    for end_user in end_users:
        if end_user.attribute_json:
            attribute_dict = json.loads(end_user.attribute_json)
            if "affiliate_id" in attribute_dict:
                if attribute_dict["affiliate_id"] == affiliate_id:
                    end_user_id_list.append(end_user.id)

    return end_user_id_list
