# -*- coding: utf-8 -*-
from django.db import models
from apps.nchat.models.business import Business


class PaymentHistory(models.Model):
    """
    History of payment from one business to another.
    Since plan names and pricing can change they are copied as is to the instance
    """
    from_business = models.ForeignKey(Business, related_name='from_business', on_delete=models.CASCADE, null=False)
    to_business = models.ForeignKey(Business, related_name='to_business', on_delete=models.CASCADE, null=False)
    plan_name = models.CharField(null=False, max_length=256)
    amount = models.BigIntegerField(null=False)
    expiration_dt = models.DateTimeField('expiration datetime', null=False, auto_now_add=False)
    regist_dt = models.DateTimeField('regist datetime', null=False, auto_now_add=True)
    status = models.IntegerField('payment status', null=False, default=1)

    class Meta:
        verbose_name = "PaymentHistory"
        permissions = ()

    def __str__(self):
        return str(self.id)
