# -*- coding: utf-8 -*-
from django.db import models
from apps.qa.models.product import Product


class Stock(models.Model):
    """ Stock """
    product = models.ForeignKey(Product, verbose_name='Product_Stock', related_name='%(class)s_product_stock', null=True,on_delete=models.CASCADE)
    quantity = models.IntegerField('quantity', null=True)
    memo = models.TextField('memo', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Stock"
        permissions = ()

    def __str__(self):
        return str(self.product) + '-' + self.memo
