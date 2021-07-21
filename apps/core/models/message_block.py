# -*- coding: utf-8 -*-
import ast
from django.db import models
from apps.core.models.vendor_branch import VendorBranch


class MessageBlock(models.Model):
    """ end user conversation sequence message block """
    # api_param is converted to FBMS or LINE by wrapper method
    messaging_api_param_json = models.TextField('api parameter', null=True)
    admin_text = models.TextField('memo for admin', null=True)
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch', related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "MessageBlock"
        permissions = ()

    def __str__(self):
        return self.admin_text

    def get_messaging_api_param_json(self):
        """
        Returns message block formatted
        """
        if (self.messaging_api_param_json is None) or (self.messaging_api_param_json == ""):
            message_dict = {}
        else:
            message_dict = ast.literal_eval(self.messaging_api_param_json)

        return message_dict
