# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor_branch import VendorBranch


class Affiliate(models.Model):
    """ Affiliate """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    name = models.CharField('Name', null=True, max_length=64)
    tag_name = models.CharField('Tag Name', null=True, max_length=64)
    url_part = models.CharField('URL Part', null=True, max_length=64)
    is_active = models.BooleanField('Active flg', default=0)
    start_dt = models.DateTimeField('Start datetime', null=True)
    end_dt = models.DateTimeField('Start datetime', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Affiliate"
        permissions = ()

    def __str__(self):
        return self.name
