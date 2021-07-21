# -*- coding: utf-8 -*-
from django.conf import settings
import requests
from django.contrib.auth.decorators import login_required

# models
from apps.qa.models.vendor_user import VendorUser
from apps.qa.models.senbay_user import SenbayUser

api_base_url = settings.SENBAY_BASE_URL + "api"

request_url = {
    "team_detail": api_base_url + "/team/",
    "template": api_base_url + "/template/",
    "add_template": api_base_url + "/template/add/",
    "account": api_base_url + "/account/",
    "get_schedule_now_list": api_base_url + "/schedule/now/",
    "get_schedule_past_list": api_base_url + "/schedule/past/",
    "delete_schedule": api_base_url + "/schedule/delete/",
    "get_template_once": api_base_url + "/template/once/",
    "create_template_once": api_base_url + "/template/once/",
}


@login_required(login_url='/qa/')
def request_get(request, url_name, params, id):
    vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
    senbay_user = SenbayUser.objects.filter(vendor_user_id=vendor_user.id, is_active=True).first()
    if senbay_user is None:
        return None

    if senbay_user.jwt_token is None:
        return None

    token = senbay_user.jwt_token
    header_string = "JWT " + token
    headers = {'Authorization': header_string}
    url = request_url[url_name]

    if id is not None:
        url = url + str(id) + "/"

    if params:
        response = requests.get(url, headers=headers, params=params)
    else:
        response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    else:
        return None


@login_required(login_url='/qa/')
def request_post(request, url_name, params):
    vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
    senbay_user = SenbayUser.objects.filter(vendor_user_id=vendor_user.id, is_active=True).first()
    if senbay_user is None:
        return None

    if senbay_user.jwt_token is None:
        return None

    token = senbay_user.jwt_token
    header_string = "JWT " + token
    headers = {'Authorization': header_string}
    url = request_url[url_name]

    if params:
        response = requests.post(url, headers=headers, params=params)
    else:
        response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    else:
        return None


@login_required(login_url='/qa/')
def request_delete(request, url_name, id):
    vendor_user = VendorUser.objects.filter(auth_user=request.user).first()
    senbay_user = SenbayUser.objects.filter(vendor_user_id=vendor_user.id, is_active=True).first()
    if senbay_user is None:
        return None

    if senbay_user.jwt_token is None:
        return None

    token = senbay_user.jwt_token
    header_string = "JWT " + token
    headers = {'Authorization': header_string}
    url = request_url[url_name]

    if id is not None:
        url = url + str(id) + "/"

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    else:
        return None
