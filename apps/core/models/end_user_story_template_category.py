# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.service import Service


class EndUserStoryTemplateCategory(models.Model):
    """ EndUserStoryTemplateCategory """
    service = models.ForeignKey(Service, verbose_name='service', related_name='%(class)s_service', null=True, on_delete=models.CASCADE)
    name = models.CharField('name', null=True, max_length=256)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EndUserStoryTemplateCategory"
        permissions = ()

    def __str__(self):
        return self.name
