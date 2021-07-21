# -*- coding: utf-8 -*-
from django.db import models

from apps.core.models.vendor_branch import VendorBranch
from apps.qa.models.question_type import QuestionType


class Question(models.Model):
    """ Question """
    name = models.CharField('question name', null=False, max_length=256)
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch', related_name='qa_%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(QuestionType, verbose_name='type', related_name='qa_%(class)s_type', null=False, on_delete=models.CASCADE)
    question_text = models.CharField('question text', null=False, max_length=2048, default='')
    question_options = models.CharField('question options', null=True, max_length=2048, default=None)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)

    class Meta:
        verbose_name = "Question"
        permissions = ()

    def __str__(self):
        return self.name
