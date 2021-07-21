from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from apps.messageflow.models.settings import Settings


class ConfigurationException(Exception):
    pass


def get_line_token_dict_from_auth_user(auth_user):
    token_settings = get_object_or_404(Settings, owner_id=auth_user.id, app_id='nchat')
    if not token_settings.line_channel_secret:
        error_msg = (
            'line_channel_secret not configured for user {0}'
        ).format(auth_user)
        raise ConfigurationException(error_msg)

    if not token_settings.line_channel_access_token:
        error_msg = (
            'line_channel_access_token not configured for user {0}'
        ).format(auth_user)
        raise ConfigurationException(error_msg)

    line_token_dict = {
        "platform": 'line',
        "line_access_url_part": token_settings.line_access_url_part,
        "line_channel_secret": token_settings.line_channel_secret,
        "line_channel_access_token": token_settings.line_channel_access_token,
    }
    return line_token_dict


@login_required()
def get_line_token_dict_from_request(request):
    """
    Find and returns a settings object containing access tokens for the LINE api
    :param request:
    :return:
    """
    return get_line_token_dict_from_auth_user(request.user)