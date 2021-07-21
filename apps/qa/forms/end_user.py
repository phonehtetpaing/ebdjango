# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

# import models
from apps.core.models.end_user import EndUser


class EndUserForm(forms.ModelForm):

    last_name = forms.CharField(max_length=64, label=_("lbl_last_name"), required=False, disabled=True)
    first_name = forms.CharField(max_length=64, label=_("lbl_first_name"), required=False, disabled=True)
    gender = forms.CharField(max_length=25, label=_("lbl_gender"), required=False, disabled=True)
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}),
                                 input_formats=['%Y/%m/%d',],
                                 label=_("lbl_birthday"),
                                 required=False)
    email = forms.EmailField(max_length=2048, label=_("Email address"), required=False)
    tel1 = forms.CharField(max_length=32, label=_("lbl_tel"), required=False)
    zip_code = forms.CharField(max_length=20, label=_("lbl_zip"), required=False)
    prefecture = forms.CharField(max_length=32, label=_("lbl_prefecture"), required=False)

    class Meta:
        model = EndUser
        fields = ('last_name', 'first_name', 'gender', 'birth_date', 'email', 'tel1', 'zip_code',
                  'prefecture')
