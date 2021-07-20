# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor import Vendor


class VendorBranch(models.Model):
    """ Vendor VendorBranch """
    vendor = models.ForeignKey(Vendor, verbose_name='Vendor', related_name='%(class)s_vendor', null=True, on_delete=models.CASCADE)
    cd = models.CharField('branch code', null=True, max_length=128)
    name = models.CharField('branch name', null=True, max_length=128)
    cd_path = models.CharField('branch code path', null=True, max_length=2024)
    join_cd = models.CharField('Client Join Code', null=True, max_length=64)
    google_credentials = models.TextField('Google Credentials', null=True)
    google_credentials_initial_code = models.TextField('Google Credentials Code', null=True)
    google_credentials_refresh_token = models.TextField('Google Credentials Code', null=True)
    is_google_calendar_ready = models.BooleanField('Google Calendar Ready flg', default=0)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "VendorBranch"
        permissions = ()

    def __str__(self):
        return self.cd
