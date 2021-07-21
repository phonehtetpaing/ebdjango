# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.end_user import EndUser


class EndUserFacebook(models.Model):
    """ Facebook users  """
    end_user = models.ForeignKey(EndUser, verbose_name='end_user', related_name='%(class)s_end_user', null=True, on_delete=models.CASCADE)
    sender_id = models.CharField('sender id', null=True, max_length=256)
    last_name = models.CharField('last name', null=True, max_length=64)
    first_name = models.CharField('first name', null=True, max_length=64)
    gender = models.CharField('gender', null=True, max_length=25)
    locale = models.CharField('locale', null=True, max_length=25)
    profile_pic_url = models.CharField('profile picture url', null=True, max_length=2024)
    timezone = models.IntegerField('timezone', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EndUserFacebook"
        permissions = ()

    def __str__(self):
        return self.sender_id
