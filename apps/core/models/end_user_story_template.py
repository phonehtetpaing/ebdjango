# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.end_user_story_template_category import EndUserStoryTemplateCategory


class EndUserStoryTemplate(models.Model):
    """ EndUserStoryTemplate """
    end_user_story_template_category = models.ForeignKey(EndUserStoryTemplateCategory, verbose_name='end_user_story_template_category', related_name='%(class)s_end_user_story_template_category', null=True, on_delete=models.CASCADE)
    payload = models.CharField('payload value', null=True, max_length=256)
    end_user_state = models.CharField('end_user_state', null=True, max_length=256)
    next_end_user_state = models.CharField('next_end_user_state', null=True, max_length=256)
    messaging_api_type = models.CharField('messaging_api_type', null=True, max_length=256)
    messaging_api_param_json = models.TextField('messaging_api_param_json', null=True)
    run_order_num = models.IntegerField('run order', null=True)
    is_todo = models.BooleanField('todo flg', default=0)
    todo_title = models.CharField('todo title', null=True, max_length=128)
    admin_text = models.TextField('memo for admin', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EndUserStoryTemplate"
        permissions = ()

    def __str__(self):
        return self.payload
