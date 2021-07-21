# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor_user import VendorUser


class SummaryLogVendorUsers(models.Model):
    """ summary log vendor user """
    vendor_user = models.ForeignKey(VendorUser, verbose_name='vendor_user', related_name='%(class)s_vendor_user', null=True, on_delete=models.CASCADE)
    level = models.CharField('LEVEL', null=True, max_length=64)
    log_dt = models.DateTimeField('Log Datetime', null=True)
    device_type = models.IntegerField(null=True, verbose_name='Device Type')
    device_family = models.CharField('Device Family', null=True, max_length=64)
    os_family = models.CharField('OS Family ', null=True, max_length=64)
    os_version = models.CharField('OS Version ', null=True, max_length=64)
    browser_family = models.CharField('Browser Family ', null=True, max_length=64)
    browser_version = models.CharField('Browser Version ', null=True, max_length=64)
    ip_address = models.CharField('IP Address ', null=True, max_length=64)
    server_host = models.CharField('Server HOST ', null=True, max_length=64)
    status_code = models.CharField('Status Code ', null=True, max_length=64)
    content_type = models.CharField('Content Type ', null=True, max_length=64)
    http_referer = models.CharField('Http Referer ', null=True, max_length=1024)
    action_type = models.CharField('Action Type', null=True, max_length=64)
    params = models.CharField('Params', null=True, max_length=1024)
    endpoint = models.CharField('Server HOST ', null=True, max_length=1024)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "SummaryLogVendorUser"
        permissions = ()

    def __str__(self):
        return self.ip_address
