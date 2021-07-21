# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor_branch import VendorBranch


class EventCategory(models.Model):
    """ EventCategory """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    name = models.CharField('Name', null=True, max_length=64)
    description = models.TextField('Description', null=True)
    display_order_num = models.IntegerField('Display Order', null=True)
    is_public = models.BooleanField('public flg', default=0)
    # Google Calendar (gcal) Settings
    is_gcal_use = models.BooleanField('use google calender flg', default=0)
    is_gcal_available_time = models.BooleanField('available time flg', default=0)
    # User can set MTG minutes or not.
    is_user_select_event_minutes = models.BooleanField('user can select the event minutes', default=0)
    event_minutes_csv = models.CharField('Event Minutes (CSV) ', null=True, max_length=64)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EventCategory"
        ordering = ['-id']
        permissions = ()

    def __str__(self):
        return self.name
