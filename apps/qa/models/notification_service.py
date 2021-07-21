# -*- coding: utf-8 -*-
from django.db import models


class NotificationService(models.Model):
    """ NotificationService """
    name = models.CharField('notification service name', null=False, max_length=256)
    icon = models.CharField('notification service icon', null=True, max_length=256)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "NotificationService"
        permissions = ()

    def __str__(self):
        return str(self.name)
