# -*- coding: utf-8 -*-
from django.db import models


class EventReservationStatus(models.Model):
    """ TodoActionStatus   """
    name = models.CharField('status name', null=True, max_length=256)
    display_order_num = models.IntegerField('Display Order', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EventReservationStatus"
        permissions = ()

    def __str__(self):
        return self.name
