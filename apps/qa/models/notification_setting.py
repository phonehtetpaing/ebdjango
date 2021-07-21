# -*- coding: utf-8 -*-
from django.db import models
from apps.qa.models.vendor_user import VendorUser
from apps.qa.models.notification_service import NotificationService


class NotificationSetting(models.Model):
    """ NotificationSetting """
    notification_service = models.ForeignKey(NotificationService, verbose_name='NotificationService', related_name='%(class)s_service', null=False,
                               on_delete=models.CASCADE)
    vendor_user = models.ForeignKey(VendorUser, verbose_name='VendorUser', related_name='%(class)s_vendor_user', null=False,
                               on_delete=models.CASCADE)
    setting_value = models.IntegerField('setting value', null=False, default=0)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "NotificationSetting"
        permissions = ()

    def __str__(self):
        return str(self.notification_service) + "-" + str(self.vendor_user)
