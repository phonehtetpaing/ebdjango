import django_filters

from django import forms
from django.utils.translation import ugettext_lazy as _

from apps.nchat.models.payment import PaymentHistory


class PaymentHistoryFilter(django_filters.FilterSet):
    plan_name = django_filters.CharFilter(label=_("Plan Name"))
    status = django_filters.NumberFilter(label=_("Payment Status"))
    regist_dt = django_filters.DateFromToRangeFilter(label=_("Payment Date"))
    expiration_dt = django_filters.DateTimeFromToRangeFilter(
        widget=django_filters.fields.RangeWidget(attrs={'placeholder': _('e.g.') + ' 2099-12-31'}), label=_("Expiration Date"))

    amount = django_filters.RangeFilter(label=_("Amount"))


    class Meta:
        model = PaymentHistory
        fields = ['plan_name', 'amount', 'expiration_dt', 'regist_dt', 'status']

