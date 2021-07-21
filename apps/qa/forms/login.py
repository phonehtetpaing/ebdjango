# -*- Coding: utf-8 -*-
import datetime
import random
import string
from django import forms
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.models import User
from apps.qa.models.vendor_user import VendorUser
from apps.core.models.vendor import Vendor
from apps.core.models.vendor_branch import VendorBranch
from apps.qa.models.vendor_service import VendorService
from apps.qa.models.vendor_plan import VendorPlan
from apps.qa.models.plan import Plan
from apps.qa.models.service import Service as QaService
from apps.core.models.service import Service

from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Email address'), max_length=255, required=True)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class RegistrationForm(forms.Form):
    username = forms.CharField(label=_('Email address'), max_length=255, required=True)
    vendorname = forms.CharField(label=_('Vendor Name'), min_length=4, max_length=255, required=True)
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
        vendorname = self.cleaned_data.get('vendorname')

        vendor_user = VendorUser.objects.filter(email=username)
        auth_user = User.objects.filter(username=username).first()
        user = authenticate(username=username, password=password)
        vendor = Vendor.objects.filter(company_name=vendorname).first()

        if vendor_user:
            raise forms.ValidationError(_("Sorry, that email cannot be registered. Please try again."))
        # this user already exists in core but the provided password is not the current one!
        if auth_user and not user:
            raise forms.ValidationError(_("Sorry, that email cannot be registered. Please try again."))
        if password != password_confirm:
            raise forms.ValidationError(_("The two password fields didn't match."))
        if vendor:
            # todo check for vendor admin user and email him directly for confirmation
            print('vendor already exists')

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

    def register_user(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            user = User.objects.create_user(username=username, email=username, password=password)

        return user

    def register_vendor(self):
        # get QA core.service through core.service.name
        service = Service.objects.filter(name='contactchat').first()

        # if vendor already exists use that one instead
        vendor = Vendor.objects.filter(company_name=self.cleaned_data.get('vendorname')).first()
        if vendor:
            vendor_branch = VendorBranch.objects.filter(vendor=vendor).first()
            is_new = False
        # Create New Vendor
        else:
            vendor = Vendor()
            vendor.service = service
            vendor.cd = datetime.datetime.now().strftime('%m%d-%H%M')
            vendor.company_name = self.cleaned_data.get('vendorname')

            vendor.contactchat_access_url_part = "cc" + random_character(20)
            vendor.contactchat_access_token = random_character(20)

            # Also Create new Vendor Branch
            vendor_branch = VendorBranch()
            vendor_branch.vendor = vendor
            vendor_branch.cd = "00001"
            vendor_branch.name = "branch_00001"
            vendor_branch.is_google_calendar_ready = True
            is_new = True

        return {
            'vendor': vendor,
            'vendor_branch': vendor_branch,
            'is_new': is_new,
        }

    @staticmethod
    def register_vendor_service(*args, **kwargs):
        # Also register the qa vendor_service relation
        service = QaService.objects.filter(name='QA').first()
        vendor_service = VendorService.objects.filter(vendor=kwargs['vendor']).first()
        if not vendor_service:
            vendor_service = VendorService()
            vendor_service.vendor = kwargs['vendor']
            vendor_service.service = service

        return vendor_service

    @staticmethod
    def register_vendor_plan(*args, **kwargs):
        # also register initial vendor_plan relation
        plan = Plan.objects.filter(name='Free').first()
        vendor_plan = VendorPlan.objects.filter(vendor=kwargs['vendor']).first()
        if not vendor_plan:
            vendor_plan = VendorPlan()
            vendor_plan.plan = plan
            vendor_plan.vendor = kwargs['vendor']

        return vendor_plan

    def register_vendor_user(self, *args, **kwargs):
        vendor_branch = kwargs['vendor_branch']
        user = kwargs['user']
        vendor_user = VendorUser.objects.filter(auth_user=user).first()
        if not vendor_user and vendor_branch and user:
            vendor_user = VendorUser()
            vendor_user.auth_user = user
            vendor_user.email = self.cleaned_data.get('username')
            vendor_user.tel = self.cleaned_data.get('tel1')
            vendor_user.vendor_branch = vendor_branch
            vendor_user.is_active = False

        return vendor_user


def random_character(n):
    c = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(c) for i in range(n)])


def random_numbers(n):
    c = string.digits
    return ''.join([random.choice(c) for i in range(n)])
