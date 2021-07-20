from django.db import models
from apps.core.models.manual_message_overview import ManualMessageOverview
from apps.core.models.messaging_api_type import MessagingAPIType


class ManualMessageController(models.Model):
    """ Auto Message exec controller """
    manual_message_overview = models.ForeignKey(ManualMessageOverview, verbose_name='manual_message_overview', related_name='%(class)s_manual_message_overview', null=True, on_delete=models.CASCADE)
    messaging_api_type = models.ForeignKey(MessagingAPIType, verbose_name='messaging_api_type',
                                           related_name='%(class)s_messaging_api_type', null=True,
                                           on_delete=models.CASCADE)
    # api_param is converted to FBMS or LINE by wrapper method
    messaging_api_param_json = models.TextField('api parameter', null=True)
    run_order_num = models.IntegerField('run order', null=True)
    admin_text = models.TextField('memo for admin', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "ManualMessageController"
        permissions = ()

    def __str__(self):
        return self.admin_text
