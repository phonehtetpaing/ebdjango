# -*- coding: utf-8 -*-
import json
import requests
from random import choice
from string import ascii_letters, digits, punctuation

# import models
from django.conf import settings
from django.contrib.auth.models import User
from apps.core.models.service import Service
from apps.core.models.vendor import Vendor
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_facebook import EndUserFacebook
from apps.core.models.end_user_state import EndUserState
from apps.core.models.end_user_auto_message import EndUserAutoMessage
from apps.core.models.auto_message_type import AutoMessageType


def get_end_user_info(request_path, sender_id):
    path_list = request_path.split("/")
    end_user_dict = dict()
    service_name = path_list[1]
    print(service_name)

    service = Service.objects.filter(name=service_name).first()
    end_user_vendor_info = get_end_user_vendor_info(request_path)
    print("end_user_vendor_info")
    print(end_user_vendor_info)

    end_user_facebooks = EndUserFacebook.objects.filter(sender_id=sender_id).all()
    end_user_facebook = None

    for tmp_user in end_user_facebooks:
        if tmp_user.end_user.vendor_branch.vendor.service == service and tmp_user.end_user.vendor_branch.id == end_user_vendor_info['vendor_branch_id']:
            end_user_facebook = tmp_user

    if end_user_facebook:
        end_user = EndUser.objects.filter(id=end_user_facebook.end_user_id).first()

        end_user_dict = {
            "sender_id": sender_id,
            "service_id": end_user.vendor_branch.vendor.service.id,
            "vendor_id": end_user.vendor_branch.vendor.id,
            "vendor_branch_id": end_user.vendor_branch.id,
            "platform": path_list[2],
            "fbms_access_token": end_user.vendor_branch.vendor.fbms_access_token,
            "reservation_data": end_user.reservation_data_json,
            "end_user_obj": end_user,
            "vendor_branch": end_user.vendor_branch,
        }

    print("end_user_dict")
    print(end_user_dict)

    return end_user_dict


def get_end_user_vendor_info(request_path):
    path_list = request_path.split("/")

    try:
        service = Service.objects.filter(name=path_list[1]).first()
        vendor = Vendor.objects.filter(service_id=service.id, fbms_access_url_part=path_list[3]).first()
        vendor_branch = VendorBranch.objects.filter(vendor_id=vendor.id).first()

        end_user_dict = {
            "service_id": service.id,
            "vendor_id": vendor.id,
            "vendor_branch_id": vendor_branch.id,
            "platform": path_list[2],
            "fbms_access_token": vendor.fbms_access_token,
        }

        return end_user_dict

    except Exception as e:
        print('%r' % e)
        return None


def create_or_update_auth_user(sender_id, end_user_vendor_info_dict):
    """" create or update auth user"""
    fb_user_url = settings.FB_USER_URL + sender_id
    fb_user_param = {'fields': 'first_name, last_name, profile_pic, locale,timezone,gender', 'access_token': end_user_vendor_info_dict["fbms_access_token"]}
    fb_user_details = requests.get(fb_user_url, fb_user_param).json()
    print(fb_user_details)

    if "error" in fb_user_details:
        fb_user_details["last_name"] = "N/A"
        fb_user_details["first_name"] = "N/A"
        fb_user_details["gender"] = None
        fb_user_details["locale"] = None
        fb_user_details["profile_pic"] = None
        fb_user_details["timezone"] = None

    end_users = EndUser.objects.filter(vendor_branch_id=end_user_vendor_info_dict["vendor_branch_id"])
    end_user_facebook = EndUserFacebook.objects.filter(sender_id=sender_id, end_user__in=end_users).first()

    end_user_state = EndUserState.objects.filter(cd="INITIAL").first()

    try:
        if end_user_facebook:
            end_user = EndUser.objects.filter(id=end_user_facebook.end_user_id).first()

            if end_user:
                # update state to INITIAL
                end_user.end_user_state_id = end_user_state.id
                # if user was deleted reactivate it
                if end_user.is_delete:
                    end_user.is_delete = False
                end_user.save()
                # update facebook info.
                end_user_facebook.last_name = fb_user_details["last_name"]
                end_user_facebook.first_name = fb_user_details["first_name"]
                end_user_facebook.gender = fb_user_details["gender"]
                end_user_facebook.locale = fb_user_details["locale"]
                end_user_facebook.profile_pic_url = fb_user_details["profile_pic"]
                end_user_facebook.timezone = fb_user_details["timezone"]
                end_user_facebook.save()

                return True

            return False

        else:
            # get initial user status id

            # create auth user
            auth_username = fb_user_details['first_name'] + ' ' + fb_user_details['last_name']
            auth_user_info_dict = get_new_auth_user_dict(auth_username)

            # create a new end_user
            end_user = EndUser()
            end_user.last_name = fb_user_details["last_name"]
            end_user.first_name = fb_user_details["first_name"]
            end_user.gender = fb_user_details["gender"]
            end_user.django_pass_cd = auth_user_info_dict["pass_code"]
            end_user.auth_user_id = auth_user_info_dict["user_id"]
            end_user.vendor_branch_id = end_user_vendor_info_dict["vendor_branch_id"]
            end_user.end_user_state_id = end_user_state.id
            end_user.save()

            # create a new end_user_facebook
            end_user_facebook = EndUserFacebook()
            end_user_facebook.sender_id = sender_id
            end_user_facebook.last_name = fb_user_details["last_name"]
            end_user_facebook.first_name = fb_user_details["first_name"]
            end_user_facebook.gender = fb_user_details["gender"]
            end_user_facebook.locale = fb_user_details["locale"]
            end_user_facebook.profile_pic_url = fb_user_details["profile_pic"]
            end_user_facebook.timezone = fb_user_details["timezone"]
            end_user_facebook.end_user_id = end_user.id
            end_user_facebook.save()

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
