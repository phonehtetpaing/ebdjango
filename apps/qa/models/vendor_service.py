# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor import Vendor
from apps.qa.models.service import Service


class VendorService(models.Model):
    """ Vendor Service ( company QA service ) """
    vendor = models.ForeignKey(Vendor, verbose_name='Vendor', related_name='%(class)s_vendor', null=True,
                               on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name='Service', related_name='%(class)s_service', null=True,
                                on_delete=models.CASCADE)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "VendorService"
        permissions = ()

    def __str__(self):
        return str(self.vendor) + '-' + self.service.name
