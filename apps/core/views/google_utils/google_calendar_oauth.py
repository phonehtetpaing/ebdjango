# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
import httplib2
import os
import urllib

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

from django.conf import settings

import datetime
import pytz
from django.contrib.auth.decorators import login_required

# import models

# import views
from apps.core.views.vendor_common.login_user_info import *


try:
    import argparse
    # flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
# SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'SMART BOT Google Calendar Connector'


@login_required
def authorize(request):
    """ Google Authentication """
    home_api_dir = get_home_api_dir(request)
    client_secret_file_path = os.path.join(home_api_dir, CLIENT_SECRET_FILE)

    # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(client_secret_file_path, scopes=SCOPES)
    flow.redirect_uri = settings.GOOGLE_CALLBACK_URL

    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true'
    )

    # Store the state so the callback can verify the auth server response.
    request.session['state'] = state

    return redirect(authorization_url)


@login_required
def oauth2callback(request):
    user_obj = get_login_user_objects(request)

    # Specify the state when creating the flow in the callback so that it can
    #  verified in the authorization server response.
    state = request.session['state']
    home_api_dir = get_home_api_dir(request)

    client_secret_file_path = os.path.join(home_api_dir, CLIENT_SECRET_FILE)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = request.build_absolute_uri()
    authorization_response = authorization_response.replace('http://', 'https://')
    url_parse_result = urllib.parse.urlparse(authorization_response)
    url_parse_qs_result = urllib.parse.parse_qs(url_parse_result.query)
    code = url_parse_qs_result["code"][0]

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(client_secret_file_path, scopes=SCOPES, state=state)
    flow.redirect_uri = settings.GOOGLE_CALLBACK_URL

    flow.fetch_token(authorization_response=authorization_response, code=code)

    # Store credentials in the session.
    # TODO ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    credentials = flow.credentials
    credentials_dict = credentials_to_dict(credentials)
    request.session['credentials'] = credentials_dict

    vendor_branch = user_obj["vendor_branch"]
    vendor_branch.google_credentials = credentials_dict
    vendor_branch.google_credentials_initial_code = code
    if credentials_dict["refresh_token"] is not None:
        vendor_branch.google_credentials_refresh_token = credentials_dict["refresh_token"]
    vendor_branch.save()

    return redirect('/google/calender/oauth/')


@login_required
def oauth(request):
    user_obj = get_login_user_objects(request)
    vendor_branch = user_obj["vendor_branch"]

    if 'credentials' not in request.session or vendor_branch.google_credentials is None or vendor_branch.google_credentials == "":
        return redirect('/google/calender/authorize/')

    credentials = google.oauth2.credentials.Credentials(**request.session['credentials'])

    # http = credentials.authorize(httplib2.Http())
    # service = discovery.build('calendar', 'v3', http=http)
    service = discovery.build('calendar', 'v3', credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    print('Getting the upcoming XXX events')
    mex_result = 10

    try:
        events_result = service.events().list(
            calendarId='primary', timeMin=now, maxResults=mex_result, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])

        vendor_branch.google_calender_oauth_flg = True
        vendor_branch.save()

    except Exception as e:
        print('%r' % e)
        return redirect('/google/calender/authorize/')

    redirect_url = "/" + user_obj["service_url"] + "/settings/event/"
    return redirect(redirect_url)


# TODO
# @login_required
def reoauth(request):
    user_obj = get_login_user_objects(request)
    vendor_branch = user_obj["vendor_branch"]
    vendor_branch.google_credentials = None
    vendor_branch.save()

    return redirect('/google/calender/oauth/')


# TODO:
# @login_required
def revoke(request):
    # 認証済みアカウントならば、認証情報の取り消し
    if hasattr(request.user, 'credentials'):
        request.user.credentials.revoke()
    return redirect('gservice:top')


def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }


def get_home_api_dir(request):
    user_obj = get_login_user_objects(request)

    home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    google_api_dir = os.path.join(home_dir, 'google_utils')
    home_dir = os.path.join(google_api_dir, 'calender_credential')

    # set home dir depending on the server environment
    if settings.MODE == 'PRODUCTION':
        home_mode_dir = os.path.join(home_dir, 'production')

    elif settings.MODE == 'STAGING':
        home_mode_dir = os.path.join(home_dir, 'staging')

    elif settings.MODE == 'DEV':
        home_mode_dir = os.path.join(home_dir, 'development')

    else:
        home_mode_dir = os.path.join(home_dir, 'local')

    # Service Code + Vendor Code + Vendor Branch Code
    vendor_branch = user_obj["vendor_branch"]
    credential_dir = vendor_branch.vendor.service.cd + "_" + vendor_branch.vendor.cd + "_" + vendor_branch.cd

    # home_api_dir = os.path.join(home_mode_dir, credential_dir)
    # Use the same credential file for each env.
    home_api_dir = home_mode_dir

    print("home_api_dir")
    print(home_api_dir)

    return home_api_dir
