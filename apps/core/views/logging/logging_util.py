# -*- coding: utf-8 -*
import traceback
import inspect
import json
from user_agents import parse

from apps.core.models.end_user import EndUser
from apps.core.models.vendor_user import VendorUser


def get_request_info(request):
    try:
        user_agent = request.META['HTTP_USER_AGENT']
        content_type = request.META['CONTENT_TYPE']
        try:
            ip_address = get_client_ip(request)
        except Exception as e:
            ip_address = None

        try:
            http_referer = request.META['HTTP_REFERER']
        except Exception as e:
            http_referer = None

        try:
            server_host = request.get_host()
        except Exception as e:
            server_host = None

        endpoint = request.META['PATH_INFO']
        action_type = get_action_type(endpoint)

        if request.method == u'GET':
            params = format_params(dict(request.GET))
        elif request.method == u'POST':
            params = format_params(dict(request.POST))
        else:
            params = u''

        user_agent_dict = get_user_agents(user_agent)

        request_dict = {
            "device_type": user_agent_dict["device_type"],
            "device_family": user_agent_dict["device_family"],
            "os_family": user_agent_dict["os_family"],
            "os_version": user_agent_dict["os_version"],
            "browser_family": user_agent_dict["browser_family"],
            "browser_version": user_agent_dict["browser_version"],
            "content_type": content_type,
            "params": params,
            "http_referer": http_referer,
            "ip_address": ip_address,
            "server_host": server_host,
            "endpoint": endpoint,
            "action_type": action_type
        }

        print("logging_request_dict ==================")
        print(request_dict)

        return request_dict

    except Exception as e:
        return None


def get_end_sender_info(request):
    # json from contact chat
    # sender: {
    #     id: '', end_user_contactchat_id
    #     useragent: '',
    #     address: '',
    # },

    try:
        endpoint = request.META['PATH_INFO']
        content_type = request.META['CONTENT_TYPE']
        action_type = get_action_type(endpoint)
        if request.method == u'GET':
            params = format_params(dict(request.GET))
        elif request.method == u'POST':
            params = format_params(dict(request.POST))
        else:
            params = u''

        body_data = json.loads(request.body)
        sender_body = body_data[0]["sender"]

        end_user_contactchat_id = sender_body["id"]
        sender_useragent = sender_body["useragent"]
        sender_address = sender_body["address"]
        user_agent_dict = get_user_agents(sender_useragent)

        sender_dict = {
            "device_type": int(user_agent_dict["device_type"]),
            "device_family": user_agent_dict["device_family"],
            "os_family": user_agent_dict["os_family"],
            "os_version": user_agent_dict["os_version"],
            "browser_family": user_agent_dict["browser_family"],
            "browser_version": user_agent_dict["browser_version"],
            "content_type": content_type,
            "params": params,
            "http_referer": None,
            "ip_address": sender_address,
            "server_host": None,
            "endpoint": endpoint,
            "action_type": action_type
        }

        print("logging_sender_dict ==================")
        print(sender_dict)

        return sender_dict

    except Exception as e:
        print("error: get_end_sender_info")
        print('%r' % e)
        return None


def get_end_user_info(end_user_info):
    if enumerate is None:
        return None

    else:
        end_user_obj = end_user_info["end_user_obj"]

        user_dict = {
            "app_id": end_user_obj.vendor_branch.vendor.service.id,
            "vendor_id": end_user_obj.vendor_branch.vendor.id,
            "vendor_branch_id": end_user_obj.vendor_branch.id,
            "end_user_id": end_user_obj.id,
        }

        return user_dict


def get_user_info(user):

    user_dict = {
        "app_id": None,
        "vendor_id": None,
        "vendor_branch_id": None,
        "end_user_id": None,
        "vendor_user_id": None
    }

    if user is None:
        # TODO: EndUser without Login (Contact chat)

        # TODO: get data from POST
        end_user = EndUser.objects.filter(auth_user_id=user.id).first()
        if end_user:
            app_id = end_user.vendor_branch.vendor.service.id
            end_user_id = end_user.id
            vendor_branch_id = end_user.vendor_branch.id
            vendor_id = end_user.vendor_branch.vendor.id

            user_dict["app_id"] = app_id
            user_dict["vendor_id"] = vendor_id
            user_dict["vendor_branch_id"] = vendor_branch_id
            user_dict["end_user_id"] = end_user_id

            # TODO
            return None

        return None

    try:
        # Vendor User Access
        # # cannot get FB/LINE end user info because of Messaging Service
        vendor_user = VendorUser.objects.filter(auth_user_id=user.id).first()
        if vendor_user:
            app_id = vendor_user.vendor_branch.vendor.service.id
            vendor_user_id = vendor_user.id
            vendor_branch_id = vendor_user.vendor_branch.id
            vendor_id = vendor_user.vendor_branch.vendor.id

            user_dict["app_id"] = app_id
            user_dict["vendor_id"] = vendor_id
            user_dict["vendor_branch_id"] = vendor_branch_id
            user_dict["vendor_user_id"] = vendor_user_id

            return user_dict

        return None

    except Exception as e:
        print('%r' % e)
        return None


def format_params(params):
    param_items = filter(lambda kv: kv[0] != u'csrfmiddlewaretoken', params.items())
    return u', '.join([u'{}={}'.format(key, list_str(value)) for (key, value) in param_items])


def list_str(params):
    if params is None:
        return u''
    elif len(params) == 1:
        return u'{}'.format(params[0])

    return u'[' + u', '.join(u'{}'.format(item) for item in params) + u']'


def get_client_ip( request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]


def get_function_parameters_and_values():
    frame = inspect.currentframe().f_back
    args, _, _, values = inspect.getargvalues(frame)
    return ([(i, values[i]) for i in args])


def get_function_info():
    return get_function_name() + '(' + str(get_function_parameters_and_values()) + ')'


def get_user_agents(ua_string):

    try:
        user_agent = parse(ua_string)

        # device_type
        if user_agent.is_mobile:
            device_type = 1
        elif user_agent.is_tablet:
            device_type = 2
        elif user_agent.is_pc:
            device_type = 3
        else:
            device_type = 4

        user_agent_dict = {
            "device_type": device_type,    # 1: mobile 2: tablet  3: pc  4: other
            "device_family": user_agent.device.family ,
            "os_family": user_agent.os.family,
            "os_version": user_agent.os.version_string,
            "browser_family": user_agent.browser.family,
            "browser_version": user_agent.browser.version_string,
        }

        return user_agent_dict

    except Exception as e:
        print('%r' % e)
        return None


def get_action_type(endpoint):

    exclude_string_list = ["jsi18n"]

    try:
        # Exclude action_type
        for exclude_string in exclude_string_list:
            if exclude_string in endpoint:
                return None

        # login
        if endpoint == "/":
            return "login"

        # api for ajax
        if "/api/data/" in endpoint:
            return "ajax"

        # TODO: web chat action_type

        return endpoint

    except Exception as e:
        print('%r' % e)
        return None
