# -*- coding: utf-8 -*-
import json
import requests
from random import choice
from string import ascii_letters, digits, punctuation
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

# import models
from django.conf import settings
from django.contrib.auth.models import User
from apps.core.models.service import Service
from apps.core.models.vendor import Vendor
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_line import EndUserLINE
from apps.core.models.end_user_state import EndUserState
from apps.core.models.end_user_auto_message import EndUserAutoMessage
from apps.core.models.auto_message_type import AutoMessageType


def get_end_user_info(request_path, user_id):
    path_list = request_path.split("/")
    end_user_dict = dict()
    service_name = path_list[1]
    print(service_name)

    service = Service.objects.filter(name=service_name).first()
    end_user_vendor_info = get_end_user_vendor_info(request_path)

    end_user_lines = EndUserLINE.objects.filter(user_id=user_id).all()
    end_user_line = None
    for tmp_user in end_user_lines:
        if tmp_user.end_user.vendor_branch.vendor.service == service and tmp_user.end_user.vendor_branch.id == end_user_vendor_info['vendor_branch_id']:
            end_user_line = tmp_user

    if end_user_line:
        end_user = EndUser.objects.filter(id=end_user_line.end_user_id).first()
        # if user was deleted reactivate it
        if end_user.is_delete:
            end_user.is_delete = False
            end_user.save()
        print(end_user_line.end_user_id)

        end_user_dict = {
            "user_id": user_id,
            "service_id": end_user.vendor_branch.vendor.service.id,
            "vendor_id": end_user.vendor_branch.vendor.id,
            "vendor_branch_id": end_user.vendor_branch.id,
            "platform": path_list[2],
            "line_access_token": end_user.vendor_branch.vendor.line_access_token,
            "reservation_data": end_user.reservation_data_json,
            "end_user_obj": end_user,
            "vendor_branch": end_user.vendor_branch,
        }

    return end_user_dict


def get_end_user_vendor_info(request_path):
    path_list = request_path.split("/")

    try:
        service = Service.objects.filter(name=path_list[1]).first()
        vendor = Vendor.objects.filter(service_id=service.id, line_access_url_part=path_list[3]).first()
        vendor_branch = VendorBranch.objects.filter(vendor_id=vendor.id).first()

        end_user_dict = {
            "service_id": service.id,
            "vendor_id": vendor.id,
            "vendor_branch_id": vendor_branch.id,
            "platform": path_list[2],
            "line_access_token": vendor.line_access_token,
            "line_verify_token": vendor.line_verify_token,
        }

        print(vendor.company_name)
        print(vendor.line_access_token)
        print(vendor.line_verify_token)

        return end_user_dict

    except Exception as e:
        print('%r' % e)
        return None


def create_or_update_auth_user(user_id, end_user_vendor_info_dict):
    """" create or update auth user"""
    line_bot_api = LineBotApi(end_user_vendor_info_dict["line_access_token"])
    profile = line_bot_api.get_profile(user_id)

    end_users = EndUser.objects.filter(vendor_branch_id=end_user_vendor_info_dict["vendor_branch_id"])
    end_user_line = EndUserLINE.objects.filter(user_id=user_id, end_user__in=end_users).first()
    end_user_state = EndUserState.objects.filter(cd="INITIAL").first()

    try:

        if end_user_line:
            end_user = EndUser.objects.filter(id=end_user_line.end_user_id).first()

            if end_user:
                # update state to INITIAL
                end_user.end_user_state_id = end_user_state.id
                end_user.save()
                # update LINE user info.
                end_user_line.display_name = profile.display_name
                end_user_line.picture_url = profile.picture_url
                end_user_line.user_id = profile.user_id
                end_user_line.save()

                return True

            return False

        else:
            # get initial user status id

            # create auth user
            auth_username = profile.display_name
            auth_user_info_dict = get_new_auth_user_dict(auth_username)

            # create a new end_user
            end_user = EndUser()
            # end_user.last_name = profile.display_name
            end_user.first_name = profile.display_name
            end_user.django_pass_cd = auth_user_info_dict["pass_code"]
            end_user.auth_user_id = auth_user_info_dict["user_id"]
            end_user.vendor_branch_id = end_user_vendor_info_dict["vendor_branch_id"]
            end_user.end_user_state_id = end_user_state.id
            end_user.save()

            # create a new end_user_facebook
            end_user_line = EndUserLINE()
            end_user_line.user_id = profile.user_id
            end_user_line.display_name = profile.display_name
            end_user_line.picture_url = profile.picture_url
            end_user_line.end_user = end_user
            end_user_line.save()

            # create a new EndUserAutoMessage
            auto_message_types = AutoMessageType.objects.filter(is_delete=False).all()
            for auto_message_type in auto_message_types:
                end_user_auto_message = EndUserAutoMessage()
                if auto_message_type.name == "Registration Date":
                    end_user_auto_message.message_target_dt = end_user.regist_dt
                end_user_auto_message.auto_message_type = auto_message_type
                end_user_auto_message.end_user = end_user
                end_user_auto_message.save()

            return True

    except Exception as e:
        print('%r' % e)
        return False


def generate_passwd(length=10, chars=ascii_letters+digits+punctuation):
    return ''.join([choice(chars) for i in range(length)])


def get_new_auth_user_dict(auth_username):
    # make a random password and user name
    random_password = generate_passwd(10, ascii_letters+digits)
    random_code = generate_passwd(6, ascii_letters + digits)
    auth_username = auth_username + '_' + random_code

    # create a new django auth user
    user = User.objects.create_user(username=auth_username, password=random_password)
    auth_user_info_dict = {"user_id": user.id, "pass_code": random_password }

    return auth_user_info_dict


def get_payload(user_id):
    end_user_line = EndUserLINE.objects.filter(user_id=user_id).first()
    payload = None
    if end_user_line:
        if end_user_line.payload:
            payload = end_user_line.payload
            end_user_line.payload = None
            end_user_line.save()

    return payload


def set_payload(user_id, payload):
    end_user_line = EndUserLINE.objects.filter(user_id=user_id).first()
    if end_user_line:
        end_user_line.payload = payload
        end_user_line.save()
