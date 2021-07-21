# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor import Vendor


class VendorBusinessPartnerTag(models.Model):
    """ Vendor Business Partner """
    vendor = models.ForeignKey(Vendor, verbose_name='Vendor_BusinessPartnerTag', related_name='%(class)s_vendor_business_partner_tag', null=True,on_delete=models.CASCADE)
    name = models.CharField('tag name', null=True, max_length=256)
    # cd = vendor_id_id
    cd = models.CharField('tag code', null=True, max_length=256)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "VendorBusinessPartnerTag"
        permissions = ()

    def __str__(self):
        return str(self.vendor) + '-' + self.name
