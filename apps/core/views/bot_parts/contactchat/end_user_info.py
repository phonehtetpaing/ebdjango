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
from apps.core.models.end_user_contactchat import EndUserContactChat
from apps.core.models.end_user_state import EndUserState


def get_end_user_info(request_path, user_id):
    path_list = request_path.split("/")
    end_user_dict = dict()
    service_name = path_list[1]

    try:
        service = Service.objects.filter(name=service_name).first()
        end_user_vendor_info = get_end_user_vendor_info(request_path)
        end_user_contactchat = EndUserContactChat.objects.filter(user_id=user_id).first()
        if end_user_contactchat:
            end_user = EndUser.objects.filter(vendor_branch_id=end_user_vendor_info['vendor_branch_id'], id=end_user_contactchat.end_user_id).first()
        else:
            print('debug could not find contactchat user', user_id)

        if end_user_contactchat:
            end_user_dict = {
                "user_id": user_id,
                "service_id": end_user.vendor_branch.vendor.service.id,
                "vendor_id": end_user.vendor_branch.vendor.id,
                "vendor_branch_id": end_user.vendor_branch.id,
                "platform": path_list[2],
                "contactchat_access_token": end_user.vendor_branch.vendor.contactchat_access_token,
                "reservation_data": end_user.reservation_data_json,
                "end_user_obj": end_user,
                "vendor_branch": end_user.vendor_branch,
            }

        return end_user_dict
    except Exception as e:
        print('%r' % e)
        return None


def get_end_user_vendor_info(request_path):
    print('request path is: ', request_path)
    path_list = request_path.split("/")

    service = Service.objects.filter(name=path_list[1]).first()
    print('service: ', service)
    print('vendor path: ', path_list[3])
    vendor = Vendor.objects.filter(service_id=service.id, contactchat_access_url_part=path_list[3]).first()
    print('vendor: ', vendor)
    try:
        service = Service.objects.filter(name=path_list[1]).first()
        print(service)
        vendor = Vendor.objects.filter(service_id=service.id, contactchat_access_url_part=path_list[3]).first()
        print(vendor)
        vendor_branch = VendorBranch.objects.filter(vendor_id=vendor.id).first()
        print(vendor_branch)

        end_user_dict = {
            "service_id": service.id,
            "vendor_id": vendor.id,
            "vendor_branch_id": vendor_branch.id,
            "platform": path_list[2],
            "contactchat_access_token": vendor.contactchat_access_token,
            "contactchat_verify_token": vendor.contactchat_verify_token,
        }

        return end_user_dict

    except Exception as e:
        print('%r' % e)
        return None


def create_or_update_auth_user(user_id, end_user_vendor_info_dict):
    """" create or update auth user"""

    end_users = EndUser.objects.filter(vendor_branch_id=end_user_vendor_info_dict["vendor_branch_id"])
    end_user_contactchat = EndUserContactChat.objects.filter(user_id=user_id, end_user__in=end_users).first()
    end_user_state = EndUserState.objects.filter(cd="INITIAL").first()

    try:
        if end_user_contactchat:
            end_user = EndUser.objects.filter(id=end_user_contactchat.end_user_id).first()

            if end_user:
                # update state to INITIAL
                end_user.end_user_state_id = end_user_state.id
                end_user.save()

                return True

            # todo replace this with an actual exception
            # this is clearly some kind of error state so log it
            print('ERROR: found contactchat user without end_user')
            return False

        else:
            # create auth user
            auth_username = ""
            auth_user_info_dict = get_new_auth_user_dict(auth_username)

            # create a new end_user
            end_user = EndUser()
            end_user.first_name = ""
            end_user.last_name = ""

            end_user.django_pass_cd = auth_user_info_dict["pass_code"]
            end_user.auth_user_id = auth_user_info_dict["user_id"]
            end_user.vendor_branch_id = end_user_vendor_info_dict["vendor_branch_id"]
            end_user.end_user_state_id = end_user_state.id
            end_user.save()

            # create a new end_user_contactchat
            end_user_contactchat = EndUserContactChat()
            end_user_contactchat.end_user = end_user
            end_user_contactchat.user_id = user_id
            end_user_contactchat.save()
            print('created new end user contactchat: ', end_user, end_user_contactchat)
            return True

    except Exception as e:
        print('%r' % e)
        return False


def delete_auth_user(user_id, end_user_vendor_info_dict):
    end_users = EndUser.objects.filter(vendor_branch_id=end_user_vendor_info_dict["vendor_branch_id"])
    end_user_contactchat = EndUserContactChat.objects.filter(user_id=user_id, end_user__in=end_users).first()

    if end_user_contactchat:
        # delete end_user_contactchat
        end_user_contactchat.is_delete = True
        end_user_contactchat.save()

        # delete end_user
        end_user = end_user_contactchat.end_user
        end_user.is_delete = True
        end_user.save()


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

