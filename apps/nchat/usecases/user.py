# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from django.urls import resolve

from django.contrib.auth.models import AnonymousUser, User

# import models
from linebot import LineBotApi

from apps.messageflow.models import EndUser
from apps.nchat.models.vendor_user import VendorUser
from apps.nchat.models.business import Business
from apps.nchat.models.payment import PaymentHistory


class UserUnauthorizedError(Exception):
    pass


class AuthorizeUser:
    """
    Use case for authorizing user that access messageflow views.
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
        vendor_user = VendorUser.objects.filter(auth_user=self._user).first()
        return {
            "business": vendor_user.business,
            "vendor_user": vendor_user,
            "owner_id": self._user.id
        }

    def _get_app_info(self):
        r = resolve(self._path)
        # the the currently active instance
        namespace = r.namespace.split(":")[0]
        return {
            "app_id": namespace,
            "namespace": namespace,
        }


class WebhookError(Exception):
    pass


class CreateOrUpdateEndUser:
    """
    Creates or updates an EndUser instance and returns it for use with LINE webhook calls
    """
    def __init__(
            self,
            user_id,
            line_token_dict,
    ):
        # Set the internal state for the operation
        self._user_id = user_id
        self._line_token_dict = line_token_dict

    def execute(self):
        self.valid_data()
        profile = self._get_line_profile()
        end_user = self.create_or_update_end_user(profile)

        return end_user

    def valid_data(self):
        # It is a public method to allow clients of this object to validate
        # the data even before to execute the use case.

        if not self._user_id:
            error_msg = (
                'The user, {}, is can not be used to perform any meaningful operation.'
            ).format(self._user_id)

            raise WebhookError(_(error_msg))

        if not self._line_token_dict or not self._line_token_dict["line_channel_secret"]:
            error_msg = (
                'The token dict required for this operation is missing or the line_channel_secret, {}, is invalid.'
            ).format(self._line_token_dict["line_channel_secret"])

            raise WebhookError(_(error_msg))

        return True

    def _get_line_profile(self):
        """
        Retrieves EndUser profile from LINE platform servers
        """
        line_bot_api = LineBotApi(self._line_token_dict["line_channel_access_token"])
        print('debugging get profile', self._user_id, line_bot_api)
        profile = line_bot_api.get_profile(self._user_id)

        return profile

    def _create_new_auth_user(self, auth_username):
        """
        Creates a new auth user using the provided username,
        the eventual username is suffixed with a random code and the default is a randomly generated string
        of 10 characters.
        :param auth_username:
        :return:
        """
        # make a random password and user name
        random_password = User.objects.make_random_password(length=10)
        random_code = User.objects.make_random_password(length=6)
        auth_username = auth_username + '_' + random_code

        # create a new django auth user
        user = User.objects.create_user(username=auth_username, email=auth_username, password=random_password)
        return user

    def _create_new_end_user(self, line_profile):
        """
        Creates a new LINE end user instance using the provided LINE profile
        :param line_profile:
        :return:
        """
        business = self._line_token_dict['business']
        owner = get_object_or_404(VendorUser, business=business)

        auth_user = self._create_new_auth_user(line_profile.display_name)
        new_user = EndUser(
            auth_user=auth_user,
            first_name=line_profile.display_name,
            owner_id=owner.auth_user.id,
            app_id='nchat',
        )
        new_user.set_attribute_json('line_user_id', line_profile.user_id)
        new_user.set_attribute_json('picture_url', line_profile.picture_url)
        new_user.save()
        return new_user

    def _update_existing_end_user(self, line_profile):
        """
        Update an existing end user using the provided LINE profile if it can be found, returns False if no such
        user exists.
        :param line_profile:
        """
        business = self._line_token_dict['business']
        owner = get_object_or_404(VendorUser, business=business)

        all_users = EndUser.objects.filter(owner_id=owner.auth_user.id, app_id='nchat').all()
        for user in all_users:
            line_id = user.get_attribute_json('line_user_id')
            if line_id and line_id == str(self._user_id):
                user.first_name = line_profile.display_name
                user.set_attribute_json('picture_url', line_profile.picture_url)
                return user

        return False

    def create_or_update_end_user(self, line_profile):
        """" create or update auth user"""
        user = self._update_existing_end_user(line_profile)
        if not user:
            user = self._create_new_end_user(line_profile)

        return user
