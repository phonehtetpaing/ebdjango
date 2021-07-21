# -*- coding: utf-8 -*-
from django import forms
from django.forms import modelformset_factory
from django.utils.translation import ugettext_lazy as _

# import models
from apps.qa.models.questionnaire import Questionnaire
from apps.qa.models.question import Question
from apps.qa.models.question_type import QuestionType
from apps.qa.models.questionnaire_question import QuestionnaireQuestion


class QuestionnaireForm(forms.ModelForm):

    name = forms.CharField(max_length=64, label=_("Questionaire Title"), required=True)
    intro = forms.CharField(max_length=2048, label=_("Greeting Message"), required=True, widget=forms.Textarea(attrs={'width': '100%', 'cols': '80', 'rows': '5'}))
    outro = forms.CharField(max_length=2048, label=_("Closing Message"), required=True, widget=forms.Textarea(attrs={'width': '100%', 'cols': '80', 'rows': '5'}))

    valid_from = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datepicker'}, format='%Y-%m-%d %H:%M'),
                                 input_formats=['%Y-%m-%d %H:%M',],
                                 label=_("Valid From"),
                                 required=True)
    valid_until = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datepicker'}, format='%Y-%m-%d %H:%M'),
                                 input_formats=['%Y-%m-%d %H:%M', ],
                                 label=_("Valid Until"),
                                 required=True)

    class Meta:
        model = Questionnaire
        fields = ('name', 'intro', 'outro', 'valid_from', 'valid_until')

    # AuthorFormset = modelformset_factory(
    #     Author,
    #     fields=('name', ),
    #     extra=1,
    #     widgets={
    #         'name': forms.TextInput(
    #             attrs={
    #                 'class': 'form-control',
    #                 'placeholder': 'Enter Author Name here'
    #             }
    #         )
    #     }
    # )