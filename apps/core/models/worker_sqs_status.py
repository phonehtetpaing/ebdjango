from django.db import models


class WorkerSQSStatus(models.Model):
    """ SQS Status """
    message_id = models.CharField('message_id', null=True, max_length=512)
    message = models.TextField("message", null=True)
    # status 1: In-progress 2: Done 3: Failed
    status = models.IntegerField('status', null=True)
    error_text = models.TextField("message", null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "WorkerSQSStatus"
        permissions = ()

    def __str__(self):
        return self.message_id
