from django.db import models


class MessageStatus(models.Model):
    """ Message Status """
    name = models.CharField('Title for settings', null=True, max_length=128)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "MessageStatus"
        permissions = ()

    def __str__(self):
        return self.name
