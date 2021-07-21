# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# import models
from apps.qa.models.vendor_business_partner import VendorBusinessPartner
from apps.qa.models.vendor_business_partner_tag import VendorBusinessPartnerTag

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects


@login_required(login_url='/qa/')
def list(request):
    """ Dashboard Index """
    user_obj = get_login_user_objects(request)

    bps = VendorBusinessPartner.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()
    bp_tags = VendorBusinessPartnerTag.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id,
                                                      is_delete=False).all()

    context = {
        "bps": bps,
        "bp_tags": bp_tags,
        "title": "Business Partner",
        "namespace": user_obj["service_namespace"],
    }

    return render(request, "vendor/business_partner/bp_list.html", context)


@login_required(login_url='/qa/')
def edit(request, bp_id=None):
    """ BP Editor """
    user_obj = get_login_user_objects(request)
    bp_tags = VendorBusinessPartnerTag.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id,
                                                      is_delete=False).all()
    bp_detail = {
        "zip_code": None,
        "tel1": None,
        "tel2": None,
        "fax": None,
    }

    if request.POST:
        bp = VendorBusinessPartner.objects.filter(id=bp_id).first()
        try:
            vendor_id = user_obj["vendor_branch"].vendor.id
            bp.vendor_id = vendor_id

            if "name" in request.POST:
                bp.name = request.POST["name"]

            if "short_name" in request.POST:
                bp.short_name = request.POST["short_name"]

            if "name_kana" in request.POST:
                bp.name_kana = request.POST["name_kana"]

            if "email" in request.POST:
                bp.email = request.POST["email"]

            if "zip_code_1" in request.POST and "zip_code_2" in request.POST:
                bp.zip_code = request.POST["zip_code_1"] + "-" + request.POST["zip_code_2"]

            if "prefecture" in request.POST:
                bp.prefecture = request.POST["prefecture"]

            if "address1" in request.POST:
                bp.address1 = request.POST["address1"]

            if "address2" in request.POST:
                bp.address2 = request.POST["address2"]

            if "tel1_1" in request.POST and "tel1_2" in request.POST and "tel1_3" in request.POST:
                bp.tel1 = request.POST["tel1_1"] + "-" + request.POST["tel1_2"] + "-" + request.POST["tel1_3"]

            if "tel2_1" in request.POST and "tel2_2" in request.POST and "tel2_3" in request.POST:
                bp.tel2 = request.POST["tel2_1"] + "-" + request.POST["tel2_2"] + "-" + request.POST["tel2_3"]

            if "fax1" in request.POST and "fax2" in request.POST and "fax3" in request.POST:
                bp.fax = request.POST["fax1"] + "-" + request.POST["fax2"] + "-" + request.POST["fax3"]

            if "memo" in request.POST:
                bp.memo = request.POST["memo"]

            # Get bp_tag list
            bp_tag_list = request.POST.getlist("bp_tag")
            bp_tag_str = ",".join(bp_tag_list)
            bp.tag_csv = bp_tag_str

            bp.save()
            redirect_url = "/" + user_obj["service_url"] + "/bp/list/"
            return redirect(redirect_url)

        except Exception as e:
            print("ERROR:" + str(e))

    else:
        bp = VendorBusinessPartner.objects.filter(id=bp_id).first()

        if bp:
            if bp.zip_code:
                zip_code_list = bp.zip_code.split("-")
                if len(zip_code_list) == 2:
                    bp_detail["zip_code"] = zip_code_list

            if bp.tel1:
                tel1_list = bp.tel1.split("-")
                if len(tel1_list) == 3:
                    bp_detail["tel1"] = tel1_list

            if bp.tel2:
                tel2_list = bp.tel2.split("-")
                if len(tel2_list) == 3:
                    bp_detail["tel2"] = tel2_list

            if bp.fax:
                fax_list = bp.fax.split("-")
                if len(fax_list) == 3:
                    bp_detail["fax"] = fax_list

    context = {
        "title": "BP Editor",
        "bp": bp,
        "bp_tags": bp_tags,
        "bp_detail": bp_detail,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/business_partner/bp_detail.html", context)


@login_required(login_url='/qa/')
def add(request):
    """ Add BP """
    user_obj = get_login_user_objects(request)

    try:
        bp = VendorBusinessPartner()
        vendor_id = user_obj["vendor_branch"].vendor.id
        bp.vendor_id = vendor_id

        if "name" in request.POST:
            bp.name = request.POST["name"]

        if "short_name" in request.POST:
            bp.short_name = request.POST["short_name"]

        if "name_kana" in request.POST:
            bp.name_kana = request.POST["name_kana"]

        if "email" in request.POST:
            bp.email = request.POST["email"]

        if "zip_code_1" in request.POST and "zip_code_2" in request.POST:
            bp.zip_code = request.POST["zip_code_1"] + "-" + request.POST["zip_code_2"]

        if "prefecture" in request.POST:
            bp.prefecture = request.POST["prefecture"]

        if "address1" in request.POST:
            bp.address1 = request.POST["address1"]

        if "address2" in request.POST:
            bp.address2 = request.POST["address2"]

        if "tel1_1" in request.POST and "tel1_2" in request.POST and "tel1_3" in request.POST:
            bp.tel1 = request.POST["tel1_1"] + "-" + request.POST["tel1_2"] + "-" + request.POST["tel1_3"]

        if "tel2_1" in request.POST and "tel2_2" in request.POST and "tel2_3" in request.POST:
            bp.tel2 = request.POST["tel2_1"] + "-" + request.POST["tel2_2"] + "-" + request.POST["tel2_3"]

        if "fax1" in request.POST and "fax2" in request.POST and "fax3" in request.POST:
            bp.fax = request.POST["fax1"] + "-" + request.POST["fax2"] + "-" + request.POST["fax3"]

        if "memo" in request.POST:
            bp.memo = request.POST["memo"]

        # Get bp_tag list
        bp_tag_list = request.POST.getlist("bp_tag")
        bp_tag_str = ",".join(bp_tag_list)
        bp.tag_csv = bp_tag_str

        bp.save()

    except Exception as e:
        print("ERROR:" + str(e))

    redirect_url = "/" + user_obj["service_url"] + "/bp/list/"
    return redirect(redirect_url)


def delete(request, bp_id):
    """ Delete BP"""

    user_obj = get_login_user_objects(request)

    bp = VendorBusinessPartner.objects.filter(id=bp_id).first()
    bp.is_delete = True
    bp.save()

    redirect_url = "/" + user_obj["service_url"] + "/bp/list/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def tag_list(request):
    """ Tag list """
    user_obj = get_login_user_objects(request)

    bp_tags = VendorBusinessPartnerTag.objects.filter(vendor_id=user_obj["vendor_branch"].vendor.id, is_delete=False).all()

    context = {
        "bp_tags": bp_tags,
        "title": "Business Partner Tag",
        "namespace": user_obj["service_namespace"],
    }

    return render(request, "vendor/business_partner/bp_tag_list.html", context)


@login_required(login_url='/qa/')
def tag_edit(request, bp_tag_id=None):
    """ BP Editor """
    user_obj = get_login_user_objects(request)

    if request.POST:
        bp_tag = VendorBusinessPartnerTag.objects.filter(id=bp_tag_id).first()
        bp_tag.name = request.POST["name"]
        bp_tag.save()

        redirect_url = "/" + user_obj["service_url"] + "/bp/tag/list/"
        return redirect(redirect_url)

    else:
        bp_tag = VendorBusinessPartnerTag.objects.filter(id=bp_tag_id).first()

    context = {
        "title": "BP Tag Editor",
        "bp_tag": bp_tag,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/business_partner/bp_tag_detail.html", context)


@login_required(login_url='/qa/')
def tag_add(request):
    """ Add BP Tag """
    user_obj = get_login_user_objects(request)
    bp_tag = VendorBusinessPartnerTag()
    bp_tag.vendor_id = user_obj["vendor_branch"].vendor.id
    bp_tag.name = request.POST["name"]
    bp_tag.save()
    bp_tag.cd = str(user_obj["vendor_branch"].vendor.id) + "_" + str(bp_tag.id)
    bp_tag.save()

    redirect_url = "/" + user_obj["service_url"] + "/bp/tag/list/"
    return redirect(redirect_url)


def tag_delete(request, bp_tag_id):
    """ Delete BP"""

    user_obj = get_login_user_objects(request)
    bp_tag = VendorBusinessPartnerTag.objects.filter(id=bp_tag_id).first()
    bp_tag.is_delete = True
    bp_tag.save()

    redirect_url = "/" + user_obj["service_url"] + "/bp/tag/list/"
    return redirect(redirect_url)
