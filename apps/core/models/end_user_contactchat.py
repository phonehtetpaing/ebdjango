# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.end_user import EndUser


class EndUserContactChat(models.Model):
    """ ContactChat users  """
    end_user = models.ForeignKey(EndUser, verbose_name='end_user', related_name='%(class)s_end_user', null=True, on_delete=models.CASCADE)
    user_id = models.CharField('user_id', null=True, max_length=64)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EndUserContactChat"
        permissions = ()

    def __str__(self):
        return self.user_id
