# -*- coding: utf-8 -*-
import ast
import json
from django.db import models
from django.contrib.auth.models import User
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.end_user_state import EndUserState
from taggit.managers import TaggableManager


class EndUser(models.Model):
    """ End users  """
    auth_user = models.ForeignKey(User, related_name='%(class)s_user', null=True, on_delete=models.CASCADE)
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch', related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    end_user_state = models.ForeignKey(EndUserState, verbose_name='EndUserState', related_name='%(class)s_end_user_state', null=True, on_delete=models.CASCADE)
    tag = TaggableManager(blank=True)
    django_pass_cd = models.CharField('django user login password', null=True, max_length=2048)
    last_name = models.CharField('last name', null=True, max_length=64)
    first_name = models.CharField('first name', null=True, max_length=64)
    last_name_kana = models.CharField('last name kana', null=True, max_length=64)
    first_name_kana = models.CharField('first name kana', null=True, max_length=64)
    gender = models.CharField('gender', null=True, max_length=25)
    age = models.CharField('age', null=True, max_length=25)
    birth_date = models.DateField('birth day', null=True)
    email = models.CharField('email', null=True, max_length=2048)
    zip_code = models.CharField('zip code', null=True, max_length=20)
    prefecture = models.CharField('prefecture / state', null=True, max_length=32)
    address1 = models.CharField('address1', null=True, max_length=256)
    address2 = models.CharField('address2', null=True, max_length=256)
    tel1 = models.CharField('tel1', null=True, max_length=32)
    tel2 = models.CharField('tel2', null=True, max_length=32)
    admin_text = models.TextField('memo for admin', null=True)
    attribute_json = models.TextField('Attribute', null=True)
    last_login_dt = models.DateTimeField('login datetime', null=True)
    reservation_data_json = models.TextField('reservation data(json)', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)
    subscribed = models.BooleanField('subscribe flg', default=1)

    class Meta:
        verbose_name = "EndUser"
        permissions = ()

    def __str__(self):
        return self.last_name

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        if not self.first_name and not self.last_name:
            return u'%s %s' % ('Anonymous User', self.id)
        full_name = u'%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_attribute_json(self, key=None):
        """
        Returns the specified user json attribute by name.
        If no key is specified the entire dict is returned instead.
        """
        if key is None:
            if (self.attribute_json is None) or (self.attribute_json == ""):
                attribute_dict = {
                    '_form_length': 0,
                    '_form_step': 0
                }
            else:
                attribute_dict = ast.literal_eval(self.attribute_json)

            return attribute_dict

        attribute_dict = self.get_attribute_json()
        return attribute_dict.get(key)

    def set_attribute_json(self, key, value):
        """
        Sets the specified user json attribute in the user json attribute object.
        """
        attribute_dict = self.get_attribute_json()
        attribute_dict[key] = value
        self.attribute_json = json.dumps(attribute_dict)
        self.save()

    @property
    def business_name(self):
        return self.get_attribute_json('business_name')

    @business_name.setter
    def business_name(self, value):
        self.set_attribute_json('business_name', value)

    @property
    def instagram_id(self):
        return self.get_attribute_json('instagram_id')

    @instagram_id.setter
    def instagram_id(self, value):
        self.set_attribute_json('instagram_id', value)
