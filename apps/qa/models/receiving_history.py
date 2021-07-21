# -*- coding: utf-8 -*-
from django.db import models
from apps.qa.models.product import Product
from apps.qa.models.vendor_business_partner import VendorBusinessPartner


class ReceivingHistory(models.Model):
    """ Receiving History """
    product = models.ForeignKey(Product, verbose_name='Product_Receiving_History', related_name='%(class)s_product_receiving_history', null=True,on_delete=models.CASCADE)
    business_partner = models.ForeignKey(VendorBusinessPartner, verbose_name='BP_Receiving_History', related_name='%(class)s_bp_receiving_history', null=True,on_delete=models.CASCADE)
    quantity = models.IntegerField('quantity', null=True)
    price = models.IntegerField('sales price', null=True)
    issue_number = models.CharField('issue number', null=True, max_length=256)
    track_number = models.CharField('track number', null=True, max_length=256)
    scheduled_dt = models.DateTimeField('scheduled datetime', null=True)
    stats = models.IntegerField('status', null=True, default=0)
    memo = models.TextField('memo', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Receiving History"
        permissions = ()

    def __str__(self):
        return str(self.product) + '-' + str(self.business_partner)
