# -*- coding: utf-8 -*-
from django.db import models
from apps.qa.models.product_category import ProductCategory
from apps.qa.models.stock_space import StockSpace


class Product(models.Model):
    """ Product """
    product_category = models.ForeignKey(ProductCategory, verbose_name='ProductCategory_Product', related_name='%(class)s_product_category_product', null=True,on_delete=models.CASCADE)
    stock_space = models.ForeignKey(StockSpace, verbose_name='StockSpace_Product', related_name='%(class)s_stock_space_product', null=True,on_delete=models.CASCADE)
    name = models.CharField('product category name', null=True, max_length=256)
    code = models.CharField('product category code', null=True, max_length=256)
    memo = models.TextField('memo', null=True)
    sales_price = models.IntegerField('sales price', null=True)
    receiving_price = models.IntegerField('receiving price', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Product"
        permissions = ()

    def __str__(self):
        return str(self.product_category) + '-' + self.name
