from django.shortcuts import render

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.event_category import EventCategory

# import views

# import models
from apps.core.models.vendor_branch import VendorBranch






def registration(request):
    """ Get Vendor Login User Info """

    # TODO : check the session if user_object exists.

    # TODO: get vendor_branch_id from login_vendor_user_id

    vendor_branch_id = 1
    vendor_branch = VendorBranch.objects.filter(id=vendor_branch_id, is_delete=False).first()

    user_object_dict = {
        "vendor_branch": vendor_branch,
        "service_namespace": "smart_sec",
        "service_url": "smartsec",
    }

    return user_object_dict
