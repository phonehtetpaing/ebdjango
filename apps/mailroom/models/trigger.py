# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from apps.mailroom.models.trigger_type import MaTriggerType
from apps.mailroom.models.message import Message

# timezone settings
import datetime
import pytz
utc=pytz.UTC


class MaTrigger(models.Model):
    """ MaTrigger """
    days = models.IntegerField(verbose_name='days', null=False, default=0)
    hours = models.IntegerField(verbose_name='days', null=False, default=0)
    is_active = models.BooleanField(verbose_name='is_active', default=False)
    trigger_type = models.ForeignKey(MaTriggerType, verbose_name='trigger_type',
                                      related_name='mailroom_%(class)s_trigger_type', null=False, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, verbose_name='message',
                                 related_name='mailroom_%(class)s_message', null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "MaTrigger"
        permissions = ()

    def __str__(self):
        return self.trigger_type.name + '-' + str(self.id)
