# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# import models
from apps.qa.models.product_category import ProductCategory
from apps.qa.models.stock_space import StockSpace
from apps.qa.models.product import Product
from apps.qa.models.stock import Stock


# import views
from apps.qa.views.common.login_user_info import get_login_user_objects


@login_required(login_url='/qa/')
def list(request):
    """ Stock List """
    user_obj = get_login_user_objects(request)
    product_categories = ProductCategory.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()
    products = Product.objects.filter(product_category__in=product_categories, is_delete=False).all()
    stocks = Stock.objects.filter(product__in=products, is_delete=False).all()

    context = {
        "stocks": stocks,
        "title": "Stock",
        "namespace": user_obj["service_namespace"],
    }

    return render(request, "vendor/product/stock_list.html", context)


@login_required(login_url='/qa/')
def edit(request, stock_id=None):
    """ Product Editor """
    user_obj = get_login_user_objects(request)
    product_categories = ProductCategory.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id,is_delete=False).all()
    spaces = StockSpace.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()
    all_products = Product.objects.filter(product_category__in=product_categories, is_delete=False).all()
    stocks = Stock.objects.filter(product__in=all_products, is_delete=False).all()
    # Get exsisting product id
    stock_product_id_list = []
    for stock in stocks:
        stock_product_id_list.append(stock.product.id)

    products = Product.objects.filter(product_category__in=product_categories, is_delete=False).exclude(id__in=stock_product_id_list).all()

    if request.POST:
        stock = Stock.objects.filter(id=stock_id).first()
        stock.product_id = int(request.POST["product"])
        stock.quantity = int(request.POST["quantity"])
        if "memo" in request.POST:
            stock.memo = request.POST["memo"]
        stock.save()

        redirect_url = "/" + user_obj["service_url"] + "/stock/list/"
        return redirect(redirect_url)

    else:
        stock = Stock.objects.filter(id=stock_id).first()

    context = {
        "title": "Product Editor",
        "products": products,
        "spaces": spaces,
        "stock": stock,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/product/stock_detail.html", context)


@login_required(login_url='/qa/')
def add(request):
    """ Add Stock """
    user_obj = get_login_user_objects(request)

    try:
        stock = Stock()
        stock.product_id = int(request.POST["product"])
        stock.quantity = int(request.POST["quantity"])
        if "memo" in request.POST:
            stock.memo = request.POST["memo"]
        stock.save()

    except Exception as e:
       print("ERROR:" + str(e))

    redirect_url = "/" + user_obj["service_url"] + "/stock/list/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def delete(request, stock_id):
    """ Delete Stock """

    user_obj = get_login_user_objects(request)

    stock = Stock.objects.filter(id=stock_id).first()
    stock.is_delete = True
    stock.save()

    redirect_url = "/" + user_obj["service_url"] + "/stock/list/"
    return redirect(redirect_url)
