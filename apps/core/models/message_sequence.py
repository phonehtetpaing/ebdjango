# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.message_block import MessageBlock
from apps.core.models.vendor_branch import VendorBranch


class MessageSequence(models.Model):
    """ end user conversation sequence """
    start_block = models.ForeignKey(MessageBlock, verbose_name='start_block', related_name='%(class)s_start_block', null=True, on_delete=models.CASCADE)
    admin_text = models.TextField('memo for admin', null=True)
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch', related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "MessageSequence"
        permissions = ()

    def __str__(self):
        return self.admin_text
