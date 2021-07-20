# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os
import ast
import datetime
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from django.conf import settings

# import views
from apps.core.views.google_utils.google_calendar_oauth import *

# import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.event import Event


def insert_event_schedule(end_user_info, google_event_dict):
    # Google Authentication
    vendar_brach_id = end_user_info["vendor_branch_id"]
    vendor_branch = VendorBranch.objects.filter(id=vendar_brach_id).first()
    credentials_dict = ast.literal_eval(vendor_branch.google_credentials)
    credentials = google.oauth2.credentials.Credentials(**credentials_dict)
    service = discovery.build('calendar', 'v3', credentials=credentials)

    # インサート
    event = {
        'summary': google_event_dict["summary"],
        'location': google_event_dict["location"],
        # 'description': 'ここにメモを登録できる。',
        'start': {
            'dateTime': google_event_dict["start_time"],
            'timeZone': google_event_dict["timezone"],
        },
        'end': {
            'dateTime': google_event_dict["end_time"],
            'timeZone': google_event_dict["timezone"],
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                # {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

    return event.get('htmlLink')