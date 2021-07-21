# -*- coding: utf-8 -*-
from django.db import models
from froala_editor.fields import FroalaField


class MessageHistory(models.Model):
    """ Message """
    subject = models.CharField('message subject', null=False, max_length=256)
    recipients = models.TextField('message recipients', null=False, blank=True)
    # message_text = models.CharField('question text', null=False, max_length=2048, default='')
    message_text = FroalaField()
    send_dt = models.DateTimeField('send_dt', null=False, auto_now_add=True)
    status = models.IntegerField('status', null=False)
    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)

    class Meta:
        verbose_name = "MessageHistory"
        permissions = ()

    def __str__(self):
        return self.subject
