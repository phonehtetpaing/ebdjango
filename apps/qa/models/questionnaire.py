# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from apps.core.models.vendor_branch import VendorBranch

# timezone settings
import datetime
import pytz
utc=pytz.UTC


def get_formatted_now():
    time_now = datetime.datetime.now()
    time_now = time_now.strftime("%Y-%m-%d %H:%M")
    return time_now


class Questionnaire(models.Model):
    """ Questionnaire """
    name = models.CharField('questionnaire name', null=False, max_length=256)
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='qa_%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    intro = models.CharField('intro', null=False, max_length=2048, default='')
    outro = models.CharField('outro', null=False, max_length=2048, default='')

    valid_from = models.DateTimeField('valid from datetime', null=False, default=get_formatted_now)
    valid_until = models.DateTimeField('valid until datetime', null=True, auto_now_add=False)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Questionnaire"
        permissions = ()

    def __str__(self):
        return self.name

    def status(self):
        now = datetime.datetime.now().replace(tzinfo=utc)
        if self.valid_until and self.valid_until.replace(tzinfo=utc) < now:
            return "Completed"
        elif self.valid_from and self.valid_from.replace(tzinfo=utc) < now and self.name != '':
            return "Running"
        else:
            return "Draft"
