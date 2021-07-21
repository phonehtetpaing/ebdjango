from django.conf import settings

# import models
from apps.nchat.models.vendor_user import VendorUser
from apps.nchat.models.business import Business


def get_service_platform_info_by_id(service_name):
    business = Business.objects.filter(service_name=service_name, is_delete=False).first()
    if not business:
        raise LookupError("the specified service with id, {0}, could not be found!".format(service_name))

    service_name = business.service_name
    service_logo = business.logo

    service_platform_info = {
        "namespace": "nchat",
        "service_name": service_name,
        "service_logo": '{0}{1}'.format(settings.MEDIA_ROOT, service_logo),
    }
    return service_platform_info
