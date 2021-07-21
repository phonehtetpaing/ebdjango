from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# import models
from apps.core.models.vendor import Vendor
from apps.core.models.vendor_user import VendorUser

# import views
from apps.core.views.vendor_common.login_user_info import *

# import forms
from apps.core.forms.settings_vendor import VendorSettingsForm


@login_required
def index(request):
    """ list """
    user_obj = get_login_user_objects(request)
    vendor_users = VendorUser.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=False).all()

    context = {
        "title": "Direct Message",
        "path": ["Message", "Direct Message"],
        "vendor": user_obj["vendor_branch"].vendor,
        "vendor_users": vendor_users,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor_contactchat/direct_message.html", context)

