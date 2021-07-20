# -*- Coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def index(request):
    user_obj = get_login_user_objects(request)
    redirect_url = "/"
    logout(request)

    return redirect(redirect_url)
