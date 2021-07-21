import django_filters
from django import forms
from django.utils.translation import ugettext_lazy as _

from apps.core.models.end_user import EndUser
from apps.core.models.tag import Tag

from apps.core.views.vendor_common.login_user_info import *


class UserFilter(django_filters.FilterSet):
    GENDER_CHOICES = (
        ('male', _("lbl_gender_male")),
        ('female', _("lbl_gender_female")),
    )

    first_name = django_filters.CharFilter(label=_('lbl_first_name'), lookup_expr='icontains')
    last_name = django_filters.CharFilter(label=_('lbl_last_name'), lookup_expr='icontains')
    gender = django_filters.ChoiceFilter(label=_('lbl_gender'), choices=GENDER_CHOICES)
    tag = django_filters.ModelMultipleChoiceFilter(queryset=EndUser.tag.all(),
                                                      widget=forms.CheckboxSelectMultiple(attrs={'hidden': True,
                                                                                                 'onchange': 'filterform.submit();'}))

    class Meta:
        model = EndUser
        fields = ['gender']
