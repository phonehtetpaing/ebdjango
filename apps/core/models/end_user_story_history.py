# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.end_user_story import EndUserStory
from apps.core.models.end_user import EndUser
from apps.core.models.todo_action_status import TodoActionStatus


class EndUserStoryHistory(models.Model):
    """ End User Story History """
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch',
                                      related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    end_user_story = models.ForeignKey(EndUserStory, verbose_name='end_user_story', related_name='%(class)s_end_user_story', null=True, on_delete=models.CASCADE)
    end_user = models.ForeignKey(EndUser, verbose_name='end_user', related_name='%(class)s_end_user', null=True,
                                 on_delete=models.CASCADE)
    end_user_reply = models.CharField('reply text or payload', null=True, max_length=2048)
    is_todo = models.BooleanField('delete flg', default=0)
    todo_action_status = models.ForeignKey(TodoActionStatus, verbose_name='todo_action_status', related_name='%(class)s_todo_action_status', null=True, on_delete=models.CASCADE)
    memo = models.TextField('memo', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "EndUserStoryHistory"
        permissions = ()

    def __str__(self):
        return self.end_user_reply
