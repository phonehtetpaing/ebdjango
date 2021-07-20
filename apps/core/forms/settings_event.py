from django import forms
from django.utils.translation import ugettext_lazy as _

# import models
from apps.core.models.vendor_event_settings import VendorEventSettings

WEEKDAY_HOLIDAY_CHOICES = (
    ('0', _("Mon")),
    ('1', _("Tue")),
    ('2', _("Wed")),
    ('3', _("Thu")),
    ('4', _("Fri")),
    ('5', _("Sat")),
    ('6', _("Sun")),
)


class EventSettingsForm(forms.ModelForm):
    work_start_time = forms.TimeField(label=_("lbl_title_starttime"), required=True, widget=forms.TimeInput(format='%H:%M'))
    work_end_time = forms.TimeField(label=_("lbl_title_stoptime"), required=True, widget=forms.TimeInput(format='%H:%M'))
    day_off_csv = forms.MultipleChoiceField(label=_("lbl_title_holidays"), required=True,
                                            widget=forms.CheckboxSelectMultiple,
                                            choices=WEEKDAY_HOLIDAY_CHOICES,
                                            )
    buffer_period = forms.IntegerField(label=_("lbl_time_between_schedules_minutes"), required=True)

    class Meta:
        model = VendorEventSettings
        fields = ('work_start_time', 'work_end_time', 'day_off_csv', 'buffer_period')

    def clean_day_off_csv(self):
        data = self.cleaned_data['day_off_csv']

        day_off_csv = ""
        for day in data:
            if day_off_csv == "":
                day_off_csv = day_off_csv + day
            else:
                day_off_csv = day_off_csv + "," + day
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return day_off_csv
