from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.tmp_entry import TmpEntry
from apps.core.models.vendor_branch import VendorBranch


def entry(request):
    # Access source : URL generated by Vendor Settings
    # e.g. http://0.0.0.0:8888/xxxx/?branch_code=001&tag=tagname

    user_agent = request.META["HTTP_USER_AGENT"]
    x_forwarded_for = request.META["HTTP_X_FORWARDED_FOR"]
    access_dt = datetime.datetime.now()
    branch_code = request.GET["branch_code"]
    tag = request.GET["tag"]

    print("[Entry] ================")
    print(user_agent)
    print(x_forwarded_for)
    print(access_dt)
    print(branch_code)
    print(tag)

    tmp_entry = TmpEntry()
    tmp_entry.user_agent = user_agent
    tmp_entry.x_forwarded_for = x_forwarded_for
    tmp_entry.branch_code = branch_code
    tmp_entry.tag_name = tag
    tmp_entry.access_dt = access_dt
    tmp_entry.save()

    # TODO: retrieve LINE URL from DB
    return redirect("https://line.me/R/ti/p/%40cxv4122b")


def check(request, user_id=None):
    # user_id is dynamically set as part of URL
    user_agent = request.META["HTTP_USER_AGENT"]
    x_forwarded_for = request.META["HTTP_X_FORWARDED_FOR"]
    access_dt = datetime.datetime.now()

    buffer_min = 3
    access_dt_lt = access_dt - datetime.timedelta(minutes=buffer_min)
    tmp_entry = TmpEntry.objects.filter(user_agent=user_agent, x_forwarded_for=x_forwarded_for, is_delete=False, access_dt__range=(access_dt_lt, access_dt)).order_by("-regist_dt").first()

    if tmp_entry:
        print("[Registration] ================")
        print(user_agent)
        print(x_forwarded_for)
        print(access_dt)
        print(user_id)

        # Retrieve end user
        end_user = EndUser.objects.filter(id=user_id).first()

        # Retrive new vendor branch
        new_vendor_branch = VendorBranch.objects.filter(id=int(tmp_entry.branch_code)).first()

        # Retrieve service namespace
        vendor = end_user.vendor_branch.vendor
        if vendor.oem_service_namespace:
            service_namespace = vendor.oem_service_namespace
        else:
            service_namespace = vendor.service.name

        context = {
            "new_vendor_branch": new_vendor_branch,
            "tmp_entry_id": tmp_entry.id,
            "end_user": end_user,
            "namespace": service_namespace
        }

        return render(request, "common/line_registration.html", context)

    else:

        context = {
            "message": "申し訳ございません。もう一度最初からご確認ください。",
            "line_url": "https://line.me/R/ti/p/%40cxv4122b"
        }

        return render(request, "common/close.html", context)