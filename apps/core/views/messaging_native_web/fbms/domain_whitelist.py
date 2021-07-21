import json, requests, random, re
import time
import hashlib
from copy import deepcopy
from urllib.parse import urlparse
from django.conf import settings
from django.views import generic
from django.http.response import HttpResponse
from django.core.cache import cache
from decouple import config


def get_url(url):
    return '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(url))


def add_whitelist(end_user_facebook, url):
    fbms_access_token = end_user_facebook.end_user.vendor_branch.vendor.fbms_access_token
    post_profile_url = settings.FB_PROFILE_URL + fbms_access_token

    # Get domain whitelist from cache
    old_whitelist = get_whitelist(end_user_facebook)
    new_whitelist = deepcopy(old_whitelist)
    # Facebook stores up to 48 whitelisted entries
    # We want to kick out the oldest url if n > 48 and always keep the ROOT_URL
    if settings.ROOT_URL + "/" not in old_whitelist:
        new_whitelist.insert(0, settings.ROOT_URL + "/")
    if "https" in url and get_url(url) not in old_whitelist:
        new_whitelist.insert(1, get_url(url))

    # trim old entries to keep only the 48 freshest ones
    response_msg = json.dumps(
                {
                    "whitelisted_domains": new_whitelist[0:48]
                }
            )

    # if no changes occurred just serve the cached version
    print('DEBUG WHITELIST, old: ', old_whitelist, ' new: ', new_whitelist)
    if old_whitelist == new_whitelist:
        return old_whitelist
    else:
        try:
            status = requests.post(post_profile_url, headers={"Content-Type": "application/json"}, data=response_msg)
            time.sleep(settings.SLEEP_SEC)

            # cache the new whitelist to prevent future api hits
            key = hashlib.sha256(fbms_access_token.encode() + fbms_access_token.encode()).hexdigest()
            set_cache_list(key, new_whitelist)
            print('DEBUG AFTER FB REQUEST STATUS: ', status)

            return status

        except Exception as e:
            print("ERROR: whitelist_api")
            print('%r' % e)
            return None


def set_cache_list(key, list):
    # Only stores lists in cache if REDIS cache location has been explicitly set
    if config('REDIS_LOCATION'):
        cache.set("whitelist-" + key, list, nx=True)


def get_cache_list(key):
    cached_list = None
    if config('REDIS_LOCATION'):
        cached_list = cache.get("whitelist-" + key)
    return cached_list


def get_whitelist(end_user_facebook):
    # For Facebook whitelisting we use a Write Through Cache,
    # in order to minimize the amount of API calls made to Facebook servers
    # we keep a whitelist in cache and only update the Facebook whitelist if
    # new entries are added that were previously not in the cache.
    fbms_access_token = end_user_facebook.end_user.vendor_branch.vendor.fbms_access_token
    key = hashlib.sha256(fbms_access_token.encode() + fbms_access_token.encode()).hexdigest()
    cached_list = get_cache_list(key)

    if cached_list:
        return cached_list
    else:
        try:
            post_profile_url = settings.FB_PROFILE_WHITELIST_URL + fbms_access_token
            result = requests.get(post_profile_url, headers={"Content-Type": "application/json"}).json()

            # check if results contain data
            if result and result.get("data") and len(result.get("data")) > 0:
                return result.get("data")[0]["whitelisted_domains"]
            else:
                return []
        except Exception as e:
            print("ERROR: get_whitelist")
            print('%r' % e)
            return []
