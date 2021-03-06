from django.shortcuts import render, redirect
import datetime
from datetime import timedelta
from django.http import HttpResponse
import json

# import views
from apps.core.views.bot_parts.fbms import end_user_info as fbms_end_user_info
from apps.core.views.bot_parts.line import end_user_info as line_end_user_info

# TODO: change to NEW logic
from apps.core.views.bot_common.start_end_user_story import *

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_line import EndUserLINE
from apps.core.models.end_user_facebook import EndUserFacebook
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.tmp_registration_entry import TmpRegistrationEntry
from apps.core.models.affiliate import Affiliate


def line_entry(request):
    # Access source : URL generated by Vendor Settings
    # e.g. http://0.0.0.0:8888/xxxx/?code=XXXXXXX001

    user_agent = request.META["HTTP_USER_AGENT"]
    x_forwarded_for = request.META["HTTP_X_FORWARDED_FOR"]
    access_dt = datetime.now()
    code = request.GET["code"]
    affiliate_id = request.GET["di"]

    print("[Entry] ================")
    print(user_agent)
    print(x_forwarded_for)
    print(access_dt)
    print(code)
    print(affiliate_id)

    affiliate = Affiliate.objects.filter(id=affiliate_id).first()
    redirect_url = affiliate.vendor_branch.vendor.line_public_url

    tmp_registration_enty = TmpRegistrationEntry()
    tmp_registration_enty.affiliate_id = affiliate_id
    tmp_registration_enty.user_agent = user_agent
    tmp_registration_enty.x_forwarded_for = x_forwarded_for
    tmp_registration_enty.code = code
    tmp_registration_enty.access_dt = access_dt
    tmp_registration_enty.save()

    return redirect(redirect_url)


def fbms_entry(request):
    # Access source : URL generated by Vendor Settings
    # e.g. http://0.0.0.0:8888/xxxx/?code=XXXXXXX001

    user_agent = request.META["HTTP_USER_AGENT"]
    x_forwarded_for = request.META["HTTP_X_FORWARDED_FOR"]
    access_dt = datetime.now()
    code = request.GET["code"]
    affiliate_id = request.GET["di"]

    print("[Entry] ================")
    print(user_agent)
    print(x_forwarded_for)
    print(access_dt)
    print(code)
    print(affiliate_id)

    affiliate = Affiliate.objects.filter(id=affiliate_id).first()
    redirect_url = affiliate.vendor_branch.vendor.fbms_public_url

    print("[Entry] ================")
    print(user_agent)
    print(x_forwarded_for)
    print(access_dt)
    print(code)

    tmp_registration_enty = TmpRegistrationEntry()
    tmp_registration_enty.affiliate_id = affiliate_id
    tmp_registration_enty.user_agent = user_agent
    tmp_registration_enty.x_forwarded_for = x_forwarded_for
    tmp_registration_enty.code = code
    tmp_registration_enty.access_dt = access_dt
    tmp_registration_enty.save()

    return redirect(redirect_url)


