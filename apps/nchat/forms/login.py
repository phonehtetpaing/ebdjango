# -*- Coding: utf-8 -*-
import datetime
import random
import string
from django import forms
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.models import User
from apps.nchat.models.vendor_user import VendorUser
from apps.nchat.models.business import Business

from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    service = forms.CharField(label=_('Service'), max_length=255, required=True)
    username = forms.CharField(label=_('Email address'), max_length=255, required=True)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput, required=True)

    def clean(self):
        service = self.cleaned_data.get('service')
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        business = Business.objects.filter(service_name=service).first()
        vendor_user = VendorUser.objects.filter(business=business, auth_user=user).first()

        if not user or not user.is_active or not vendor_user:
            raise forms.ValidationError(_("Sorry, that login was invalid. Please try again."))
        elif not vendor_user.is_active:
            raise forms.ValidationError(_("Sorry, your account is not currently active."))
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        return user


class RegistrationForm(forms.Form):
    """ Registration form for new business + vendor_user """
    username = forms.CharField(label=_('Email address'), max_length=255, required=True)
    business_name = forms.CharField(label=_('Business Name'), min_length=3, max_length=255, required=True)
    first_name = forms.CharField(label=_('First Name'), max_length=255, required=True)
    last_name = forms.CharField(label=_('Last Name'), max_length=255, required=True)
    tel1 = forms.CharField(max_length=32, label=_("lbl_tel"), required=True)
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
        required=True,
    )
    password_confirm = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
        required=True,
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        business_name = self.cleaned_data.get('business_name')

        vendor_user = VendorUser.objects.filter(email=username)
        auth_user = User.objects.filter(username=username).first()
        user = authenticate(username=username, password=password)
        business = Business.objects.filter(business_name=business_name).first()

        if vendor_user:
            raise forms.ValidationError(_("Sorry, that email cannot be registered. Please try again."))
        # this user already exists in core but the provided password is not the current one!
        if auth_user and not user:
            raise forms.ValidationError(_("Sorry, that email cannot be registered. Please try again."))
        if password != password_confirm:
            raise forms.ValidationError(_("The two password fields didn't match."))
        if business:
            raise forms.ValidationError(_("That business name cannot be registered."))

        return self.cleaned_data

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password')
        if password:
            try:
                password_validation.validate_password(password)
            except forms.ValidationError as error:
                self.add_error('password', error)

    def register_business(self, parent=None):
        business_name = self.cleaned_data.get('business_name')
        if parent:
            parent = Business.objects.filter(service_name=parent).first().id
        business = Business(business_name=business_name, service_name=business_name, parent_id=parent)
        business.save()
        return business

    def register_user(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            user = User.objects.create_user(username=username, email=username, password=password)

        return user

    def register_vendor_user(self, service_name=None, *args, **kwargs):
        business = self.register_business(parent=service_name)
        user = self.register_user()
        vendor_user = VendorUser()
        vendor_user.auth_user = user
        vendor_user.business = business
        vendor_user.email = self.cleaned_data.get('username')
        vendor_user.tel = self.cleaned_data.get('tel1')
        vendor_user.is_active = False
        vendor_user.is_oem_admin = True

        return vendor_user

    def save(self, service_name=None):
        user = self.register_vendor_user(service_name)
        return user


def random_character(n):
    c = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(c) for i in range(n)])


def random_numbers(n):
    c = string.digits
    return ''.join([random.choice(c) for i in range(n)])
