# -*- coding: utf-8 -*-
from django.db import models


class TmpEntry(models.Model):
    """ TmpEntry  """
    user_agent = models.CharField('payload value', null=True, max_length=256)
    x_forwarded_for = models.CharField('payload value', null=True, max_length=256)
    branch_code = models.CharField('vendor branch code', null=True, max_length=256)
    tag_name = models.CharField('tag name', null=True, max_length=256)
    access_dt = models.DateTimeField('access datetime', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "TmpEntry"
        permissions = ()

    def __str__(self):
        return self.user_agent
