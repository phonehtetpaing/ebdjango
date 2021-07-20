from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ngettext_lazy

# import models
from apps.core.models import AutoMessageCondition, AutoMessageController, AutoMessageTrigger

TRIGGER_CHOICES = (
    ('False', _('lbl_trigger_before')),
    ('True', _('lbl_trigger_after')),
)


class AutoMessageTriggerForm(forms.ModelForm):
    title_name = forms.CharField()
    trigger_days_num = forms.IntegerField(label=_("tbl_title_day"), required=True)
    is_trigger_after = forms.ChoiceField(label='',
                                    widget=forms.RadioSelect(attrs={'id': 'is_trigger_after'}), choices=TRIGGER_CHOICES,
                                    initial='0', required=True)
    trigger_time = forms.TimeField(label=_("tbl_title_time"), widget=forms.TimeInput(format='%H:%M'), required=True)

    class Meta:
        model = AutoMessageTrigger
        fields = ('title_name', 'trigger_days_num', 'is_trigger_after', 'trigger_time')
