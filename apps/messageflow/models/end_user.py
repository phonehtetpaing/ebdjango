# -*- coding: utf-8 -*-
import ast
import json
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class EndUser(models.Model):
    """ End users  """
    auth_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    tag = TaggableManager(related_name='user_tag', blank=True)

    last_name = models.CharField('last name', null=False, blank=False, max_length=64)
    first_name = models.CharField('first name', null=False, blank=False, max_length=64)
    gender = models.CharField('gender', null=True, max_length=25)
    birth_date = models.DateField('birth day', null=True)

    email = models.CharField('email', null=False, blank=False, max_length=255)
    tel = models.CharField('tel', max_length=32, null=True)

    attribute_json = models.TextField('Attribute', null=True)

    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)

    last_login_dt = models.DateTimeField('login datetime', null=True)
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
                attribute_dict = {}
            else:
                print('self.attribute_json', self.attribute_json)
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
