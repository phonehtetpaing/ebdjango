from django.urls import path
from django.conf.urls import url
from apps.core.views.google_utils import google_calendar_oauth

urlpatterns = [
    # Google Calendar Authentication
    url(r'^calender/oauth/', google_calendar_oauth.oauth, name='google_calender_oauth'),
    url(r'^calender/reoauth/', google_calendar_oauth.reoauth, name='google_calender_reoauth'),
    url(r'^calender/authorize/', google_calendar_oauth.authorize, name='google_calender_authorize'),
    url(r'^calender/oauth2callback/', google_calendar_oauth.oauth2callback,name='google_calender_oauth2callback'),

]
