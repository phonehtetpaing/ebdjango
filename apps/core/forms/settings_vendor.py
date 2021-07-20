from django import forms
from django.utils.translation import ugettext_lazy as _

# import models
from apps.core.models import Vendor


class VendorSettingsForm(forms.ModelForm):
    company_name = forms.CharField(label=_('lbl_company_name'), max_length=256, required=False)
    company_name_kana = forms.CharField(label=_('lbl_company_name'), label_suffix=_('lbl_kana'), max_length=256, required=False)
    company_url = forms.URLField(label=_('lbl_company_website'), max_length=2048, required=False)
    picture_url = forms.URLField(label=_('lbl_picture_url'), max_length=2024, required=False)
    fbms_public_url = forms.URLField(label=_('lbl_fbms_public_url'), max_length=1024, required=False)
    line_public_url = forms.URLField(label=_('lbl_line_public_url'), max_length=2024, required=False)

    class Meta:
        model = Vendor
        fields = ('company_name', 'company_name_kana', 'company_url', 'picture_url', 'fbms_public_url',
                  'line_public_url')
