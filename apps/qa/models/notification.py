from django.db import models


class Notification(models.Model):
    """ Notification """
    title = models.CharField('notification title', max_length=512, null=False, blank=False)
    body = models.TextField('notification body', null=False, blank=False)
    priority = models.IntegerField('notification priority', default=0, null=False)

    schedule_dt = models.DateTimeField('schedule datetime', null=False, blank=False)


    class Meta:
        verbose_name = "Notification"
        permissions = ()

    def __str__(self):
        return str(self.id)
