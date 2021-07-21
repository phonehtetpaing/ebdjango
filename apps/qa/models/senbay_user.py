# -*- coding: utf-8 -*-
from django.db import models
from apps.qa.models.vendor_user import VendorUser


class SenbayUser(models.Model):
    """ Vendor Users ( company admin user ) """
    vendor_user = models.ForeignKey(VendorUser, related_name='qa_%(class)s_vendor_user', null=True, on_delete=models.CASCADE)
    jwt_token = models.CharField('last name', null=True, max_length=1024)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_active = models.BooleanField('active flg', default=False)
    is_delete = models.BooleanField('delete flg', default=False)

    class Meta:
        verbose_name = "SenbayUser"
        permissions = ()

    def __str__(self):
        return self.jwt_token
