from django import forms
from django.utils.translation import ugettext_lazy as _

# import models
from apps.core.models.vendor_user import VendorUser


class VendorUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=2048, label=_("Email address"), required=True)

    first_name = forms.CharField(max_length=64, label=_("lbl_first_name"), required=False)
    last_name = forms.CharField(max_length=64, label=_("lbl_last_name"), required=False)
    first_name_kana = forms.CharField(max_length=64, label=_("lbl_first_name"), label_suffix=_('lbl_kana'),
                                      required=False)
    last_name_kana = forms.CharField(max_length=64, label=_("lbl_last_name"), label_suffix=_('lbl_kana'), required=False)

    facebook_sender_id = forms.CharField(max_length=256, label=_("Facebook Messenger"), required=False)
    line_user_id = forms.CharField(max_length=256, label=_("LINE"), required=False)

    class Meta:
        model = VendorUser
        fields = ('last_name', 'first_name', 'last_name_kana', 'first_name_kana',  'email', 'facebook_sender_id', 'line_user_id')
        exclude = ['auth_user']
