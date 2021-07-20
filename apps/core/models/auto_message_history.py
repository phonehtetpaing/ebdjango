from django.db import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.auto_message_condition import AutoMessageCondition
from apps.core.models.auto_message_trigger import AutoMessageTrigger
from apps.core.models.message_status import MessageStatus


class AutoMessageHistory(models.Model):
    """ AutoMessageHistory """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    auto_message_condition = models.ForeignKey(AutoMessageCondition, verbose_name='auto_message_condition', related_name='%(class)s_auto_message_condition', null=True, on_delete=models.CASCADE)
    auto_message_trigger = models.ForeignKey(AutoMessageTrigger, verbose_name='auto_message_trigger', related_name='%(class)s_auto_message_trigger', null=True, on_delete=models.CASCADE)
    admin_text = models.CharField('memo for admin', null=True, max_length=64)
    send_dt = models.DateTimeField('sent datetime', null=True)
    send_user_count = models.IntegerField("number of users", null=True)
    send_user_id_csv = models.CharField('users sent', null=True, max_length=64)
    selected_tag_csv = models.CharField('tag selected', null=True, max_length=64)
    message_status = models.ForeignKey(MessageStatus, verbose_name='message_status',
                                       related_name='%(class)s_message_status', null=True, on_delete=models.CASCADE)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "AutoMessageHistory"
        ordering = ['-send_dt']
        permissions = ()

    def __str__(self):
        return self.admin_text
