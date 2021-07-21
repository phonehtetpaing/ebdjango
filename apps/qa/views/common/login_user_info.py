# import models
from apps.qa.models.vendor_user import VendorUser
from apps.qa.models.vendor_service import VendorService


def get_login_user_objects(request):
    """ Get Vendor Login User Info """
    vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
    vendor_service = VendorService.objects.filter(vendor=vendor_user.vendor_branch.vendor).first()
    if vendor_service:
        service = vendor_service.service
        service_namespace = service.name.lower()
        service_url = service.name.lower()

    user_object_dict = {
        "vendor_branch": vendor_user.vendor_branch,
        "service_namespace": service_namespace,
        "service_url": service_url,
        "vendor_user": vendor_user,
    }

    return user_object_dict
