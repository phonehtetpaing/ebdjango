# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.end_user import EndUser


class EndUserLINE(models.Model):
    """ Facebook users  """
    end_user = models.ForeignKey(EndUser, verbose_name='end_user', related_name='%(class)s_end_user', null=True, on_delete=models.CASCADE)
    display_name = models.CharField('display_name', null=True, max_length=256)
    user_id = models.CharField('user_id', null=True, max_length=64)
    picture_url = models.CharField('picture_url', null=True, max_length=2048)
    payload = models.CharField('payload value', null=True, max_length=256)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EndUserLINE"
        permissions = ()

    def __str__(self):
        return self.user_id
