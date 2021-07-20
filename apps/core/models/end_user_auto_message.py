# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.end_user import EndUser
from apps.core.models.auto_message_type import AutoMessageType


class EndUserAutoMessage(models.Model):
    """ Auto message target datetime for users  """
    end_user = models.ForeignKey(EndUser, verbose_name='end_user', related_name='%(class)s_end_user', null=True, on_delete=models.CASCADE)
    auto_message_type = models.ForeignKey(AutoMessageType, verbose_name='auto_message_type', related_name='%(class)s_auto_message_type', null=True, on_delete=models.CASCADE)
    message_target_dt = models.DateTimeField('target datetime', null=True)
    admin_text = models.TextField('memo for admin', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EndUserAutoMessage"
        permissions = ()

    def __str__(self):
        return self.admin_text
