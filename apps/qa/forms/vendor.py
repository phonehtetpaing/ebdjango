# -*- Coding: utf-8 -*-
from django import forms
from django.forms import ClearableFileInput
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from apps.qa.models.vendor_user import VendorUser
from apps.core.models import Vendor


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'forms/custom_fileinput_widget.html'


class VendorUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=2048, label=_("Email address"), required=True)
    tel = forms.CharField(max_length=32, label=_("lbl_tel"), required=False)

    first_name = forms.CharField(max_length=64, label=_("lbl_first_name"), required=False)
    last_name = forms.CharField(max_length=64, label=_("lbl_last_name"), required=False)
    first_name_kana = forms.CharField(max_length=64, label=_("lbl_first_name"), label_suffix=_('lbl_kana'),
                                      required=False)
    last_name_kana = forms.CharField(max_length=64, label=_("lbl_last_name"), label_suffix=_('lbl_kana'), required=False)

    class Meta:
        model = VendorUser
        fields = ('last_name', 'first_name', 'last_name_kana', 'first_name_kana',  'email', 'tel',)
        exclude = ('auth_user', 'vendor_branch',)

    def clean_email(self):
        auth_user = self.instance.auth_user
        new_email = self.cleaned_data.get('email')
        # if the email changes verify we don't steal another auth account
        if auth_user.username != new_email:
            existing_auth_user = User.objects.filter(username=new_email)
            if existing_auth_user:
                raise forms.ValidationError("Sorry, that email is already in use. Please try again.")

        return self.cleaned_data.get('email')

    def save(self, commit=True):
        instance = super(VendorUserForm, self).save(commit=False)
        if commit:
            auth_user = self.instance.auth_user
            auth_user.username = self.cleaned_data.get('email')
            auth_user.email = self.cleaned_data.get('email')
            auth_user.save()
            instance.update_dt = timezone.now()
            instance.save()

        return instance


class VendorSettingsForm(forms.ModelForm):
    company_name = forms.CharField(label=_('lbl_company_name'), max_length=256, required=False)
    company_name_kana = forms.CharField(label=_('lbl_company_name'), label_suffix=_('lbl_kana'), max_length=256, required=False)
    company_url = forms.URLField(label=_('lbl_company_website'), max_length=2048, required=False)
    picture_url = forms.ImageField(label=_('lbl_picture_url'), widget=CustomClearableFileInput)

    class Meta:
        model = Vendor
        fields = ('company_name', 'company_name_kana', 'company_url', 'picture_url',)
