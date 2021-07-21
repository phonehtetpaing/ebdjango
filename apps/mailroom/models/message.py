# -*- coding: utf-8 -*-
from django.db import models
from froala_editor.fields import FroalaField
from django.utils.translation import gettext


class Message(models.Model):
    """ Message """
    subject = models.CharField('message subject', null=False, max_length=256)
    message_text = FroalaField()
    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)

    class Meta:
        verbose_name = "Message"
        permissions = ()

    def __str__(self):
        if not self.subject or self.subject == "":
            # todo fix the following line:
            output = gettext("No Subject")
            return output
        else:
            return self.subject


class MessageTemplateCategory(models.Model):
    """ Message Template Category """

    name = models.CharField('message template category name', null=False, max_length=256)
    language_code = models.CharField('message template category name', null=False, max_length=32)

    class Meta:
        verbose_name = "MessageTemplateCategory"
        permissions = ()

    def __str__(self):
        if not self.name or self.name == "":
            return "(No Name)"
        else:
            return self.name


class MessageTemplate(models.Model):
    """ Message Template """

    name = models.CharField('message template name', null=False, max_length=256)
    language_code = models.CharField('message template category name', null=False, max_length=32)
    template_category = models.ForeignKey(MessageTemplateCategory, verbose_name='template_category',
                                      related_name='message_templates', null=False, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, verbose_name='message',
                                 related_name='mailroom_message', null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "MessageTemplate"
        permissions = ()

    def __str__(self):
        if not self.name or self.name == "":
            return "(No Name)"
        else:
            return self.name
