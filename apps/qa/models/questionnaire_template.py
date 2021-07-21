# -*- coding: utf-8 -*-
from django.db import models
from apps.qa.models.question import Question
from apps.qa.models.questionnaire import Questionnaire


class QuestionnaireTemplate(models.Model):
    """ Questionnaire Template """
    name = models.CharField('template name', null=False, max_length=256)

    class Meta:
        verbose_name = "Questionnaire Template"
        permissions = ()

    def __str__(self):
        return "Questionnaire Template - " + str(self.name)
