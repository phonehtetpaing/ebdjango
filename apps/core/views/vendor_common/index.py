# -*- Coding: utf-8 -*-
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.models import User


# import models
from apps.core.models.vendor_user import VendorUser

#import views
from apps.core.views.vendor_common.login_user_info import *


def index(request):
    """ Login Index """

    if request.POST:

        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                vendor_user = VendorUser.objects.filter(auth_user_id=user.id, is_active=True, is_delete=False).first()

                if vendor_user:
                    if vendor_user.is_active:
                        login(request, user)
                        user_obj = get_login_user_objects(request)
                        return redirect(user_obj["service_url"] + '/dashboard/')

                    else:
                        # TODO : add error_obj
                        error = None
                        context = {
                            'form': form,
                            'page_name': 'Login',
                            'error': error,
                        }

                        return render(request, 'common/index.html', context)

    # New form when not the request is get.
    else:
        form = LoginForm()
        # TODO: remove
        return render(request, 'common/index.html', None)

    # if request.user.is_authenticated():
    #     return redirect('dashboard/')

    context = {
        'form': form,
        'page_name': 'Login',
    }

    return render(request, 'common/index.html', context)


class LoginForm(forms.Form):
    username = forms.CharField(label="User name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Wrong user name or passwsord")
        return self.cleaned_data
