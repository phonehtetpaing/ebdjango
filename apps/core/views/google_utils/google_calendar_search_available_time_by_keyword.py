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


def get_available_time_by_keyword(end_user_info, event_id):
    # event
    event = Event.objects.filter(id=event_id).first()

    # Google Authentication
    vendar_brach_id = end_user_info["vendor_branch_id"]
    vendor_branch = VendorBranch.objects.filter(id=vendar_brach_id).first()
    credentials_dict = ast.literal_eval(vendor_branch.google_credentials)

    credentials = google.oauth2.credentials.Credentials(**credentials_dict)
    service = discovery.build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    mex_result = 20

    event_results = service.events().list(calendarId='primary', timeMin=now, maxResults=mex_result, singleEvents=True, orderBy='startTime').execute()
    events = event_results.get('items', [])

    google_event_list = []
    for evnt in events:
        if evnt["summary"] == event.gcal_keyword:
            google_event_dict = {
                "summary": event.gcal_keyword,
                "start_time": evnt['start'].get('dateTime', evnt['start'].get('date')),
                "end_time": evnt['end'].get('dateTime', evnt['end'].get('date')),
                "location": event.location,
                "time_zone": "Asia/Tokyo",
            }

            google_event_list.append(google_event_dict)

    return google_event_list
