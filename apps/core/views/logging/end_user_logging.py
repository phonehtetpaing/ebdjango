import logging
import json
from apps.core.views.logging.logging_util import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test(request):
    logger = logging.getLogger('default')
    try:
        request_body = request.body.decode('utf-8')
        request_body_json = request_body.replace('\'', '\"')

        print("debug:request_body_json")
        print(request_body_json)

        request_data = json.loads(request_body_json)

        if "sender" in request_data[0]:
            request_info = get_end_sender_info(request)
        else:
            request_info = get_request_info(request)

    except Exception as e:
        logger.error('%r' % e)


def end_user_logger(request, end_user_info):
    logger = logging.getLogger('default')
    try:
        request_body = request.body.decode('utf-8')
        request_body_json = request_body.replace('\'', '\"')

        print("debug:request_body_json")
        print(request_body_json)

        request_data = json.loads(request_body_json)

        try:
            if "sender" in request_data[0]:
                request_info = get_end_sender_info(request)
            else:
                request_info = get_request_info(request)

        except Exception as e:
            print("debug: exception : request_info")
            request_info = get_request_info(request)

        user_info = get_end_user_info(end_user_info)

        if request_info is not None and user_info is not None:
            # Set NULL (not used for Web)
            message_info = None
            msg = json.dumps(user_info) + "\t" + json.dumps(request_info) + "\t" + json.dumps(message_info)
            logger.info(msg)

    except Exception as e:
        logger.error('%r' % e)


def end_user_logger_ms(param_dict):
    logger = logging.getLogger('default')
    try:
        if "function_name" in param_dict:
            function_name = param_dict["function_name"]
        else:
            function_name = None

        if "payload_text" in param_dict:
            payload_text = param_dict["payload_text"]
        else:
            payload_text = None

        if "text" in param_dict:
            text = param_dict["text"]
        else:
            text = None

        if "end_user_info" in param_dict:
            end_user_info = param_dict["end_user_info"]
        else:
            end_user_info = None

        if "step" in param_dict:
            step = param_dict["step"]
        else:
            step = None

        if "message" in param_dict:
            message = param_dict["message"]
            message_dict = {
                "message_block_id": message["message_block_id"],
                "message_progress": message["message_progress"]
            }
        else:
            message_dict = None

        if end_user_info is None:
            user_dict = dict()

        else:
            print(end_user_info)
            end_user_obj = end_user_info["end_user_obj"]
            user_dict = {
                "app_id": end_user_obj.vendor_branch.vendor.service.id,
                "vendor_id": end_user_obj.vendor_branch.vendor.id,
                "vendor_branch_id": end_user_obj.vendor_branch.id,
                "end_user_id": end_user_obj.id,
            }

        request_dict = None

        msg = json.dumps(user_dict) + "\t" + json.dumps(request_dict) + "\t" + json.dumps(message_dict)

        logger.info(msg)

    except Exception as e:
        logger.error('%r' % e)
