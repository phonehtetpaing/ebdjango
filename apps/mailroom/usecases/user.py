# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from django.urls import resolve

from django.contrib.auth.models import AnonymousUser

class UserUnauthorizedError(Exception):
    pass


class AuthorizeUser:
    """
    Use case for authorizing user that access mailroom views.
    If the user is unrecognized or somehow incorrectly configured an exception is raised.
    """

    def __init__(
            self,
            user,
            path,
    ):
        # Set the internal state for the operation
        self._user = user
        self._path = path

    def execute(self):
        self.valid_data()
        login_user_info = self._get_app_info()
        login_user_info.update(self._get_login_user_info())

        return login_user_info

    def valid_data(self):
        # It is a public method to allow clients of this object to validate
        # the data even before to execute the use case.
        if isinstance(self._user, AnonymousUser) or not self._user:
            error_msg = (
                'The authenticated user, {}, is not registered or is not authorized to perform this operation.'
            ).format(self._user)

            raise UserUnauthorizedError(_(error_msg))

        return True

    def _get_login_user_info(self):
        """ Get Login User Info """
        return {
            "owner_id": self._user.id
        }

    def _get_app_info(self):
        r = resolve(self._path)
        # the the currently active instance
        print('debug namespacing', r.namespace)
        namespace = r.namespace.split(":")[0]
        return {
            "app_id": namespace,
            "namespace": namespace,
        }
