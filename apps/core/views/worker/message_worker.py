import json
import datetime
import string
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# import views
from apps.core.views.messaging_adapter_web.text_send_message import *
from apps.core.views.messaging_adapter_web.button_select_message import *
from apps.core.views.messaging_adapter_web.image_send_message import *
from apps.core.views.messaging_adapter_web.carousel_send_message import *
from apps.core.views.vendor_common.message_json_converter import *
from apps.core.views.vendor_common.login_user_info import *
from apps.core.views.worker.manual_message import *
from apps.core.views.worker.auto_message import *

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.manual_message_controller import ManualMessageController
from apps.core.models.manual_message_history import ManualMessageHistory
from apps.core.models.tag import Tag
from apps.core.models.manual_message_overview import ManualMessageOverview
from apps.core.models.message_status import MessageStatus
from apps.core.models.worker_sqs_status import WorkerSQSStatus


@csrf_exempt
def send_message(request):
    """
    Get SQS Message (request.META)
    [Sun Jul 08 22: 33:36.674864
    2018] [: error] [pid 14993]
    {'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PROTOCOL': 'HTTP/1.1', 'REQUEST_METHOD': 'POST', 'QUERY_STRING': '',
     'REQUEST_URI': '/smartsec/worker/manual/message/', 'SCRIPT_NAME': '',
     'PATH_INFO': '/smartsec/worker/manual/message/',
     'PATH_TRANSLATED': '/opt/python/current/app/messaging_platform/wsgi.py/smartsec/worker/manual/message/',
     'CONTENT_TYPE': 'application/json', 'HTTP_USER_AGENT': 'aws-sqsd/2.3',
     'HTTP_X_AWS_SQSD_MSGID': 'ae631e0c-ee1c-4563-a6cb-55bc3783237e', 'HTTP_X_AWS_SQSD_RECEIVE_COUNT': '6',
     'HTTP_X_AWS_SQSD_FIRST_RECEIVED_AT': '2018-07-08T13:08:26Z', 'HTTP_X_AWS_SQSD_SENT_AT': '2018-07-08T13:08:26Z',
     'HTTP_X_AWS_SQSD_QUEUE': 'awseb-e-qmt9dhtxp4-stack-AWSEBWorkerQueue-15DBFG1KM87I6', 'HTTP_X_AWS_SQSD_PATH': '',
     'HTTP_X_AWS_SQSD_SENDER_ID': 'AIDAI5U3ZEJYSDUDXD44K', 'HTTP_X_AWS_SQSD_ATTR_TITLE': 'Manual Message',
     'HTTP_X_AWS_SQSD_ATTR_VENDORUSERID': '1', 'HTTP_HOST': 'localhost', 'CONTENT_LENGTH': '54', 'SERVER_SIGNATURE': '',
     'SERVER_SOFTWARE': 'Apache/2.4.33 (Amazon) mod_wsgi/3.5 Python/3.6.5', 'SERVER_NAME': 'localhost',
     'SERVER_ADDR': '127.0.0.1', 'SERVER_PORT': '80', 'REMOTE_ADDR': '127.0.0.1', 'DOCUMENT_ROOT': '/var/www/html',
     'REQUEST_SCHEME': 'http', 'CONTEXT_PREFIX': '', 'CONTEXT_DOCUMENT_ROOT': '/var/www/html',
     'SERVER_ADMIN': 'root@localhost', 'SCRIPT_FILENAME': '/opt/python/current/app/messaging_platform/wsgi.py',
     'REMOTE_PORT': '58972', 'mod_wsgi.process_group': 'wsgi',
     'mod_wsgi.application_group': 'ip-172-31-15-216.ap-northeast-1.compute.internal|',
     'mod_wsgi.callable_object': 'application', 'mod_wsgi.request_handler': 'wsgi-script',
     'mod_wsgi.handler_script': '', 'mod_wsgi.script_reloading': '1', 'mod_wsgi.listener_host': '',
     'mod_wsgi.listener_port': '80', 'mod_wsgi.input_chunked': '0', 'mod_wsgi.enable_sendfile': '0',
     'mod_wsgi.queue_start': '1531056816672520', 'wsgi.version': (1, 0), 'wsgi.multithread': True,
     'wsgi.multiprocess': True, 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.errors': < _io.TextIOWrapper
    encoding = 'utf-8' >, 'wsgi.input': < mod_wsgi.Input
    object
    at
    0x7f07fa928e70 >, 'wsgi.file_wrapper': < built - in method
    file_wrapper
    of
    mod_wsgi.Adapter
    object
    at
    0x7f07fa87ff30 >, 'mod_wsgi.version': (3, 5)}
    """

    # Get SQS Message Data
    sqs_message_body_dict = json.loads(request.body)

    # Get data for message Type (Auto / Manual)
    message_type = sqs_message_body_dict["message_type"]

    if settings.MODE == "LOCAL":
        sqs_message_id = sqs_message_body_dict["HTTP_X_AWS_SQSD_MSGID"]
        sqs_timestamp = sqs_message_body_dict["HTTP_X_AWS_SQSD_FIRST_RECEIVED_AT"]
    else:
        sqs_message_id = request.META['HTTP_X_AWS_SQSD_MSGID']
        sqs_timestamp = request.META['HTTP_X_AWS_SQSD_FIRST_RECEIVED_AT']

    # Check if the same message is taken
    # status 1: Inprogress 2: DONE 3: Send Message Error 4: Save History Error
    worker_sqs_status = WorkerSQSStatus.objects.filter(message_id=sqs_message_id, is_delete=False).order_by(
        "-regist_dt").first()
    if worker_sqs_status:
        if worker_sqs_status.status == 1:
            return HttpResponse("In-Progress", status=500)
        elif worker_sqs_status.status == 2:
            return HttpResponse("Done", status=200)
        elif worker_sqs_status.status == 3:
            # retry
            worker_sqs_status = WorkerSQSStatus()
        elif worker_sqs_status.status == 4:
            return HttpResponse("ERROR: Save history", status=200)
        else:
            return HttpResponse("Return 500", status=500)

    else:
        # Insert SQS Status
        worker_sqs_status = WorkerSQSStatus()

    # Save Message data & Process starts
    worker_sqs_status.message_id = sqs_message_id
    worker_sqs_status.message = sqs_message_body_dict
    worker_sqs_status.status = 1
    worker_sqs_status.save()

    # Send Manual Message
    if message_type == "MANUAL":
        vendor_user_id = int(sqs_message_body_dict["vendor_user_id"])
        manual_message_overview_id = int(sqs_message_body_dict["manual_message_overview_id"])
        manual_message_history_id = int(sqs_message_body_dict["manual_message_history_id"])

        manual_message_history = ManualMessageHistory.objects.filter(id=manual_message_history_id).first()
        result = send_manual_message(vendor_user_id, manual_message_overview_id, manual_message_history, worker_sqs_status)

        # response
        if result == "Message Send ERROR":
            return HttpResponse("Message Send ERROR", status=500)
        elif result == "Success":
            return HttpResponse("Success", status=200)
        elif result == "Success":
            return HttpResponse("History Save ERROR", status=200)
        else:
            return HttpResponse("ERROR", status=500)

    # Send Auto Message
    elif message_type == "AUTO":
        auto_message_trigger_id = int(sqs_message_body_dict["auto_message_trigger_id"])
        auto_message_history_id = int(sqs_message_body_dict["auto_message_history_id"])
        batch_start_dt = datetime.datetime.strptime(sqs_message_body_dict["batch_start_dt"], '%Y-%m-%d %H:%M:%S')
        result = send_auto_message(auto_message_trigger_id, auto_message_history_id, batch_start_dt, worker_sqs_status)

        if result == "Message Send ERROR":
            return HttpResponse("Message Send ERROR", status=500)
        elif result == "Success":
            return HttpResponse("Success", status=200)
        else:
            return HttpResponse("ERROR", status=500)
