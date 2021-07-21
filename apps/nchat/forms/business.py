# -*- Coding: utf-8 -*-
from django import forms
from django.forms import ClearableFileInput
from froala_editor.widgets import FroalaEditor
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from apps.nchat.models.vendor_user import VendorUser
from apps.nchat.models.business import Business, BusinessPlan


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'nchat/forms/custom_fileinput_widget.html'

class BusinessForm(forms.ModelForm):
    business_name = forms.CharField(label=_('Business Name'), max_length=256, min_length=3, required=True)
    service_name = forms.CharField(label=_('Service Name'), max_length=256, min_length=3, required=True)

    logo = forms.ImageField(label=_('Logo'), widget=CustomClearableFileInput, required=False)

    class Meta:
        model = Business
        fields = ('business_name', 'service_name', 'logo',)


class BusinessPlanForm(forms.ModelForm):
    name = forms.CharField(label=_('Name'), max_length=256, min_length=1, required=True)
    price = forms.IntegerField(label=_('Price'), min_value=0, required=True)
    duration = forms.IntegerField(label=_('Duration'), min_value=0, required=True)
    description = forms.CharField(label=_("Description"), required=False,
                                  widget=FroalaEditor(options={'attribution': False}))

    class Meta:
        model = BusinessPlan
        fields = ('name', 'price', 'duration', 'description')


class VendorUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=64, label=_("lbl_first_name"), required=True)
    last_name = forms.CharField(max_length=64, label=_("lbl_last_name"), required=True)

    email = forms.EmailField(max_length=2048, label=_("Email address"), required=True)
    tel = forms.CharField(max_length=32, label=_("lbl_tel"), required=False)

    class Meta:
        model = VendorUser
        fields = ('last_name', 'first_name', 'email', 'tel',)
        exclude = ('auth_user', 'business',)

    def clean_email(self):
        auth_user = self.instance.auth_user
        new_email = self.cleaned_data.get('email')
        # if the email changes verify we don't steal another auth account
        if auth_user.username != new_email:
            existing_auth_user = User.objects.filter(username=new_email)
            if existing_auth_user:
                raise forms.ValidationError(_("Sorry, that email is already in use. Please try again."))

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
