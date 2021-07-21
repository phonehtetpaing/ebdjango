# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

# import models
from apps.qa.models.coupon import Coupon
from apps.qa.models.coupon_type import CouponType


COUPONTYPE_CHOICES = (
        ('text', _("text")),
        ('url', _("url")),
        ('questionnaire', _("questionnaire")),
)

class CouponForm(forms.ModelForm):

    name = forms.CharField(max_length=64, label=_("Name"), required=True)
    type = forms.ChoiceField(choices=COUPONTYPE_CHOICES)

    # these fields are JSON containers populated by custom BL
    data = forms.CharField(max_length=64, required=False)
    style = forms.CharField(max_length=64, required=False)

    valid_from = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datepicker'}, format='%Y-%m-%d %H:%M'),
                                 input_formats=['%Y-%m-%d %H:%M', ],
                                 label=_("Valid From"),
                                 required=True)
    valid_until = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datepicker'}, format='%Y-%m-%d %H:%M'),
                                 input_formats=['%Y-%m-%d %H:%M', ],
                                 label=_("Valid Until"),
                                 required=True)

    def clean(self):
        cleaned_type = self.cleaned_data.get('type')
        real_type = CouponType.objects.filter(name=cleaned_type).first()
        if not real_type:
            raise forms.ValidationError(_("Sorry, that coupon type cannot be found."))
        else:
            self.cleaned_data['type'] = real_type
        return self.cleaned_data

    class Meta:
        model = Coupon
        fields = ('name', 'type', 'data', 'style', 'valid_from', 'valid_until')
