# -*- coding: utf-8 -*-
from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

# import models
from apps.messageflow.models.bot import Bot, Scenario


class BotForm(forms.ModelForm):

    name = forms.CharField(max_length=256, label=_("Name"), required=True)
    is_active = forms.BooleanField(label=_("Active"), required=False)

    class Meta:
        model = Bot
        fields = ('name', 'is_active',)


class BotScenarioFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(BotScenarioFormSet, self).__init__(*args, **kwargs)

        if kwargs.get('instance'):
            owner_id = kwargs['instance'].owner_id
            scenario_options = Scenario.objects.filter(owner_id=owner_id).all()
            for idx, form in enumerate(self.forms):
                    form.fields['scenario'].queryset = scenario_options


ScenarioFormSet = inlineformset_factory(Bot, Bot.scenario.through, exclude=('bot',), formset=BotScenarioFormSet)
