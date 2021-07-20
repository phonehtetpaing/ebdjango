# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
import datetime
import urllib.parse
import json
import requests

# import models
from apps.core.models.vendor_branch import VendorBranch

import ast
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from oauth2client.client import OAuth2WebServerFlow


# extends BaseCommand
class Command(BaseCommand):
    # python manage.py help count_entry
    help = 'Display the number of users'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        result = refresh_token()

        if result:
            # self.stdout.write(self.style.SUCCESS('count = "%s"' % articles_count))
            self.stdout.write(self.style.SUCCESS('OK'))
        else:
            self.stdout.write(self.style.SUCCESS('NG'))


def refresh_token():
    print("refresh tokens")

    redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
    base_url = r"https://accounts.google.com/o/oauth2/"

    try:
        # access_token_req = {
        #     "code": authorization_code,
        #     "client_id": client_id,
        #     "client_secret": client_secret,
        #     "redirect_uri": redirect_uri,
        #     "grant_type": "authorization_code",
        # }

        vendor_branches = VendorBranch.objects.filter(is_delete=False).exclude(google_credentials__isnull=True).all()

        print("=======")
        print(vendor_branches)

        for vendor_branch in vendor_branches:
            print("vendor_id:" + str(vendor_branch.id))
            credentials_json = vendor_branch.google_credentials.replace("\'", "\"")
            credentials_json_load = credentials_json.replace("None", "\"\"")
            credentials_dict = json.loads(credentials_json_load)

            refresh_token_req = {
                "client_id": credentials_dict["client_id"],
                "client_secret": credentials_dict["client_secret"],
                "refresh_token": vendor_branch.google_credentials_refresh_token,
                "grant_type": "refresh_token",
            }

            content_length = len(urllib.parse.urlencode(refresh_token_req))
            refresh_token_req['content-length'] = str(content_length)

            # r = requests.post(base_url + "token", data=access_token_req)
            r = requests.post(base_url + "token", data=refresh_token_req)
            data = json.loads(r.text)
            print("data:")
            print(data)

            credentials_dict["token"] = data["access_token"]
            vendor_branch.google_credentials = credentials_dict
            vendor_branch.save()

        return True

    except Exception as e:
        print('%r' % e)
        return False
