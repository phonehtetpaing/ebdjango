# -*- coding: utf-8 -*-
# import models
from apps.core.models.vendor import Vendor


def get_access_url_path_dict(request_path):
    path_list = request_path.split("/")
    print(path_list)

    try:
        path_dict = {
            "service": path_list[1],
            "vendor_access_url": path_list[3]
        }

        return path_dict

    except Exception as e:
        print('%r' % e)
        return None


def get_verify_token(access_url_part):
    vendor = Vendor.objects.filter(contactchat_access_url_part=access_url_part, is_delete=0).first()
    return vendor.contactchat_verify_token
