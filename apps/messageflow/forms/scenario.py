# -*- coding: utf-8 -*-
from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet
from django.utils.translation import ugettext_lazy as _
from copy import deepcopy

# import models
from apps.messageflow.models.bot import Scenario
from apps.messageflow.models.message import Message, MessageBlock, MessageType


class ScenarioForm(forms.ModelForm):

    name = forms.CharField(max_length=256, label=_("Name"), required=True)

    class Meta:
        model = Scenario
        fields = ('name',)


class MessageBlockForm(forms.ModelForm):

    name = forms.CharField(max_length=256, label=_("Name"), required=True)

    class Meta:
        model = Scenario
        fields = ('name',)


class OrderedMessageFormSet(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(OrderedMessageFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['type'].empty_label = None

    def get_queryset(self):
        return super(OrderedMessageFormSet, self).get_queryset().order_by('display_order')

    def clean(self):
        print('testing clean', self.data)
        super().clean()

        for index, form in enumerate(self.forms):
            print("FORM.CLEANED_DATA: ", form.cleaned_data)
            message_type = form.cleaned_data.get('type')

            #if message_type
            if message_type.name == 'option':
                option_titles = form.data.getlist('message_set-{}-option-title'.format(index))
                option_payloads = form.data.getlist('message_set-{}-option-payload'.format(index))

                option_template = {'title': '', 'payload': ''}
                options = []
                for i, title in enumerate(option_titles):
                    tmp = deepcopy(option_template)
                    tmp['title'] = title
                    tmp['payload'] = option_payloads[i]
                    options.append(tmp)

                form.cleaned_data['options'] = options
                form.instance.options = options

                print('testing', option_titles, option_payloads)

    def save(self, commit=True):
        super().save(commit)


MessageFormSet = inlineformset_factory(MessageBlock, Message, form=MessageBlockForm, formset=OrderedMessageFormSet, fk_name='message_block', fields=('name', 'type', 'display_order', 'options', 'json_content'), extra=0)
