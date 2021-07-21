# imports for webhook
import traceback

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
import json

# import models
from apps.nchat.models.settings import Settings

# import forms
from apps.nchat.usecases.webhook import HandleCallback


@csrf_exempt
def line(request):
    payload = request.body
    event = None
    print(payload)
    return HttpResponse(status=200)


@csrf_exempt
def line_callback(request, access_url_part=None, bot_id=None):
    # todo placeholder function for testing
    try:
        print("trying to get a message from line:", request)
        response = HandleCallback(request, access_url_part).execute()
        return response
    except Exception as e:
        print('got exception in HandleCallback', e)
        print(print(traceback.format_exc()))
        return HttpResponseBadRequest()
