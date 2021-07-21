# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# import models
from apps.qa.models.stock_space import StockSpace

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects


@login_required(login_url='/qa/')
def list(request):
    """ Stock Space List """
    user_obj = get_login_user_objects(request)

    spaces = StockSpace.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()

    context = {
        "spaces": spaces,
        "title": "Stock Stapce",
        "namespace": user_obj["service_namespace"],
    }

    return render(request, "vendor/product/space_list.html", context)


@login_required(login_url='/qa/')
def edit(request, ss_id=None):
    """ Stock Space Editor """
    user_obj = get_login_user_objects(request)

    if request.POST:
        space = StockSpace.objects.filter(id=ss_id).first()
        space.name = request.POST["name"]
        if "memo" in request.POST:
            space.memo = request.POST["memo"]
        space.save()

        redirect_url = "/" + user_obj["service_url"] + "/product/space/list/"
        return redirect(redirect_url)

    else:
        space = StockSpace.objects.filter(id=ss_id).first()

    context = {
        "title": "Stock Space Editor",
        "ss": space,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/product/space_detail.html", context)


@login_required(login_url='/qa/')
def add(request):
    """ Add Stock Space """
    user_obj = get_login_user_objects(request)

    try:
        ss = StockSpace()
        vendor_id = user_obj["vendor_branch"].vendor.id
        ss.vendor_id = vendor_id
        ss.name = request.POST["name"]
        if "memo" in request.POST:
            ss.memo = request.POST["memo"]
        ss.save()

    except Exception as e:
       print("ERROR:" + str(e))

    redirect_url = "/" + user_obj["service_url"] + "/product/space/list/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def delete(request, ss_id):
    """ Delete Stock Space """

    user_obj = get_login_user_objects(request)

    ss = StockSpace.objects.filter(id=ss_id).first()
    ss.is_delete = True
    ss.save()

    redirect_url = "/" + user_obj["service_url"] + "/product/space/list/"
    return redirect(redirect_url)
