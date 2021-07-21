from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.vendor_event_settings import VendorEventSettings

# import views
from apps.core.views.vendor_common.login_user_info import *

# import forms
from apps.core.forms.settings_event import EventSettingsForm


@login_required
def index(request):
    """ index """
    user_obj = get_login_user_objects(request)

    vendor_event_settings = VendorEventSettings.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).first()
    form = EventSettingsForm(instance=vendor_event_settings)

    context = {
        "title": "Event Base Settings",
        "path": ["Settings", "Event Base Settings"],
        "vendor_branch": user_obj["vendor_branch"],
        "vendor_event_settings": vendor_event_settings,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings_event_index.html", context)


@login_required
def edit(request, vendor_event_settings_id=None):
    """ Edit """
    user_obj = get_login_user_objects(request)

    vendor_event_settings = VendorEventSettings.objects.filter(id=vendor_event_settings_id).first()
    if request.method == "POST":
        form = EventSettingsForm(request.POST, instance=vendor_event_settings)
        if form.is_valid():
            vendor_event_settings = form.save(commit=False)
            vendor_event_settings.update_dt = timezone.now()
            vendor_event_settings.save()
            redirect_url = "/" + user_obj["service_url"] + "/settings/event/"
            return redirect(redirect_url)

    else:
        form = EventSettingsForm(instance=vendor_event_settings)

    context = {
        "title": "Event Base Settings",
        "path": ["Settings", "Event Base Settings"],
        "vendor_branch": user_obj["vendor_branch"],
        "vendor_event_settings": vendor_event_settings,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings_event_index.html", context)
