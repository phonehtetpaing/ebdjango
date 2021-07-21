# -*- coding: utf-8 -*-
from django.utils import timezone
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

# import models
from apps.core.models import Vendor
from apps.qa.models.coupon import Coupon
from apps.qa.models.coupon_type import CouponType
from apps.qa.models.questionnaire import Questionnaire

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects

# import forms
from apps.qa.forms.coupon import CouponForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='/qa/')
def edit(request, coupon_id=None):
    """ Coupon Editor """
    user_obj = get_login_user_objects(request)

    selected_coupon = Coupon.objects.filter(id=coupon_id, vendor_branch=user_obj["vendor_branch"]).first()
    coupons = sorted(Coupon.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=0).all(), key=lambda t: t.status(), reverse=True)
    questionnaires = Questionnaire.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=0).all()

    page = request.GET.get('page', 1)
    paginator = Paginator(coupons, 5)
    try:
        coupons = paginator.page(page)
    except PageNotAnInteger:
        coupons = paginator.page(1)
    except EmptyPage:
        coupons = paginator.page(paginator.num_pages)

    if request.POST:
        form = CouponForm(request.POST, instance=selected_coupon)
        if form.is_valid():
            selected_coupon = form.save(commit=False)
            selected_coupon.update_dt = timezone.now()
            # coupon.style = format_style(request.POST)
            selected_coupon.data = format_data(request.POST)
            selected_coupon.save()
    else:
        form = CouponForm(instance=selected_coupon)

    context = {
        "title": "Coupon Editor",
        "coupons": coupons,
        "selected_coupon": selected_coupon,
        "questionnaires": questionnaires,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/coupon/coupon_editor.html", context)


@login_required(login_url='/qa/')
def add(request):
    """ Add Coupon """
    user_obj = get_login_user_objects(request)

    text_type = CouponType.objects.filter(name="text").first()
    coupon = Coupon(vendor_branch=user_obj["vendor_branch"], type=text_type)
    coupon.save()

    redirect_url = "/" + user_obj["service_url"] + "/coupon/" + str(coupon.id) + "/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def delete(request, coupon_id=None):
    """ Delete Coupon """
    user_obj = get_login_user_objects(request)

    selected_coupon = Coupon.objects.filter(id=coupon_id, vendor_branch=user_obj["vendor_branch"]).first()
    selected_coupon.is_delete = 1
    selected_coupon.save()

    redirect_url = "/" + user_obj["service_url"] + "/coupon/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def print_coupon(request, coupon_id=None):
    """ Coupon Editor """
    user_obj = get_login_user_objects(request)

    selected_coupon = Coupon.objects.filter(id=coupon_id, vendor_branch=user_obj["vendor_branch"]).first()

    context = {
        "title": "Coupon Print",
        "selected_coupon": selected_coupon,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/coupon/coupon_print.html", context)


def claim(request, coupon_id=None):
    coupon = Coupon.objects.filter(id=coupon_id, is_delete=0).first()
    vendor = coupon.vendor_branch.vendor
    # todo add analytics tracking

    # display error page for unknown/invalid coupons
    if not coupon:
        return render(request, "vendor/coupon/coupon_claim.html", {
            "title": "Coupon Claims",
            "coupon_message": "Sorry that coupon can't be found!",
        })

    # take appropriate action depending on coupon type
    if coupon.type.name == 'url':
        return redirect(coupon.data)
    elif coupon.type.name == 'questionnaire':
        questionnaire_id = coupon.data
        questionnaire_url = "{0}v2/form/{1}/{2}/".format(settings.CONTACTCHAT_BASE_URL, vendor.contactchat_access_url_part, questionnaire_id)
        return redirect(questionnaire_url)
    else:
        return render(request, "vendor/coupon/coupon_claim.html", {
            "title": "Coupon Claims",
            "coupon_message": coupon.data,
        })


def format_style(post_data):
    output = {"bgcolor": post_data['couponcolor'], "txtcolor": "#ffffff"}
    return output


def format_data(post_data):
    # text type
    if post_data.get('type') == 'text':
        return post_data.get('inputtext')
    # url redirect type
    if post_data.get('type') == 'url':
        return post_data.get('inputurl')
    if post_data.get('type') == 'questionnaire':
        return post_data.get('questionnaire')
    else:
        return 'empty'
