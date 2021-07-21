# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor import Vendor
from apps.qa.models.plan import Plan


class VendorPlan(models.Model):
    """ Vendor Plan ( company QA payment plan ) """
    vendor = models.ForeignKey(Vendor, verbose_name='Vendor', related_name='%(class)s_vendor', null=True,
                               on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, verbose_name='Plan', related_name='%(class)s_plan', null=True,
                                on_delete=models.CASCADE)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "VendorPlan"
        permissions = ()

    def __str__(self):
        return str(self.vendor) + '-' + str(self.plan.name)
