# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_state import EndUserState
from apps.core.models.message_sequence import MessageSequence
from apps.core.models.message_block import MessageBlock


class EndUserSequenceState(models.Model):
    """ End User Sequence State  """
    user = models.ForeignKey(EndUser, verbose_name='end_user', related_name='%(class)s_end_user', null=True, on_delete=models.CASCADE)
    sequence = models.ForeignKey(MessageSequence, verbose_name='sequence', related_name='%(class)s_sequence', null=True, on_delete=models.CASCADE)
    message_block = models.ForeignKey(MessageBlock, verbose_name='message_block', related_name='%(class)s_message_block', null=True, on_delete=models.CASCADE)
    step = models.IntegerField(verbose_name='step id')
    end_user_state = models.ForeignKey(EndUserState, verbose_name='EndUserState', related_name='%(class)s_end_user_state', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "EndUserSequenceState"
        permissions = ()

    def __str__(self):
        return self.cd
