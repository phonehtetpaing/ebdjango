from django.db import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.message_status import MessageStatus


class ManualMessageOverview(models.Model):
    """ Manual MEssage Overview """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    message_status = models.ForeignKey(MessageStatus, verbose_name='message_status',
                                       related_name='%(class)s_message_status', null=True, on_delete=models.CASCADE)

    name = models.CharField('name', null=True, max_length=128)
    tags = models.TextField('tags', null=True)
    is_share = models.BooleanField('share flog for the same vendor', default=0)
    push_dt = models.DateTimeField('push datetime', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "ManualMessageOverview"
        ordering = ['-id']
        permissions = ()

    def __str__(self):
        return self.name