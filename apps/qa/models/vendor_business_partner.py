# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor import Vendor


class VendorBusinessPartner(models.Model):
    """ Vendor Business Partner """
    vendor = models.ForeignKey(Vendor, verbose_name='Vendor_BusinessPartner', related_name='%(class)s_vendor_business_partner', null=True,on_delete=models.CASCADE)
    name = models.CharField('company name', null=True, max_length=256)
    short_name = models.CharField('company short name', null=True, max_length=256)
    name_kana = models.CharField('company name kana', null=True, max_length=256)
    email = models.CharField('email', null=True, max_length=2048)
    zip_code = models.CharField('zip code', null=True, max_length=20)
    prefecture = models.CharField('prefecture / state', null=True, max_length=32)
    address1 = models.CharField('address1', null=True, max_length=256)
    address2 = models.CharField('address2', null=True, max_length=256)
    tel1 = models.CharField('tel1', null=True, max_length=32)
    tel2 = models.CharField('tel2', null=True, max_length=32)
    fax = models.CharField('fax', null=True, max_length=32)
    memo = models.TextField('memo', null=True)
    tag_csv = models.CharField('Tag CSV', null=True, max_length=256)
    attribute_json = models.TextField('Attribute', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "VendorBusinessPartner"
        permissions = ()

    def __str__(self):
        return str(self.vendor) + '-' + self.name
