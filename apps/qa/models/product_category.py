# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor import Vendor


class ProductCategory(models.Model):
    """ Product Category """
    vendor = models.ForeignKey(Vendor, verbose_name='Vendor_ProductCategory', related_name='%(class)s_vendor_product_category', null=True,on_delete=models.CASCADE)
    name = models.CharField('product category name', null=True, max_length=256)
    code = models.CharField('product category code', null=True, max_length=256)
    memo = models.TextField('memo', null=True)
    display_order_num = models.IntegerField('display order', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "ProductCategory"
        permissions = ()

    def __str__(self):
        return str(self.vendor) + '-' + self.name
