# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from apps.core.models.end_user import EndUser
from apps.qa.models.questionnaire import Questionnaire

# timezone settings
import datetime
import pytz
utc=pytz.UTC


class EndUserQuestionnaire(models.Model):
    """ EndUserQuestionnaire """
    end_user = models.ForeignKey(EndUser, verbose_name='end_user',
                                      related_name='qa_%(class)s_end_user', null=False, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, verbose_name='questionnaire',
                                      related_name='qa_%(class)s_questionnaire', null=False, on_delete=models.CASCADE)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)

    class Meta:
        verbose_name = "EndUserQuestionnaire"
        permissions = ()

    def __str__(self):
        return self.questionnaire.name + '-' + str(self.id)
