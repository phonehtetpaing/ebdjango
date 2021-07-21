from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ngettext_lazy
from bootstrap_datepicker_plus import DateTimePickerInput

# import models
from apps.core.models import Event, EventCategory

PUBLIC_CHOICES = (
    ('False', _("No")),
    ('True', _("Yes")),
)

GCAL_SCHEDULE_CHOICES = (
    ('False', _("lbl_google_keyword")),
    ('True', _("lbl_google_no_schedule")),
)


class EventForm(forms.ModelForm):
    is_public = forms.ChoiceField(label=_('lbl_is_public'), widget=forms.RadioSelect, choices=PUBLIC_CHOICES,
                                  initial='0')
    name = forms.CharField(label=_('tbl_title_name'), max_length=20)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'style': "height: auto"}),
                                  label=_("tbl_title_description"),
                                  required=False)
    url = forms.URLField(label=_('lbl_event_url'), max_length=2048)
    tel = forms.CharField(label=_('lbl_event_tel'), max_length=20)
    location = forms.CharField(label=_('lbl_event_location'), max_length=1024)

    class Meta:
        model = Event
        fields = ('is_public', 'name', 'description', 'url', 'tel', 'location')


class EventDateTimeForm(forms.ModelForm):
    start_dt = forms.DateTimeField(label=_("lbl_title_starttime"), widget=DateTimePickerInput().start_of('event'))
    end_dt = forms.DateTimeField(label=_("lbl_title_stoptime"), widget=DateTimePickerInput().end_of('event'))

    class Meta:
        model = Event
        fields = ('start_dt', 'end_dt')


class EventGCalSettingForm(forms.ModelForm):
    gcal_keyword = forms.CharField(label=_('lbl_event_google_keyword'), max_length=64, required=False)
    is_gcal_set = forms.ChoiceField(label=_('lbl_event_is_push_to_google_calendar'), widget=forms.RadioSelect,
                                    choices=PUBLIC_CHOICES, initial='0')

    class Meta:
        model = Event
        fields = ('gcal_keyword', 'is_gcal_set')

    def clean_gcal_keyword(self):
        data = self.cleaned_data['gcal_keyword']

        category = EventCategory.objects.filter(id=self.instance.event_category.id).first()
        if not category.is_gcal_available_time and not data:
            raise forms.ValidationError(_('This field is required.'), code='required')

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data


class EventCategoryForm(forms.ModelForm):
    is_public = forms.ChoiceField(label=_('lbl_is_public'), widget=forms.RadioSelect, choices=PUBLIC_CHOICES,
                                  initial='0')
    name = forms.CharField(label=_('lbl_event_catagory_title'), max_length=20)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'style': "height: auto"}),
                                  label=_("lbl_event_catagory_description"),
                                  required=False)

    class Meta:
        model = EventCategory
        fields = ('is_public', 'name', 'description')

    def clean_name(self):
        data = self.cleaned_data['name']

        branch_id = self.instance.vendor_branch_id
        categories = EventCategory.objects.filter(vendor_branch_id=branch_id).only('name')
        if data in categories:
            raise forms.ValidationError(_('This field is required.'), code='required')

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data


class EventCategoryGCalForm(forms.ModelForm):
    is_gcal_use = forms.ChoiceField(label=_('lbl_is_google_calendar'),
                                    widget=forms.RadioSelect(attrs={'id': 'is_gcal_use'}), choices=PUBLIC_CHOICES,
                                    initial='0')
    is_gcal_available_time = forms.ChoiceField(label=_('lbl_how_to_use_google_calendar'), widget=forms.RadioSelect,
                                               choices=GCAL_SCHEDULE_CHOICES, initial='0')
    is_user_select_event_minutes = forms.ChoiceField(label=_('lbl_is_user_select_time'),
                                                     widget=forms.RadioSelect(attrs={'id': 'is_user_select_event_minutes'}),
                                                     choices=PUBLIC_CHOICES,
                                                     initial='0')
    event_minutes_csv = forms.MultipleChoiceField(label=_("lbl_event_select_period"), required=False,
                                                  widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = EventCategory
        fields = ('is_gcal_use', 'is_gcal_available_time', 'is_user_select_event_minutes', 'event_minutes_csv')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        MINUTES_CHOICES = (
            ('30', ngettext_lazy('%d minute', '%d minutes') % 30),
            ('60', ngettext_lazy('%d minute', '%d minutes') % 60),
            ('90', ngettext_lazy('%d minute', '%d minutes') % 90),
            ('120', ngettext_lazy('%d minute', '%d minutes') % 120),
        )
        self.fields['event_minutes_csv'].choices = MINUTES_CHOICES

    def clean_event_minutes_csv(self):
        data = self.cleaned_data['event_minutes_csv']
        is_select = self.cleaned_data['is_user_select_event_minutes']

        if is_select == "True" and len(data) < 1:
            raise forms.ValidationError(_('This field is required.'), code='required')

        event_minutes_csv = None
        for minute in data:
            if event_minutes_csv is None:
                event_minutes_csv = minute
            else:
                event_minutes_csv = event_minutes_csv + "," + minute

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return event_minutes_csv
