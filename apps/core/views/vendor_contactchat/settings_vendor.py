from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings

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
    form = VendorSettingsForm(instance=user_obj["vendor_branch"].vendor)

    script_tag = """
    <script async src="{contactchat_base_url}v1/chat/{contactchat_access_url_part}/widget/loader/"></script>
    """.format(contactchat_base_url=settings.CONTACTCHAT_BASE_URL, contactchat_access_url_part=user_obj["vendor_branch"].vendor.contactchat_access_url_part).strip()

    context = {
        "title": "Vendor Settings",
        "path": ["Settings", "Vendor Settings"],
        "vendor": user_obj["vendor_branch"].vendor,
        "vendor_users": vendor_users,
        "script_tag": script_tag,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor_contactchat/settings_vendor_index.html", context)


@login_required
def edit(request, vendor_id=None):
    """ list """
    user_obj = get_login_user_objects(request)

    vendor = Vendor.objects.filter(id=vendor_id).first()
    if request.method == "POST":
        form = VendorSettingsForm(request.POST, instance=user_obj["vendor_branch"].vendor)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.update_dt = timezone.now()
            vendor.save()
            redirect_url = "/" + user_obj["service_url"] + "/settings/vendor/"
            return redirect(redirect_url)
    else:
        form = VendorSettingsForm(instance=user_obj["vendor_branch"].vendor)

    context = {
        "title": "Vendor Settings",
        "path": ["Settings", "Vendor Settings"],
        "vendor": vendor,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor_contactchat/settings_vendor_index.html", context)


@login_required
def contract_index(request, vendor_user_id=None):
    """ contract index """

    context = {
    }

    return render(request, "vendor_contactchat/settings_contract_index.html", context)


@login_required
def organization_list(request, vendor_user_id=None):
    """ organization list  """

    context = {
    }

    return render(request, "vendor_contactchat/settings_organization_list.html", context)


@login_required
def organization_detail(request, vendor_user_id=None):
    """ contract_detail """

    context = {
    }

    return render(request, "vendor/settings_organization_detail.html", context)


@login_required
def account_list(request, vendor_user_id=None):
    """ account list  """

    context = {
    }

    return render(request, "vendor_contactchat/settings_account_list.html", context)


@login_required
def account_add(request):
    """ account add  """
    user_obj = get_login_user_objects(request)

    context = {
        "title": "Vendor Settings",
        "path": ["Settings", "Vendor Settings"],
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor_contactchat/settings_vendor_new_account.html", context)
