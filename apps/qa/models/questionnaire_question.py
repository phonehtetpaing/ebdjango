# -*- coding: utf-8 -*-
from django.db import models
from apps.qa.models.question import Question
from apps.qa.models.questionnaire import Questionnaire


class QuestionnaireQuestion(models.Model):
    """ Questionnaire Question """
    questionnaire = models.ForeignKey(Questionnaire, verbose_name='questionnaire', related_name='qa_%(class)s_questionnaire', null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name='question', related_name='qa_%(class)s_question', null=False, on_delete=models.CASCADE)

    display_order = models.IntegerField('display order', default=0)
    required = models.BooleanField('required', default=True)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)

    class Meta:
        verbose_name = "Questionnaire Question"
        permissions = ()

    def __str__(self):
        return "Questionnaire Question - " + str(self.id)
