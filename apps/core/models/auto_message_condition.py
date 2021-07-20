from django.db import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.auto_message_type import AutoMessageType


class AutoMessageCondition(models.Model):
    """ Auto Message Run Condition """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    auto_message_type = models.ForeignKey(AutoMessageType, verbose_name='auto_message_type', related_name='%(class)s_auto_message_type', null=True, on_delete=models.CASCADE)
    name = models.CharField('condition name', null=True, max_length=128)
    is_share = models.BooleanField('share flog for the same vendor', default=1)
    display_order_num = models.IntegerField('Display Order', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "AutoMessageCondition"
        ordering = ['id']
        permissions = ()

    def __str__(self):
        return self.name
