# -*- coding: utf-8 -*-
from django.db import models


class Service(models.Model):
    """ service """
    cd = models.CharField('service code', null=True, max_length=64)
    name = models.CharField('service name', null=True, max_length=256)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Service"
        permissions = ()

    def __str__(self):
        return self.name
