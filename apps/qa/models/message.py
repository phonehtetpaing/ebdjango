# -*- coding: utf-8 -*-
from django.db import models
from froala_editor.fields import FroalaField

from apps.core.models.vendor_branch import VendorBranch


class Message(models.Model):
    """ Message """
    subject = models.CharField('message subject', null=False, max_length=256)
    # message_text = models.CharField('question text', null=False, max_length=2048, default='')
    message_text = FroalaField()
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch', related_name='qa_%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Message"
        permissions = ()

    def __str__(self):
        return self.subject
