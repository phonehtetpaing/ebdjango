# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from apps.core.models.vendor_branch import VendorBranch


class VendorUser(models.Model):
    """ Vendor Users ( company admin user ) """
    auth_user = models.ForeignKey(User, related_name='%(class)s_user', null=True, on_delete=models.CASCADE)
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)

    last_name = models.CharField('last name', null=True, max_length=64)
    first_name = models.CharField('first name', null=True, max_length=64)
    last_name_kana = models.CharField('last name kana', null=True, max_length=64)
    first_name_kana = models.CharField('first name kana', null=True, max_length=64)
    email = models.CharField('email', null=True, blank=False, max_length=255, unique=True)
    # Facebook
    facebook_sender_id = models.CharField('sender id', null=True, max_length=256)
    # LINE
    line_user_id = models.CharField('user_id', null=True, max_length=64)
    is_active = models.BooleanField('active flg', default=1)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "VendorUser"
        permissions = ()

    def __str__(self):
        return self.last_name
