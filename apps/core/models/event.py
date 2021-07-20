# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from apps.core.models.event_category import EventCategory


# Manager that only returns events that reservations can be made for
class ReservationManager(models.Manager):
    def get_queryset(self):
        non_gcal = super().get_queryset().filter(is_public=1, start_dt__gte=datetime.now(), is_delete=0)
        gcal = super().get_queryset().filter(is_public=1, event_category__is_gcal_use=1, is_delete=0)
        return non_gcal | gcal


class Event(models.Model):
    """ Event """
    event_category = models.ForeignKey(EventCategory, verbose_name='event_category', related_name='%(class)s_event_category', null=True, on_delete=models.CASCADE)
    # Basic Settings
    name = models.CharField('Name', null=True, max_length=64)
    description = models.TextField('Description', null=True)
    url = models.CharField('Web site URL', null=True, max_length=2048)
    location = models.CharField('location', null=True, max_length=1024)
    tel = models.CharField('tel', null=True, max_length=64)
    is_public = models.BooleanField('public flg', default=0)
    capacity_num = models.IntegerField(null=True, verbose_name='number of capacity')
    # Google Calendar
    is_gcal_set = models.BooleanField('set google calender flg', default=1)
    # If EventCategory.is_gcal_use is False, set event datetime
    start_dt = models.DateTimeField('fixed schedule start datetime', null=True)
    end_dt = models.DateTimeField('fixed schedule start datetime', null=True)
    # If EventCategory.is_gcal_available_time is False, set keyword
    gcal_keyword = models.CharField('google calender keyword', null=True, max_length=64)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    # define managers
    objects = models.Manager()  # The default manager.
    available = ReservationManager()  # The reservation-specific manager.

    class Meta:
        verbose_name = "Event"
        ordering = ['-id']
        permissions = ()

    def __str__(self):
        return self.name
