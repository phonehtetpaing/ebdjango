# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor_branch import VendorBranch


class VendorEventSettings(models.Model):
    """ VendorReservationSettings """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    work_start_time = models.TimeField('work start time', null=True)
    work_end_time = models.TimeField('work end time', null=True)
    day_off_csv = models.CharField('off day', null=True, max_length=32)
    buffer_period = models.IntegerField(null=True, verbose_name='buffer minutes')
    is_google_calender_oauth = models.BooleanField('google_calender_oauth_flg', default=0)
    admin_text = models.TextField('memo for admin', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "VendorEventSettings"
        permissions = ()

    def __str__(self):
        return self.admin_text
