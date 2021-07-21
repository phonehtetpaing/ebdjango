# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.event import Event
from apps.core.models.event_reservation_status import EventReservationStatus
from apps.core.models.end_user import EndUser


class EventReservation(models.Model):
    """ EventReservation """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, verbose_name='event', related_name='%(class)s_event', null=True, on_delete=models.CASCADE)
    end_user = models.ForeignKey(EndUser, verbose_name='end_user', related_name='%(class)s_end_user', null=True,
                                 on_delete=models.CASCADE)
    reservation_date = models.DateField('reservation_date', null=True)
    reservation_start_time = models.TimeField('reservation_start_time', null=True)
    reservation_end_time = models.TimeField('reservation_end_time', null=True)
    event_reservation_status = models.ForeignKey(EventReservationStatus, verbose_name='event_reservation_status', related_name='%(class)s_event_reservation_status', null=True,on_delete=models.CASCADE)
    gcal_url = models.CharField('google_calender_url', null=True, max_length=1024)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EventReservation"
        ordering = ['-id']
        permissions = ()

    def __str__(self):
        return self.gcal_url
