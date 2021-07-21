# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# import models
from apps.qa.models.product_category import ProductCategory

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects


@login_required(login_url='/qa/')
def list(request):
    """ Product Category List """
    user_obj = get_login_user_objects(request)

    product_categories = ProductCategory.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()

    context = {
        "product_categories": product_categories,
        "title": "Product Category",
        "namespace": user_obj["service_namespace"],
    }

    return render(request, "vendor/product/product_category_list.html", context)


@login_required(login_url='/qa/')
def edit(request, pc_id=None):
    """ Product Category Editor """
    user_obj = get_login_user_objects(request)

    if request.POST:
        product_category = ProductCategory.objects.filter(id=pc_id).first()
        product_category.name = request.POST["name"]
        if "memo" in request.POST:
            product_category.memo = request.POST["memo"]
        product_category.save()

        redirect_url = "/" + user_obj["service_url"] + "/product/category/list/"
        return redirect(redirect_url)

    else:
        product_category = ProductCategory.objects.filter(id=pc_id).first()

    context = {
        "title": "Product Category Editor",
        "pc": product_category,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/product/product_category_detail.html", context)


@login_required(login_url='/qa/')
def add(request):
    """ Add Product Category """
    user_obj = get_login_user_objects(request)

    try:
        pc = ProductCategory()
        vendor_id = user_obj["vendor_branch"].vendor.id
        pc.vendor_id = vendor_id
        pc.name = request.POST["name"]
        if "memo" in request.POST:
            pc.memo = request.POST["memo"]
        pc.save()

    except Exception as e:
       print("ERROR:" + str(e))

    redirect_url = "/" + user_obj["service_url"] + "/product/category/list/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def delete(request, pc_id):
    """ Delete Product Category"""

    user_obj = get_login_user_objects(request)

    pc = ProductCategory.objects.filter(id=pc_id).first()
    pc.is_delete = True
    pc.save()

    redirect_url = "/" + user_obj["service_url"] + "/product/category/list/"
    return redirect(redirect_url)
