# -*- coding: utf-8 -*-
from django.core.validators import MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from froala_editor.fields import FroalaField


def business_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/vendor_branch_<id>/<filename>
    return 'business_{0}/avatar/{1}'.format(instance.id, filename)


class Business(MPTTModel):
    """ Business ( Client Company Information )
    parent_business is the business that owns this one (if any) Business.get(x).child_businesses() returns the set of children
    business_name is the name of the business partner
    service_name will be used generate the service name on all pages and for the platform url
    logo when set will display a custom service logo instead of the default one

    is_super_oem determines if this business can create child businesses
    """
    parent = TreeForeignKey('self', related_name='child_businesses', null=True, blank=True, on_delete=models.CASCADE)
    business_name = models.CharField('business name', unique=True, null=False, blank=False, max_length=255)
    service_name = models.CharField('service name', null=False, blank=False, max_length=255)
    logo = models.ImageField('logo', null=True, blank=True, max_length=2024, upload_to=business_directory_path)
    
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_super_oem = models.BooleanField('super oem flg', default=False)
    is_delete = models.BooleanField('delete flg', default=False)

    class Meta:
        verbose_name = "Business"
        permissions = ()

    def __str__(self):
        return self.business_name


class BusinessPlan(models.Model):
    """ Business Plan ( company payment plan ) """
    business = models.ForeignKey(Business, verbose_name='Business', null=False, on_delete=models.CASCADE)
    name = models.CharField('business plan name', null=False, blank=False, max_length=256)
    description = FroalaField()
    price = models.BigIntegerField('business plan price', null=False, default=0, validators=[MinValueValidator(0)])
    duration = models.IntegerField('duration in months', null=False, default=0)
    recurring = models.BooleanField('is recurring payment', null=False, default=True)

    regist_dt = models.DateTimeField('regist datetime', null=False, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=False, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=False)

    class Meta:
        verbose_name = "BusinessPlan"
        permissions = ()

    def __str__(self):
        return str(self.business) + '-' + str(self.name)
