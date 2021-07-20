# -*- coding: utf-8 -*-
from django.db import models


class LogsHistory(models.Model):
    """ Logs History  """
    event_start_dt = models.DateTimeField('Event Start datetime', null=True)
    event_end_dt = models.DateTimeField('Event Start datetime', null=True)
    is_athena_query = models.BooleanField('run athena query flg', default=False)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "event_start_dt"
        permissions = ()

    def __str__(self):
        return self.event_start_dt
