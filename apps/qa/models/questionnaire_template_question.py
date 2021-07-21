# -*- coding: utf-8 -*-
from django.db import models
from apps.qa.models.question import Question
from apps.qa.models.questionnaire_template import QuestionnaireTemplate


class QuestionnaireTemplateQuestion(models.Model):
    """ Questionnaire Template Question """
    questionnaire_template = models.ForeignKey(QuestionnaireTemplate, verbose_name='questionnaire template', related_name='qa_%(class)s_questionnaire', null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name='question', related_name='qa_%(class)s_question', null=False, on_delete=models.CASCADE)

    display_order = models.IntegerField('display order', default=0)
    required = models.BooleanField('required', default=True)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)

    class Meta:
        verbose_name = "Questionnaire Template Question"
        permissions = ()

    def __str__(self):
        return "Questionnaire Template Question - " + str(self.id)
