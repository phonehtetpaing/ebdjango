# import models
from apps.nchat.models.vendor_user import VendorUser
from apps.nchat.models.business import Business


def get_login_user_objects(request):
    """ Get Vendor Login User Info """
    vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
    business = Business.objects.filter(id=vendor_user.business.id).first()

    if business:
        service_namespace = business.service_name.lower().replace(" ", "")
        service_url = business.service_name.lower().replace(" ", "")

    user_object_dict = {
        "business": vendor_user.business,
        "service_namespace": service_namespace,
        "service_url": service_url,
        "vendor_user": vendor_user,
    }

    return user_object_dict
