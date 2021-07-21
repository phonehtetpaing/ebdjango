# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from apps.nchat.models.business import Business


class VendorUser(models.Model):
    """ Vendor Users ( company admin user ) """
    auth_user = models.ForeignKey(User, related_name='nchat_%(class)s_user', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, verbose_name='parent_business',
                                      related_name='nchat_%(class)s_parent_business', null=True, on_delete=models.CASCADE)

    last_name = models.CharField('last name', null=False, blank=False, max_length=64)
    first_name = models.CharField('first name', null=False, blank=False, max_length=64)
    email = models.CharField('email', null=False, blank=False, max_length=255, unique=True)
    tel = models.CharField('tel', max_length=32, null=True)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)

    is_oem_admin = models.BooleanField('oem admin flg', default=False)
    is_active = models.BooleanField('active flg', default=False)
    is_delete = models.BooleanField('delete flg', default=False)

    class Meta:
        verbose_name = "VendorUser"
        permissions = ()

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        if not self.first_name and not self.last_name:
            return u'%s %s' % ('Anonymous User', self.id)
        full_name = u'%s %s' % (self.first_name, self.last_name)
        return full_name.strip()