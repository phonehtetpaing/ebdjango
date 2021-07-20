from django.db import models
from apps.core.models.auto_message_condition import AutoMessageCondition
from apps.core.models.message_status import MessageStatus


class AutoMessageTrigger(models.Model):
    """ Auto Message Trigger settings """
    auto_message_condition = models.ForeignKey(AutoMessageCondition, verbose_name='auto_message_condition', related_name='%(class)s_auto_message_condition', null=True, on_delete=models.CASCADE)
    message_status = models.ForeignKey(MessageStatus, verbose_name='message_status', related_name='%(class)s_message_status', null=True, on_delete=models.CASCADE)
    trigger_days_num = models.IntegerField('trigger day before or after conditions', null=True)
    is_trigger_after = models.BooleanField('Triggered after ', default=1)
    trigger_time = models.TimeField('Trigger Schedule ', null=True)
    title_name = models.CharField('Title for settings', null=True, max_length=128)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "AutomessageTrigger"
        ordering = ['trigger_days_num', 'trigger_time', 'is_trigger_after']
        permissions = ()

    def __str__(self):
        return self.title_name
