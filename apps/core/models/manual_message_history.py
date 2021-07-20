from django.db import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.manual_message_overview import ManualMessageOverview


class ManualMessageHistory(models.Model):
    """ ManualMessageHistory """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)

    manual_message_overview = models.ForeignKey(ManualMessageOverview, verbose_name='manual_message_overview',
                                                related_name='%(class)s_manual_message_overview', null=True,
                                                on_delete=models.CASCADE)
    admin_text = models.CharField('memo for admin', null=True, max_length=64)
    send_dt = models.DateTimeField('sent datetime', null=True)
    send_user_count = models.IntegerField("number of users", null=True)
    send_user_id_csv = models.CharField('users sent', null=True, max_length=64)
    selected_tag_csv = models.CharField('tag selected', null=True, max_length=64)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "ManualMessageHistory"
        ordering = ['-send_dt']
        permissions = ()

    def __str__(self):
        return self.admin_text
