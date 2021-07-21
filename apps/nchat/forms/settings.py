# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import validate_email
import re

# import models
from apps.nchat.models.settings import Settings
from apps.messageflow.models.settings import Settings as LineSettings


class LineWebhookSettings(forms.ModelForm):
    line_channel_secret = forms.CharField(label=_("Line Channel Secret"), required=False)
    line_channel_access_token = forms.CharField(label=_("Line Channel Access Token"), required=False)

    class Meta:
        model = LineSettings
        fields = ('line_channel_secret', 'line_channel_access_token')


class WebhookSettings(forms.ModelForm):

    line_channel_secret = forms.CharField(label=_("Line Channel Secret"), required=False)
    line_channel_access_token = forms.CharField(label=_("Line Channel Access Token"), required=False)

    class Meta:
        model = Settings
        # fields = ()
        exclude = ('content_json', 'business')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.instance.get_content(field):
                self.fields[field].initial = self.instance.get_content(field)

    def save(self, commit=True):
        data = self.cleaned_data
        for field in self.fields:
            if data.get(field) is not None:
                self.instance.set_content(field, data.get(field))


class WidgetSettings(forms.ModelForm):

    widget_theme = forms.CharField(label=_("Theme"), required=False)
    widget_font_size = forms.IntegerField(label=_("Font Size"), min_value=1, max_value=15, required=False)
    widget_font_family = forms.CharField(label=_("Font Family"), required=False)
    widget_font_style = forms.CharField(label=_("Font Style"), required=False)
    widget_text_color = forms.CharField(label=_("Text Color"), required=False)
    widget_bot_icon = forms.CharField(label=_("Bot Icon"), required=False)
    widget_user_icon = forms.CharField(label=_("User Icon"), required=False)

    class Meta:
        model = Settings
        # fields = ()
        exclude = ('content_json', 'business')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.instance.get_content(field):
                self.fields[field].initial = self.instance.get_content(field)

    def save(self, commit=True):
        data = self.cleaned_data
        if 'widget_font_size' in data:
            if data['widget_font_size'] is None:
                data['widget_font_size'] = 12
        for field in self.fields:
            if data.get(field) is not None:
                self.instance.set_content(field, data.get(field))
