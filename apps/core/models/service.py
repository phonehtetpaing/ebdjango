# -*- coding: utf-8 -*-
from django.db import models


class Service(models.Model):
    """ service """
    cd = models.CharField('service code', null=True, max_length=64)
    name = models.CharField('service name', null=True, max_length=256)
    fbms_access_url_part = models.CharField('FB Messaneger Access URL', null=True, max_length=2048)
    fbms_access_token = models.CharField('FB Access Token', null=True, max_length=2048)
    fbms_verify_token = models.CharField('FB Verify Token', null=True, max_length=256)
    line_access_url_part = models.CharField('LINE Access URL', null=True, max_length=2048)
    line_access_token = models.CharField('LINE Access Token', null=True, max_length=2048)
    line_verify_token = models.CharField('LINE Verify Token', null=True, max_length=256)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Service"
        permissions = ()

    def __str__(self):
        return self.cd
