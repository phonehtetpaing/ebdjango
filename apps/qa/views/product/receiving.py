# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import datetime

# import models
from apps.qa.models.product_category import ProductCategory
from apps.qa.models.stock_space import StockSpace
from apps.qa.models.product import Product
from apps.qa.models.stock import Stock
from apps.qa.models.vendor_business_partner import VendorBusinessPartner
from apps.qa.models.receiving_history import ReceivingHistory


# import views
from apps.qa.views.common.login_user_info import get_login_user_objects


@login_required(login_url='/qa/')
def entry(request):
    """ Receiving Entry """
    user_obj = get_login_user_objects(request)

    bps = VendorBusinessPartner.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()
    product_categories = ProductCategory.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id,is_delete=False).all()
    products = Product.objects.filter(product_category__in=product_categories, is_delete=False).all()

    context = {
        "title": "Receiving Entry",
        "products": products,
        "bps": bps,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/product/receiving_detail.html", context)


@login_required(login_url='/qa/')
def add(request):
    """ Add Stock """
    user_obj = get_login_user_objects(request)

    try:
        rh = ReceivingHistory()
        rh.product_id =  int(request.POST["product"])
        rh.business_partner_id = int(request.POST["bp"])
        rh.quantity = int(request.POST["quantity"])
        rh.price = int(request.POST["price"])
        rh.issue_number = request.POST["issue_number"]
        rh.track_number = request.POST["track_number"]
        scheduled_dt = datetime.strptime(request.POST["scheduled_dt"], '%Y-%m-%d')
        rh.scheduled_dt = scheduled_dt
        rh.memo = request.POST["memo"]
        rh.save()

        # add quantity to stock
        stock = Stock.objects.filter(product_id=rh.product_id, is_delete=False).first()

        if stock:
            quantity = stock.quantity + rh.quantity
            stock.quantity = quantity
            stock.save()

        else:
            stock = Stock()
            stock.product_id = rh.product_id
            stock.quantity = rh.quantity
            stock.save()

    except Exception as e:
        print("ERROR:" + str(e))

    redirect_url = "/" + user_obj["service_url"] + "/receiving/history/list/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def history_list(request):
    """ Receiving History List """
    user_obj = get_login_user_objects(request)

    bps = VendorBusinessPartner.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()
    product_categories = ProductCategory.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id,is_delete=False).all()
    products = Product.objects.filter(product_category__in=product_categories, is_delete=False).all()
    receiving_histories = ReceivingHistory.objects.filter(product__in=products, is_delete=False).order_by("-update_dt").all()

    context = {
        "title": "Receiving History",
        "receiving_histories": receiving_histories,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/product/receiving_history_list.html", context)


@login_required(login_url='/qa/')
def history_detail(request, history_id=None):
    """ Receiving History Detail """

    user_obj = get_login_user_objects(request)

    if history_id is None:
        redirect_url = "/" + user_obj["service_url"] + "/receiving/history/list/"
        return redirect(redirect_url)

    receiving_history = ReceivingHistory.objects.filter(id=history_id).first()

    context = {
        "title": "Receiving History Detail",
        "rh": receiving_history,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/product/receiving_history_detail.html", context)
