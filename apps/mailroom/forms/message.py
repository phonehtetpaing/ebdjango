# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from froala_editor.widgets import FroalaEditor
from django.core.validators import validate_email
import re

# import models
from apps.core.models.vendor_branch import VendorBranch
from apps.mailroom.models.message_history import MessageHistory
from apps.mailroom.models.trigger_type import MaTriggerType
from apps.mailroom.models.trigger import MaTrigger
from apps.mailroom.models.message import Message

TRIGGERTYPE_CHOICES = (
        ('after joining', _("after joining")),
        ('after taking survey', _("after taking survey")),
        ('after using coupon', _("after using coupon")),
        ('after no activity', _("after no activity")),
        ('after new survey goes live', _("after new survey goes live")),
        ('after new coupon goes live', _("after new coupon goes live")),
        ('before coupon expires', _("before coupon expires")),
        ('before survey expires', _("before survey expires")),
        ('before birthday', _("before birthday")),
)


class MessageHistoryForm(forms.ModelForm):

    subject = forms.CharField(label=_("Subject"))
    recipients = forms.Textarea(attrs={'rows':2, 'cols':20})
    message_text = forms.CharField(label=_("Message Contents"), required=True,
                                   widget=FroalaEditor(options={'attribution': False, }))
    status = forms.IntegerField()

    class Meta:
        model = MessageHistory
        exclude = ('owner_id', 'app_id', 'send_dt',)
        widgets = {
            'recipients': forms.Textarea(attrs={'rows': 1, 'cols': 40, 'style': "min-height: calc(1.5em + .75rem + 2px)"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        dt = self.instance.send_dt
        self.data['send_dt'] = dt


class MaMessageForm(forms.ModelForm):

    subject = forms.CharField(max_length=256, label=_("Subject"), required=True)
    message_text = forms.CharField(label=_("Message Contents"), required=True, widget=FroalaEditor(options={'attribution': False,}))

    class Meta:
        model = Message
        fields = ('subject', 'message_text',)
        exclude = ('vendor_branch',)


class MaTriggerForm(forms.ModelForm):

    days = forms.IntegerField(label=_("Days"), min_value=0, required=True)
    hours = forms.IntegerField(label=_("Hours"), min_value=0, required=True)
    trigger_type = forms.ChoiceField(label=_("Event"), choices=TRIGGERTYPE_CHOICES)

    class Meta:
        model = MaTrigger
        fields = ('days', 'hours', 'trigger_type',)
        exclude = ('message',)

    def clean(self):
        self.cleaned_data = super().clean()
        trigger_type_name = self.data.get('trigger_type')
        trigger_type = MaTriggerType.objects.filter(name=trigger_type_name).first()
        if trigger_type:
            self.cleaned_data['trigger_type'] = trigger_type
        else:
            raise forms.ValidationError(_("That Trigger Type cannot be found"))
        return self.cleaned_data


class MaDirectMessageForm(forms.ModelForm):

    recipients = forms.CharField(label=_("Recipients"), required=False)
    subject = forms.CharField(max_length=255, label=_("Subject"), required=True)
    message_text = forms.CharField(label=_("Message Contents"), required=False,
                                   widget=FroalaEditor(options={'attribution': False}))

    class Meta:
        model = Message
        fields = ('recipients', 'subject', 'message_text',)

    def clean(self):
        self.cleaned_data = super().clean()
        bad_email_addresses = []
        email_recipients = re.split(r'[;,\s]\s*', self.data['email_recipients']) + re.split(r'[;,\s]\s*', self.data['recipients'])

        while "" in email_recipients:
            email_recipients.remove("")

        self.cleaned_data['recipients'] = email_recipients

        # recipient cleaning
        for i in email_recipients:
            try:
                validate_email(i)
            except:
                bad_email_addresses.append(i)
        if len(bad_email_addresses) > 0:
            self.add_error("recipients", "The following appear to be invalid email addresses: {}".format(' '.join(bad_email_addresses)))
        if len(email_recipients) == 0:
            self.add_error("recipients", "There must be at least one recipient.")

        # subject cleaning and checking for whitespace done automatically

        # message cleaning
        if len(self.data["message_text"]) == 0:
            self.add_error("message_text", "There must be some message content.")
        if len(self.data["message_text"]) > 8000:
            self.add_error("message_text", "Message content cannot exceed 8000 characters (including HTML).")
        return self.cleaned_data


    # def __init__(self, *args, **kwargs):
    #     #     image_upload_path = kwargs.pop('imageUploadURL')
    #     #     super(MaDirectMessageForm, self).__init__(*args, **kwargs)
    #     #     if image_upload_path:
    #     #         self.fields['message_text'].widget.options = {'attribution': False, 'imageUploadURL': image_upload_path}