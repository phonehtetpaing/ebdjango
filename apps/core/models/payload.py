# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor_branch import VendorBranch


class Payload(models.Model):
    """ Payload  """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    value = models.CharField('payload value', null=True, max_length=256)
    value_alt = models.CharField('payload value', null=True, max_length=256)
    tag_name = models.CharField('payload value', null=True, max_length=64)
    tag_category_name = models.CharField('payload value', null=True, max_length=64)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Payload"
        permissions = ()

    def __str__(self):
        return self.value
