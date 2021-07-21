import ast
import json

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# import models
from apps.qa.models.vendor_plan import VendorPlan
from apps.qa.models.plan import Plan
from apps.qa.models.notification_service import NotificationService
from apps.qa.models.notification_setting import NotificationSetting
from apps.core.models.vendor import Vendor

# import forms
from apps.qa.forms.vendor import VendorUserForm
from apps.qa.forms.vendor import VendorSettingsForm

# import views
from apps.qa.views.common.login_user_info import *

from apps.qa.views.utilities.s3_file_manager import save_css, save_static_text, create_contactchat_css, read_static_text


@login_required(login_url='/qa/')
def profile(request):
    """ Plan Settings """
    user_obj = get_login_user_objects(request)
    vendor_user = user_obj["vendor_user"]
    vendor = user_obj["vendor_branch"].vendor
    if request.POST:
        form = VendorUserForm(request.POST, instance=user_obj["vendor_user"])
        vendor_info_form = VendorSettingsForm(request.POST, request.FILES, instance=user_obj["vendor_branch"].vendor)
        if form.is_valid() and vendor_info_form.is_valid():
            form.save()
            vendor_info_form.save()
    else:
        form = VendorUserForm(instance=user_obj["vendor_user"])
        vendor_info_form = VendorSettingsForm(instance=user_obj["vendor_branch"].vendor)

    context = {
        "title": "Profile Settings",
        "form": form,
        "vendor_info_form": vendor_info_form,
        "vendor_user": vendor_user,
        "vendor": vendor,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings/profile.html", context)


@login_required(login_url='/qa/')
def plan(request):
    """ Plan Settings """
    user_obj = get_login_user_objects(request)

    vendor = user_obj["vendor_branch"].vendor
    vendor_plan = VendorPlan.objects.filter(vendor=vendor).first()
    plans = Plan.objects.all()

    context = {
        "title": "Plan Settings",
        "namespace": user_obj["service_namespace"],
        "active_plan": vendor_plan,
        "plans": plans
    }

    return render(request, "vendor/settings/plan.html", context)


@login_required(login_url='/qa/')
def notification(request, service_id=1):
    """ Notification Settings """
    user_obj = get_login_user_objects(request)
    notification_services = NotificationSetting.objects.filter(vendor_user=user_obj["vendor_user"]).all()
    notification_service = NotificationService.objects.filter(id=service_id).first()
    setting = NotificationSetting.objects.filter(notification_service_id=service_id, vendor_user=user_obj["vendor_user"]).first()
    if not setting:
        setting = NotificationSetting()
        setting.vendor_user = user_obj["vendor_user"]
        setting.notification_service = notification_service

    if request.POST:
        setting.setting_value = request.POST['setting_value']
        setting.save()

    context = {
        "title": "Notification Settings",
        "services": notification_services,
        "selected_service": notification_service,
        "setting_value": setting.setting_value,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings/notification.html", context)


@login_required(login_url='/qa/')
def style(request):
    """ list """
    user_obj = get_login_user_objects(request)

    # fetch css string from vendor object
    vendor_branch = user_obj["vendor_branch"]
    vendor = Vendor.objects.filter(id=vendor_branch.vendor.id).first()
    css_string = vendor.contactchat_css

    # convert css string to dict
    if css_string:
        css_dict = ast.literal_eval(css_string)
    else:
        css_dict = {}

    # convert static_text string to dict
    static_text_string = read_static_text(vendor.contactchat_access_url_part)

    if static_text_string:
        static_text_dict = ast.literal_eval(static_text_string)
    else:
        static_text_dict = {'english': {'header': "default text"}}

    if request.method == "POST":

        css_dict['robottextcolor'] = request.POST['--robottextcolor']
        css_dict['robotbubblecolor'] = request.POST['--robotbubblecolor']
        css_dict['usertextcolor'] = request.POST['--usertextcolor']
        css_dict['userbubblecolor'] = request.POST['--userbubblecolor']
        css_dict['chatbackgroundcolor'] = request.POST['--chatbackgroundcolor']
        css_dict['submitbuttoncolor'] = request.POST['--submitbuttoncolor']

        css_dict['windowcolor'] = request.POST['--windowcolor']
        css_dict['infotextcolor'] = request.POST['--infotextcolor']

        css_dict['usericon'] = request.POST['--usericon']
        css_dict['roboticon'] = request.POST['--roboticon']
        css_dict['fontsize'] = request.POST['--fontsize']
        css_dict['fontfamily'] = request.POST['--fontfamily']
        css_dict['fontstyle'] = request.POST['--fontstyle']


        static_text_dict['english']['header'] = request.POST['--englishheader']

        json_dump = json.dumps(css_dict)
        vendor.contactchat_css = json_dump
        vendor.save()

        # save css to S3 bucket under vendor identifier
        save_css(create_contactchat_css(css_dict), vendor.contactchat_access_url_part)

        # save static_text to S3 bucket under vendor identifier
        save_static_text(json.dumps(static_text_dict), vendor.contactchat_access_url_part)

    cc_base_url = settings.CONTACTCHAT_BASE_URL

    context = {
        "title": "Vendor Settings",
        "path": ["Settings", "Style Settings"],
        "vendor": user_obj["vendor_branch"].vendor,
        "css_dict": css_dict,
        "static_text_dict": static_text_dict,
        "cc_base_url": cc_base_url,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings/style.html", context)
