# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from apps.core.models.end_user import EndUser
from apps.qa.models.questionnaire_question import QuestionnaireQuestion
from apps.qa.models.end_user_questionnaire import EndUserQuestionnaire
# timezone settings
import datetime
import pytz
utc=pytz.UTC


class Response(models.Model):
    """ Response """
    end_user_questionnaire = models.ForeignKey(EndUserQuestionnaire, verbose_name='end_user_questionnaire',
                                               related_name='questionnaire_response', null=False,
                                               on_delete=models.CASCADE)
    questionnaire_question = models.ForeignKey(QuestionnaireQuestion, verbose_name='questionnaire_question',
                                      related_name='qa_%(class)s_questionnaire_question', null=False, on_delete=models.CASCADE)

    end_user = models.ForeignKey(EndUser, verbose_name='end_user',
                                      related_name='qa_%(class)s_end_user', null=False, on_delete=models.CASCADE)

    content = models.CharField('question content', null=True, max_length=2048)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)

    class Meta:
        verbose_name = "Response"
        permissions = ()

    def __str__(self):
        return 'response-' + str(self.id)

