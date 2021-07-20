from django.shortcuts import render, redirect

# import models
from apps.core.models.manual_message_overview import ManualMessageOverview


# import views
from apps.core.views.vendor_common.messsage_tagged_user import *


def index(request):

    context = {
    }

    return render(request, "samples/index.html", context)


def send_message_test(request):
    print("TESTTESTTEST")

    tag_id_list = [1,2,3]
    manual_message_overview = ManualMessageOverview.objects.filter(id=1).first()
    vendor_branch_id_list = [1]

    send_message_to_tagged_user(request, tag_id_list, manual_message_overview, vendor_branch_id_list, True)

    return redirect("/smartsec/dashboard/")


def entry_recome(request):
    user_agent = request.META["HTTP_USER_AGENT"]
    x_forwarded_for = request.META["HTTP_X_FORWARDED_FOR"]
    access_dt = datetime.datetime.now()
    branch_code = request.GET["branch_code"]
    tag = request.GET["tag"]
    registration_url = "/entry/registration/?branch_code=" + branch_code

    print("[Entry] ================")
    print(user_agent)
    print(x_forwarded_for)
    print(access_dt)
    print(branch_code)
    print(tag)
    print(registration_url)

    return redirect("https://line.me/R/ti/p/%40fvs9942t")


def entry_check_recome(request):
    # user_id is dynamically set as part of URL
    user_agent = request.META["HTTP_USER_AGENT"]
    x_forwarded_for = request.META["HTTP_X_FORWARDED_FOR"]
    access_dt = datetime.datetime.now()
    user_id = request.GET["user_id"]

    print("[Registration] ================")
    print(user_agent)
    print(x_forwarded_for)
    print(access_dt)
    print(user_id)
    print("send message")

    # change user status ?

    return redirect("/sample/index/")


def botui_helloworld(request):

    context = {
    }

    return render(request, "samples/botui/botui_helloworld.html", context)