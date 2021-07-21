# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.end_user_state import EndUserState
from apps.core.models.payload import Payload
from apps.core.models.messaging_api_type import MessagingAPIType


class EndUserStory(models.Model):
    """ end user conversation story """
    end_user_state = models.ForeignKey(EndUserState, verbose_name='end_user_state', related_name='%(class)s_end_user_state', null=True, on_delete=models.CASCADE)
    payload = models.ForeignKey(Payload, verbose_name='payload', related_name='%(class)s_payload', null=True, on_delete=models.CASCADE)
    next_end_user_state = models.ForeignKey(EndUserState, verbose_name='next_end_user_state', related_name='%(class)s_next_end_user_state', null=True, on_delete=models.CASCADE)
    messaging_api_type = models.ForeignKey(MessagingAPIType, verbose_name='messaging_api_type', related_name='%(class)s_messaging_api_type', null=True, on_delete=models.CASCADE)
    # api_param is converted to FBMS or LINE by wrapper method
    messaging_api_param_json = models.TextField('api parameter', null=True)
    run_order_num = models.IntegerField('run order', null=True)
    is_todo = models.BooleanField('todo flg', default=0)
    todo_title = models.CharField('todo title', null=True, max_length=128)
    admin_text = models.TextField('memo for admin', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EndUserStory"
        permissions = ()

    def __str__(self):
        return self.admin_text
