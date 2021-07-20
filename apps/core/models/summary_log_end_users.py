# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.vendor import Vendor
from apps.core.models.service import Service


class SummaryLogEndUsers(models.Model):
    """ summary log End user """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch', related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, verbose_name='vendor', related_name='%(class)s_vendor', null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name='service', related_name='%(class)s_service', null=True, on_delete=models.CASCADE)
    level = models.CharField('LEVEL', null=True, max_length=64)
    log_dt = models.DateTimeField('Log Datetime', null=True)
    end_user_id = models.IntegerField(null=True, verbose_name='End User ID')
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
    message_block_id = models.IntegerField(null=True, verbose_name='Message Block ID')
    message_progress = models.CharField('Message Progress', null=True, max_length=1024)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "SummaryLogEndUser"
        permissions = ()

    def __str__(self):
        return self.ip_address
