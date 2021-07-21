# -*- Coding: utf-8 -*-
# import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.vendor_user import VendorUser


def get_login_user_objects(request):
    """ Get Vendor Login User Info """

    # TODO : check the session if user_object exists.
    vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
    service = vendor_user.vendor_branch.vendor.service
    vendor = vendor_user.vendor_branch.vendor

    if service.cd == "00001":
        # SMART SEC
        if vendor.oem_service_namespace and vendor.oem_service_namespace:
            service_namespace = vendor.oem_service_namespace
            service_url = vendor.oem_service_namespace

        else:
            service_namespace = "smart_sec"
            service_url = "smartsec"

    elif service.cd == "00002":
        # TODO: Contact Chat
        service_namespace = "contactchat"
        service_url = "contactchat"

    elif service.cd == "00003":
        # TODO: Smart Senkyo Connect
        service_namespace = "connect"
        service_url = "connect"

    elif service.cd == "00004":
        # TODO: Contact Chat
        service_namespace = "contactchat"
        service_url = "contactchat"

    user_object_dict = {
        "vendor_branch": vendor_user.vendor_branch,
        "service_namespace": service_namespace,
        "service_url": service_url,
        "vendor_user": vendor_user,
    }

    return user_object_dict
