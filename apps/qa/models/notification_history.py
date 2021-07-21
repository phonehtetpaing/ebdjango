from django.db import models
from apps.qa.models.notification import Notification
from apps.qa.models.vendor_user import VendorUser


class NotificationHistory(models.Model):
    """ Notification History """

    notification = models.ForeignKey(Notification, verbose_name='notification', related_name='%(class)s_notification', null=False,
                               on_delete=models.CASCADE)
    vendor_user = models.ForeignKey(VendorUser, verbose_name='vendor_user', related_name='%(class)s_vendor_user', null=False,
                               on_delete=models.CASCADE)

    seen = models.BooleanField('seen', default=False, null=False)
    seen_dt = models.DateTimeField('seen datetime', null=True, blank=True)

    class Meta:
        verbose_name = "NotificationHistory"
        permissions = ()

    def __str__(self):
        return str(self.id)
