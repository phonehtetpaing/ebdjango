# -*- coding: utf-8 -*-
from django.conf import settings as conf_settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# import models
from apps.qa.models.vendor_user import VendorUser as CQVendorUser
from apps.qa.models.senbay_user import SenbayUser

# import views
from apps.core.views.vendor_common.login_user_info import *

# import api request util
from apps.qa.views.senbay_api.base import request_get, request_post, request_delete


@login_required(login_url='/qa/')
def index(request):
    """ Reservations """
    user_obj = get_login_user_objects(request)

    context = {
        "title": "Reservations",
        "namespace": "qa"
    }

    return render(request, "vendor/reservation/reservation.html", context)


@login_required(login_url='/qa/')
def settings(request):
    """ Reservations Settings"""
    # Get Senby User
    vendor_user = CQVendorUser.objects.filter(auth_user=request.user).first()
    senbay_user = SenbayUser.objects.filter(vendor_user_id=vendor_user.id, is_active=True).first()

    if "token" in request.GET and "sbid" in request.GET and "vuid" in request.GET:
        # Senbay Integration
        print("Senbay Integration....")
        print(request.GET["token"])
        token = request.GET["token"]
        sbid = request.GET["sbid"]
        vuid = request.GET["vuid"]

        if request.user.id == int(vuid):

            senbay_user = SenbayUser.objects.filter(id=sbid).first()

            if token != "error":
                senbay_user.jwt_token = token
                senbay_user.is_active = True

                try:
                    senbay_user.save()
                except Exception as e:
                    print("ERROR: saving...")
                    print(request.user.id)
                    print(vendor_user.id)
                    print(token)
                    print('%r' % e)

    context = request_get(request, "team_detail", None, None)

    if context is None:
        context = dict()
        if not senbay_user:
            senbay_user = SenbayUser()
            senbay_user.vendor_user_id = vendor_user.id
        senbay_user.is_active = False
        senbay_user.save()

    senbay_login_url = conf_settings.SENBAY_LOGIN_URL + "?qa=1&sbid=" + str(senbay_user.id) + "&vuid=" + str(request.user.id)

    context["senbay_user"] = senbay_user
    context["senbay_login_url"] = senbay_login_url
    context["title"] = "Reservations"
    context["namespace"] = "qa"

    return render(request, "vendor/reservation/settings.html", context)


@login_required(login_url='/qa/')
def update_team_setting(request):

    context = request_post(request, "team_detail", request.POST)

    return redirect("/qa/reservation/settings")


@login_required(login_url='/qa/')
def template_list(request):

    context = request_get(request, "template", None, None)
    if context is None:
        context = dict()

    context["title"] = "Schedule List"
    context["namespace"] = "qa"

    return render(request, "vendor/reservation/template_list.html", context)


@login_required(login_url='/qa/')
def template_once(request):

    context = request_get(request, "get_template_once", None, None)
    context["title"] = "One Time URL"
    context["namespace"] = "qa"

    return render(request, "vendor/reservation/template_detail.html", context)


@login_required(login_url='/qa/')
def template_create_once(request):

    context = request_post(request, "create_template_once", request.POST)
    context["title"] = "One Time URL"
    context["namespace"] = "qa"

    return render(request, "vendor/reservation/created_once_url.html", context)


@login_required(login_url='/qa/')
def template_detail(request, template_id=None):
    if template_id is None:
        context = request_post(request, "template", None)

    else:
        context = request_get(request, "template", None, template_id)

    context["template_id"] = template_id
    context["title"] = "Schedule Edit"
    context["namespace"] = "qa"
    return render(request, "vendor/reservation/template_detail.html", context)


@login_required(login_url='/qa/')
def template_add(request):

    context = request_post(request, "add_template", request.POST)
    context["title"] = "Schedule Edit"
    context["namespace"] = "qa"

    return redirect("/qa/reservation/template/list/")


@login_required(login_url='/qa/')
def template_edit(request, template_id):
    request_post(request, "add_template", request.POST)
    request_delete(request, "template", template_id)

    return redirect("/qa/reservation/template/list/")


@login_required(login_url='/qa/')
def template_delete(request, template_id=None):

    context = request_delete(request, "template", template_id)
    context["title"] = "Schedule List"
    context["namespace"] = "qa"

    return redirect("/qa/reservation/template/list/")


@login_required(login_url='/qa/')
def account_detail(request):
    context = request_get(request, "account", None, None)
    if context is None:
        context = dict()
    context["title"] = "Account Edit"
    context["namespace"] = "qa"
    return render(request, "vendor/reservation/account.html", context)


@login_required(login_url='/qa/')
def update_account_setting(request):
    context = request_post(request, "account", request.POST)
    context["title"] = "Account UPDATE"
    context["namespace"] = "qa"
    messages.success(request, 'アカウント設定を保存しました。')

    return render(request, "vendor/reservation/account.html", context)


@login_required(login_url='/qa/')
def schedule_now_list(request):

    context = request_get(request, "get_schedule_now_list", None, None)
    if context is None:
        context = dict()

    context["title"] = "Schedule List"
    context["namespace"] = "qa"

    return render(request, "vendor/reservation/schedule_list.html", context)


@login_required(login_url='/qa/')
def schedule_past_list(request):

    context = request_get(request, "get_schedule_past_list", None, None)
    context["title"] = "Schedule Past List"
    context["namespace"] = "qa"

    return render(request, "vendor/reservation/schedule_list.html", context)


@login_required(login_url='/qa/')
def schedule_delete(request, schedule_history_id=None, mode_menu=None):
    data = {
        "schedule_history_id": schedule_history_id,
        "mode_menu": mode_menu,
    }

    context = request_post(request, "delete_schedule", data)

    if mode_menu == "now":
        context = request_get(request, "get_schedule_now_list", None, None)
    else:
        context = request_get(request, "get_schedule_past_list", None, None)

    context["title"] = "Schedule List"
    context["namespace"] = "qa"

    messages.success(request, 'スケジュール履歴を削除しました。')

    return render(request, "vendor/reservation/schedule_list.html", context)
