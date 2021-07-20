from django.shortcuts import render, redirect
import datetime
from django.conf import settings
from django.http import HttpResponse

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_line import EndUserLINE
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.tmp_registration_entry import TmpRegistrationEntry
from apps.core.models.affiliate import Affiliate

# import views
from apps.core.views.messaging_adapter_chat.text_send_message import *
from apps.core.views.messaging_adapter_chat.carousel_send_message import *


def get_tmp_registration_entry(request, end_user_info):
    # user_id is dynamically set as part of URL
    user_agent = request.META["HTTP_USER_AGENT"]
    x_forwarded_for = request.META["HTTP_X_FORWARDED_FOR"]
    access_dt = datetime.datetime.now()

    buffer_min = 0.4
    access_dt_lt = access_dt - datetime.timedelta(minutes=buffer_min)
    # tmp_registration_entry = TmpRegistrationEntry.objects.filter(user_agent=user_agent, x_forwarded_for=x_forwarded_for, is_delete=False, access_dt__range=(access_dt_lt, access_dt)).order_by("-regist_dt").first()

    affiliates = Affiliate.objects.filter(vendor_branch=end_user_info["vendor_branch"], is_delete=False).all()
    affiliate_id_list = []
    for affiliate in affiliates:
        affiliate_id_list.append(affiliate.id)

    # TODO: どうやってより正しくTmpを判定するか・・
    print(affiliate_id_list)
    tmp_registration_entry = TmpRegistrationEntry.objects.filter(affiliate_id__in=affiliate_id_list, is_delete=False, access_dt__range=(access_dt_lt, access_dt)).order_by("-regist_dt").first()

    return tmp_registration_entry


def send_welcome_message(end_user_info):
    end_user = end_user_info["end_user_obj"]
    service_name = end_user.vendor_branch.vendor.service.name

    # Create Registration URL
    registration_check_url = "/" + service_name + "/registration/check/" + str(end_user.id) + "/" + "?openExternalBrowser=1"
    if settings.MODE == "LOCAL":
        registration_url = settings.ROOT_URL_PUBLIC + registration_check_url
    else:
        registration_url = settings.ROOT_URL + registration_check_url

    param = {
         "elements": [
                 {
                     "title": "Registration",
                     "url":  registration_url,
                     "image_url": settings.LINE_DEFAULT_IMG_URL,
                     "subtitle": "User Registration",
                     "buttons": [
                         {
                             "type": "url",
                             "title": "Registration Now!",
                             "data": registration_url
                         }
                     ]
                 }
             ]
        }

    carousel_send_message(end_user_info, param)

    param = {
        "text": "test！"
    }

    text_send_message(end_user_info, param)
