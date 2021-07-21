# -*- coding: utf-8 -*-
from django.db import models


class QuestionType(models.Model):
    """ QuestionType """
    name = models.CharField('question type name', null=False, max_length=256)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)

    class Meta:
        verbose_name = "QuestionType"
        permissions = ()

    def __str__(self):
        return str(self.name)
