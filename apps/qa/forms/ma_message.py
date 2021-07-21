# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from froala_editor.widgets import FroalaEditor

# import models
from apps.core.models import EndUser
from apps.core.models.vendor_branch import VendorBranch
from apps.qa.models.ma_trigger_type import MaTriggerType
from apps.qa.models.ma_trigger import MaTrigger
from apps.qa.models.message import Message
from apps.qa.models.questionnaire import Questionnaire
from apps.qa.models.end_user_questionnaire import EndUserQuestionnaire

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects


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

FILTER_CHOICES = (
    ('none', _('only listed emails')),
    ('all', _('all users and listed emails')),
    ('filter', _('filtered users and listed emails')),
)

GENDER_CHOICES = (
        ('any', '---------'),
        ('male', _("male")),
        ('female', _("female")),
)

BIRTH_MONTH_CHOICES = (
    ('any', '---------'),
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

class MaMessageForm(forms.ModelForm):

    subject = forms.CharField(max_length=256, label=_("Subject"), required=True)
    message_text = forms.CharField(label=_("Message Contents"), required=True, widget=FroalaEditor(options={'attribution': False, 'heightMin': 270, 'heightMax': 270,}))

    class Meta:
        model = Message
        fields = ('subject', 'message_text',)
        exclude = ('vendor_branch',)


class MaTriggerForm(forms.ModelForm):

    days = forms.IntegerField(label=_("Days"), required=True)
    hours = forms.IntegerField(label=_("Hours"), required=True)
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


def get_questionnaire_users(questionnaire_id):
    user_ids = EndUserQuestionnaire.objects.filter(questionnaire_id=questionnaire_id).values_list('end_user', flat=True)
    users = EndUser.objects.filter(id__in=user_ids).all()
    return users


class MaDirectMessageForm(forms.ModelForm):

    recipients = forms.CharField(label=_("Recipients"), required=False)
    subject = forms.CharField(max_length=256, label=_("Subject"), required=True)
    message_text = forms.CharField(label=_("Message Contents"), required=True, widget=FroalaEditor(options={'attribution': False, 'heightMin': 270, 'heightMax': 270,}))
    filter_all = forms.ChoiceField(initial='none', label=_("Select Users"), choices=FILTER_CHOICES, widget=forms.RadioSelect,)
    filter_gender = forms.ChoiceField(initial='any', label=_("Gender"), choices=GENDER_CHOICES)
    filter_birth_month = forms.ChoiceField(label=_("Birth Month"), choices=BIRTH_MONTH_CHOICES, required=False,)
    filter_completed_questionnaire = forms.ModelChoiceField(queryset=None, initial='any', label=_("Completed Questionnaire"), required=False,)

    class Meta:
        model = Message
        fields = ('recipients', 'subject', 'message_text')

    def clean(self):
        self.cleaned_data = super().clean()
        user_obj = get_login_user_objects(self.request)

        email_recipients = self.data['email_recipients'].split(",") + self.data['recipients'].split(",")
        selected_users = None

        if self.data['filter_all'] == 'filter':
            # get all filters
            selected_users = EndUser.objects.filter(vendor_branch=user_obj["vendor_branch"])
            if self.data['filter_completed_questionnaire'] and self.data['filter_completed_questionnaire'] != 'any':
                tmp_ids = get_questionnaire_users(self.data['filter_completed_questionnaire'])
                selected_users = selected_users.filter(id__in=tmp_ids)
            if self.data['filter_birth_month'] and self.data['filter_birth_month'] != 'any':
                selected_users = selected_users.filter(birth_date__month=self.data['filter_birth_month'])
            if self.data['filter_gender'] and self.data['filter_gender'] != 'any':
                selected_users = selected_users.filter(gender=self.data['filter_gender'])
        elif self.data['filter_all'] == 'all':
            selected_users = EndUser.objects.filter(vendor_branch=user_obj["vendor_branch"])

        if selected_users:
            if isinstance(email_recipients, str):
                email_recipients = [email_recipients]
            email_recipients.append(
                list(selected_users.exclude(email__isnull=True).exclude(email__exact='').values_list('email', flat=True).all()
                     )
            )

        self.cleaned_data['recipients'] = email_recipients

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        user_obj = get_login_user_objects(self.request)

        COMPLETED_QUESTIONNAIRE_CHOICES = Questionnaire.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=False).all()

        self.fields['filter_completed_questionnaire'].queryset = COMPLETED_QUESTIONNAIRE_CHOICES

    #     #     image_upload_path = kwargs.pop('imageUploadURL')
    #     #     super(MaDirectMessageForm, self).__init__(*args, **kwargs)
    #     #     if image_upload_path:
    #     #         self.fields['message_text'].widget.options = {'attribution': False, 'imageUploadURL': image_upload_path}