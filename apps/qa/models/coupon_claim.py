# -*- coding: utf-8 -*-
from django.db import models
from apps.qa.models.coupon import Coupon
from apps.core.models.end_user import EndUser


class CouponClaim(models.Model):
    """ CouponClaim """
    end_user = models.ForeignKey(EndUser, verbose_name='end_user', related_name='%(class)s_end_user', null=False,
                                 on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, verbose_name='Coupon', related_name='%(class)s_coupon', null=False,
                                on_delete=models.CASCADE)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "CouponClaim"
        permissions = ()

    def __str__(self):
        return self.coupon.name
