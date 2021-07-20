from django.shortcuts import render

# import views
from apps.core.views.vendor.system_initial_setup import *

# import models
from apps.core.models.service import Service
from apps.core.models.vendor import Vendor
from apps.core.models.vendor_user import VendorUser


def is_setup_approved(request):
    try:
        # Get Service Name of URL
        path_list = request.path.split("/")
        url_service_name = path_list[1]

        # Get login user Service Name
        vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
        service_name = vendor_user.vendor_branch.vendor.service.name
        oem_service_url = vendor_user.vendor_branch.vendor.oem_service_url

        if url_service_name == service_name:

            if oem_service_url is None and in_group(request.user, "system"):
                return True
        else:
            if url_service_name == oem_service_url:
                if in_group(request.user, "system"):
                    return True

        return False

    except Exception as e:
        print('%r' % e)
        return False


def get_namespace(request):
    try:
        # Get Service Name
        path_list = request.path.split("/")
        service_name = path_list[1]

        if service_name == "smartsec":
            service_name = "smart_sec"

        return service_name

    except Exception as e:
        return "smart_sec"


def get_service_id(request):
    # Requirement: the part of url equals service.name
    try:
        # Get Service Name
        path_list = request.path.split("/")
        service_name = path_list[1]
        service = Service.objects.filter(name=service_name).first()
        if service:
            return service.id
        else:
            # check if OEM url exists
            vendor = Vendor.objects.filter(oem_service_url=service_name, is_delete=False).first()
            if vendor:
                return vendor.service.id

            return None

    except Exception as e:
        print('%r' % e)
        return None


def get_oem_url(request):
    # Get Service Name
    path_list = request.path.split("/")
    url_part = path_list[1]

    return url_part


def is_oem_admin(request):
    try:
        # Get Service Name
        path_list = request.path.split("/")
        service_name = path_list[1]

        # Get Login user oem name
        vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
        if vendor_user:
            vendor = vendor_user.vendor_branch.vendor
            if vendor.oem_service_namespace == service_name:
                return True

        return False

    except Exception as e:
        print('%r' % e)
        return False


def get_oem_vendor_list(request):

    vendor_list = []

    try:
        # Get Login user oem name
        vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
        if vendor_user:
            oem_name = vendor_user.vendor_branch.vendor.oem_service_namespace
            vendors = Vendor.objects.filter(oem_service_namespace=oem_name, is_delete=False).all()
            for vendor in vendors:
                vendor_list.append(vendor.id)

        return vendor_list

    except Exception as e:
        return vendor_list


def is_initial_setup(request, vendor_id):
    try:
        # Get Service Name
        path_list = request.path.split("/")
        service_name = path_list[1]

        # Get Login user oem name
        vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
        if vendor_user:
            vendor = vendor_user.vendor_branch.vendor
            if vendor.oem_service_namespace == service_name:
                target_vendor = Vendor.objects.filter(id=vendor_id, oem_service_namespace=service_name).first()
                if target_vendor:
                    return True

            else:
                if in_group(request.user, "system"):
                    return True

        else:
            if in_group(request.user, "system"):
                return True

        return False

    except Exception as e:
        return False


def in_group(user, team_name):
    if user.groups.filter(name=team_name).exists():
        return True
    else:
        return False