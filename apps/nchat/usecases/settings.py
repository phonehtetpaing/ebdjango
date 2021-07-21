from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from apps.messageflow.usecases.settings import get_line_token_dict_from_auth_user
from apps.nchat.models.vendor_user import VendorUser
from apps.nchat.models.business import Business
from apps.messageflow.models.settings import Settings


class BusinessConfigurationException(Exception):
    pass


def get_line_token_dict_from_business(business):
    """
    Finds and returns a settings object containing access tokens for the LINE api based
    on the business identification.
    :param business:
    :return:
    """
    if not business or not isinstance(business, Business):
        error_msg = (
            'business {0} is malformed or not of type Business'
        ).format(business)
        raise LookupError(error_msg)

    vendor_user = VendorUser.objects.filter(business=business).first()
    print("vendor_user: ", vendor_user)
    line_token_dict = get_line_token_dict_from_auth_user(vendor_user.auth_user)
    line_token_dict.update({
        "business": business
    })
    return line_token_dict


@login_required()
def get_line_token_dict_from_request(request):
    """
    Find and returns a settings object containing access tokens for the LINE api
    :param request:
    :return:
    """
    vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
    if not vendor_user:
        error_msg = (
            'user {0} is not of registered for nchat or is incorrectly configured'
        ).format(vendor_user)
        raise LookupError(error_msg)

    return get_line_token_dict_from_business(vendor_user.business)


def get_line_token_dict_from_path(request_path):
    """
    Note VERIFY token(channel secret) is to verify incoming messages, ACCESS token is to sign off on outgoing ones
    :param request_path:
    :return:
    """

    path_list = request_path.split("/")
    service_name = path_list[1]
    platform = path_list[3]
    access_url = path_list[4]
    bot_id = path_list[5]

    # business and settings object have to exist
    business_settings = get_object_or_404(Settings, line_access_url_part=access_url)
    vendor_user = get_object_or_404(VendorUser, auth_user_id=business_settings.owner_id)
    business = vendor_user.business
    line_token_dict = get_line_token_dict_from_business(business)

    if access_url != line_token_dict['line_access_url_part']:
        error_msg = (
            'access tokens do not match for business {0} and access token {1}'
        ).format(business, access_url)
        raise BusinessConfigurationException(error_msg)

    line_token_dict.update({
        "bot_id": bot_id,
    })
    return line_token_dict
