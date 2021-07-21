# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# import models
from apps.qa.models.product_category import ProductCategory
from apps.qa.models.stock_space import StockSpace
from apps.qa.models.product import Product

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects


@login_required(login_url='/qa/')
def list(request):
    """ Product List """
    user_obj = get_login_user_objects(request)
    product_categories = ProductCategory.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()
    products = Product.objects.filter(product_category__in=product_categories, is_delete=False).all()

    context = {
        "products": products,
        "title": "Product",
        "namespace": user_obj["service_namespace"],
    }

    return render(request, "vendor/product/product_list.html", context)


@login_required(login_url='/qa/')
def edit(request, product_id=None):
    """ Product Editor """
    user_obj = get_login_user_objects(request)
    product_categories = ProductCategory.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id,
                                                        is_delete=False).all()
    spaces = StockSpace.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()

    if request.POST:
        product = Product.objects.filter(id=product_id).first()
        product.name = request.POST["name"]
        product.product_category_id = int(request.POST["product_category"])
        if "stock_space" in request.POST:
            product.stock_space_id = int(request.POST["stock_space"])
        if "code" in request.POST:
            product.code = request.POST["code"]
        if "sales_price" in request.POST:
            product.sales_price = int(request.POST["sales_price"])
        if "receiving_price" in request.POST:
            product.receiving_price = int(request.POST["receiving_price"])
        if "memo" in request.POST:
            product.memo = request.POST["memo"]
        product.save()

        redirect_url = "/" + user_obj["service_url"] + "/product/list/"
        return redirect(redirect_url)

    else:
        product = Product.objects.filter(id=product_id).first()

    context = {
        "title": "Product Editor",
        "product_categories": product_categories,
        "spaces": spaces,
        "product": product,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/product/product_detail.html", context)


@login_required(login_url='/qa/')
def add(request):
    """ Add Product """
    user_obj = get_login_user_objects(request)

    try:
        product = Product()
        product.name = request.POST["name"]
        product.product_category_id = int(request.POST["product_category"])
        if "stock_space" in request.POST:
            product.stock_space_id = int(request.POST["stock_space"])
        if "code" in request.POST:
            product.code = request.POST["code"]
        if "sales_price" in request.POST and request.POST["sales_price"] != "":
            product.sales_price = int(request.POST["sales_price"])
        if "receiving_price" in request.POST and request.POST["receiving_price"] != "":
            product.receiving_price = int(request.POST["receiving_price"])
        if "memo" in request.POST:
            product.memo = request.POST["memo"]
        product.save()

    except Exception as e:
        print("ERROR:" + str(e))

    redirect_url = "/" + user_obj["service_url"] + "/product/list/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def delete(request, product_id):
    """ Delete Product """

    user_obj = get_login_user_objects(request)

    product = Product.objects.filter(id=product_id).first()
    product.is_delete = True
    product.save()

    redirect_url = "/" + user_obj["service_url"] + "/product/list/"
    return redirect(redirect_url)