def check(request, end_user_id=None):
    # user_id is dynamically set as part of URL
    user_agent = request.META["HTTP_USER_AGENT"]
    x_forwarded_for = request.META["HTTP_X_FORWARDED_FOR"]
    access_dt = datetime.now()
    buffer_min = 3
    access_dt_lt = access_dt - timedelta(minutes=buffer_min)

    end_user = EndUser.objects.filter(id=end_user_id).first()
    affiliates = Affiliate.objects.filter(vendor_branch=end_user.vendor_branch, is_delete=False).all()
    tmp_registration_entry = TmpRegistrationEntry.objects.filter(affiliate__in=affiliates, user_agent=user_agent, x_forwarded_for=x_forwarded_for, is_delete=False, access_dt__range=(access_dt_lt, access_dt)).order_by("-regist_dt").first()

    if not tmp_registration_entry:
        user_agent_part = user_agent[0:25]
        tmp_registration_entry = TmpRegistrationEntry.objects.filter(affiliate__in=affiliates, user_agent__icontains=user_agent_part, x_forwarded_for=x_forwarded_for, is_delete=False, access_dt__range=(access_dt_lt, access_dt)).order_by("-regist_dt").first()

    if tmp_registration_entry:
        print("[Registration] ================")
        print(user_agent)
        print(x_forwarded_for)
        print(access_dt)

        # Retrieve end user
        end_user = EndUser.objects.filter(id=end_user_id).first()

        # Retrive new vendor branch
        new_vendor_branch = VendorBranch.objects.filter(id=tmp_registration_entry.affiliate.vendor_branch.id).first()

        # Retrieve service namespace
        vendor = end_user.vendor_branch.vendor

        service_namespace = "smart_sec"
        if vendor.oem_service_namespace:
            service_namespace = vendor.oem_service_namespace

        context = {
            "new_vendor_branch": new_vendor_branch,
            "tmp_registration_entry": tmp_registration_entry,
            "affiliate": tmp_registration_entry.affiliate,
            "end_user": end_user,
            "namespace": service_namespace
        }

        return render(request, "common/end_user_registration_confirm.html", context)

    else:

        vendor = end_user.vendor_branch.vendor
        end_user_line = EndUserLINE.objects.filter(end_user=end_user, is_delete=False).first()
        end_user_fmbs = EndUserFacebook.objects.filter(end_user=end_user, is_delete=False).first()

        redirect_url = ""

        if end_user_line:
            redirect_url = vendor.line_public_url

        elif end_user_fmbs:
            redirect_url = vendor.fbms_public_url

        context = {
            "message": "Try it again.",
            "redirect_url": redirect_url
        }

        return render(request, "common/close.html", context)


def update_affiliate(request):
    try:
        user_agent = request.META["HTTP_USER_AGENT"]
        tmp_registration_entry_id = int(request.POST["tmp_registration_entry_id"])
        end_user_id = int(request.POST["end_user_id"])
        is_register = int(request.POST["is_register"])

        # Retrieve update data
        tmp_registration_entry = TmpRegistrationEntry.objects.filter(id=tmp_registration_entry_id).first()
        affiliate = tmp_registration_entry.affiliate
        vendor_branch = affiliate.vendor_branch
        end_user = EndUser.objects.filter(id=end_user_id).first()

        # Redirect URL
        end_user_line = EndUserLINE.objects.filter(end_user=end_user, is_delete=False).first()
        end_user_fmbs = EndUserFacebook.objects.filter(end_user=end_user, is_delete=False).first()

        if "FBAV" in user_agent:
            redirect_url = end_user.vendor_branch.vendor.fbms_public_url

        else:
            redirect_url = end_user.vendor_branch.vendor.line_public_url

        context = {
            "message": "Try it again.",
            "redirect_url": redirect_url
        }

        # check if click "Yes"
        if is_register == 1:
            # Update end_user branch
            if vendor_branch and end_user:
                end_user.vendor_branch = vendor_branch
                end_user.save()

                # set end_user attribute
                # set_tag(end_user, tmp_entry)
                end_user.set_attribute_json("affiliate_id", affiliate.id)

                # TODO: send messages
                print("registration completed")

        else:
            if vendor_branch and end_user:
                # TODO: send messages
                print("registration canceled.")

        # Close Page
        context = {
            "message": "Thank you!",
            "redirect_url": redirect_url
        }

        if "FBAV" in user_agent:
            end_user_info = fbms_end_user_info.get_end_user_info(request.path, end_user_fmbs.sender_id)
            end_user_info["platform"] = "fbms"

        else:
            end_user_info = line_end_user_info.get_end_user_info(request.path, end_user_line.user_id)
            end_user_info["platform"] = "line"

        # Delete tmp entry record
        TmpRegistrationEntry.objects.filter(id=tmp_registration_entry_id).delete()

        # Start End User Story
        start_end_user_story("GET_STARTED_PAYLOAD", None, end_user_info)

        return render(request, "common/close.html", context)

    except Exception as e:
        print('%r' % e)

        # Redirect URL
        end_user_line = EndUserLINE.objects.filter(end_user=end_user, is_delete=False).first()
        end_user_fmbs = EndUserFacebook.objects.filter(end_user=end_user, is_delete=False).first()

        if end_user_line:
            redirect_url = end_user.vendor_branch.vendor.line_public_url

        elif end_user_fmbs:
            redirect_url = end_user.vendor_branch.vendor.fbms_public_url

        context = {
            "message": "Try it again.",
            "redirect_url": redirect_url
        }
        return render(request, "common/close.html", context)
