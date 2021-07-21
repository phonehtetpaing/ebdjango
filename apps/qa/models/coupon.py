# -*- coding: utf-8 -*-
import qrcode
from django.conf import settings
from django.core.files import File
from django.db import models
from django.utils import timezone
# from django.utils.datetime_safe import datetime

from apps.core.models.vendor_branch import VendorBranch
from apps.qa.models.coupon_type import CouponType

import datetime
import pytz

utc=pytz.UTC


def get_formatted_now():
    time_now = datetime.datetime.now()
    time_now = time_now.strftime("%Y-%m-%d %H:%M")
    return time_now


def vendor_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/qrcodes/<filename>
    return 'qrcodes/{0}'.format(filename)


class Coupon(models.Model):
    """ Coupon """
    name = models.CharField('coupon name', null=False, max_length=256)
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    type = models.ForeignKey(CouponType, verbose_name='CouponType', related_name='%(class)s_type', null=False,
                             on_delete=models.CASCADE)
    qrcode = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    data = models.CharField('coupon data contents', null=True, max_length=256)
    style = models.CharField('coupon data contents', null=True, max_length=256)
    valid_from = models.DateTimeField('valid from datetime', null=False, default=get_formatted_now)
    valid_until = models.DateTimeField('valid until datetime', null=True, auto_now_add=False)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Coupon"
        permissions = ()

    def __str__(self):
        return str(self.name)

    def save(self):
        # Generate qrcode before calling super.save
        self.generate_qrcode()
        super(Coupon, self).save()

    def status(self):
        now = datetime.datetime.now().replace(tzinfo=utc)
        if self.valid_until and self.valid_until.replace(tzinfo=utc) < now:
            return "Expired"
        elif self.valid_from and self.valid_from.replace(tzinfo=utc) < now and self.name != '':
            return "Running"
        else:
            return "Draft"

    def generate_qrcode(self):
        """
            generates a new QR code if one doesn't already exist
            we only need to save once since the QR code will ALWAYS redirect to the QA system
        """
        if not self.qrcode and self.id:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            data_to_add = "{0}/qa/coupon/claim/{1}/".format(settings.ROOT_URL, self.id)
            qr.add_data(data_to_add)
            qr.make(fit=True)

            filename = 'qrcode-%s.png' % self.id

            img = qr.make_image()
            img.save('{0}{1}'.format(settings.MEDIA_ROOT, filename))

            with open('{0}{1}'.format(settings.MEDIA_ROOT, filename), "r+b") as reopen:
                django_file = File(reopen)
                self.qrcode.save(filename, django_file, save=False)
