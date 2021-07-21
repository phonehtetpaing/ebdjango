import django_filters
from datetime import datetime
from django.utils.safestring import mark_safe
from django import forms
from django.utils.translation import ugettext_lazy as _
from apps.messageflow.usecases.user import AuthorizeUser


# import models
from apps.messageflow.models import EndUser


class CustomRangeWidget(django_filters.DateFromToRangeFilter):
    def __init__(self, from_attrs=None, to_attrs=None, attrs=None):
        super(CustomRangeWidget, self).__init__(attrs)

        if from_attrs:
            self.widgets[0].attrs.update(from_attrs)
        if to_attrs:
            self.widgets[1].attrs.update(to_attrs)


class TargetedMessageFilterForm(django_filters.FilterSet):
    FILTER_CHOICES = (
        ('all', _('all users')),
        ('filter', _('targeted users')),
    )

    GENDER_CHOICES = (
        ('male', _("Male")),
        ('female', _("Female")),
    )

    BIRTH_MONTH_CHOICES = (
        ('1', _('January')),
        ('2', _('February')),
        ('3', _('March')),
        ('4', _('April')),
        ('5', _('May')),
        ('6', _('June')),
        ('7', _('July')),
        ('8', _('August')),
        ('9', _('September')),
        ('10', _('October')),
        ('11', _('November')),
        ('12', _('December')),
    )

    currentYear = datetime.now().year

    #filter_all = django_filters.ChoiceFilter(initial='all', label=_("Select Users"), choices=FILTER_CHOICES, widget=forms.RadioSelect(), empty_label=None)
    filter_gender = django_filters.ChoiceFilter(label=_("Gender"), choices=GENDER_CHOICES)
    filter_birth_month = django_filters.ChoiceFilter(label=_("Birth Month"), choices=BIRTH_MONTH_CHOICES,)
    filter_birth_year = django_filters.DateFromToRangeFilter(label=mark_safe(_('Birth Date<br />(YYYY-MM-DD)')), widget=django_filters.widgets.RangeWidget(attrs={'placeholder': _('e.g.') + ' 2099-12-31'}))
    filter_regist_dt = django_filters.DateFromToRangeFilter(label=mark_safe(_('Registration Date<br />(YYYY-MM-DD)')), widget=django_filters.widgets.RangeWidget(attrs={'placeholder': _('e.g.') + ' 2099-12-31'}))

    class Meta:
        model = EndUser
        fields = ['gender']

