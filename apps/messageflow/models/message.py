# -*- coding: utf-8 -*-
import ast

from django.db import models
from apps.messageflow.models.bot import Scenario, Bot


class MessageType(models.Model):
    """ MessageType """
    name = models.CharField('message type name', null=False, max_length=256)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)

    class Meta:
        verbose_name = "MessageType"
        permissions = ()

    def __str__(self):
        return str(self.name)


class MessageBlock(models.Model):
    """
    MessageBlock that holds a sequence of messages
    """
    name = models.CharField(null=False, max_length=256)
    scenario = models.ForeignKey(Scenario, related_name='message_block_set', verbose_name='scenario', null=False, on_delete=models.CASCADE)

    display_order = models.IntegerField('display_order', null=True, default=-1)
    regist_dt = models.DateTimeField('regist datetime', null=False, auto_now_add=True)

    class Meta:
        verbose_name = "MessageBlock"
        permissions = ()

    def __str__(self):
        name = self.name
        if not name or name == '' or name.isspace():
            name = str(self.display_order)
        return name

    @property
    def start_message(self):
        return self.message_set.order_by('display_order').first()


class Message(models.Model):
    """ Message """
    message_block = models.ForeignKey(MessageBlock, verbose_name='message_block', null=False, on_delete=models.CASCADE)

    type = models.ForeignKey(MessageType, verbose_name='type', related_name='messageflow_%(class)s_type', blank=False, null=False, default=1, on_delete=models.CASCADE)
    json_content = models.TextField('json content', null=True, default='')
    options = models.CharField('options', null=True, blank=True, max_length=2048, default=None)

    display_order = models.IntegerField('display_order', null=True, default=-1)
    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)

    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)

    class Meta:
        verbose_name = "Message"
        permissions = ()

    def __str__(self):
        return str(self.id)

    @property
    def content(self):
        """
        Returns message formatted
        """
        if (self.json_content is None) or (self.json_content == ""):
            message_dict = {}
        else:
            message_dict = ast.literal_eval(self.json_content)

        return message_dict

    @property
    def options_dict(self):
        if (self.options is None) or (self.options == ""):
            options_dict = {}
        else:
            options_dict = ast.literal_eval(self.options)

        return options_dict


# todo we need to be able to determine in which block we are at any given time
# todo so we need to be able to query the current message for the current block and fetch the next display order message in the block to proceed
class EndUserBotScenario(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, null=False, blank=False)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=False, blank=False)
    current_message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)
    state = models.CharField('state', null=False, max_length=256, default='INITIAL')

    user_id = models.IntegerField('user_id', null=False)
    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)

    regist_dt = models.DateTimeField('regist datetime', null=False, auto_now_add=True)

    class Meta:
        verbose_name = "EndUserBotScenario"
        permissions = ()

    def __str__(self):
        return "EndUser:{2}-Bot:{0}-Scenario:{1}".format(self.bot, self.scenario, self.user_id)


class LogLine(models.Model):
    """ a logged message in an end_user_bot_scenario """
    end_user_bot_scenario = models.ForeignKey(EndUserBotScenario, verbose_name='end_user_bot_scenario', null=True, on_delete=models.SET_NULL)
    message = models.TextField('response', null=True, default='')

    user_id = models.IntegerField('user_id', null=False)
    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)

    is_user_message = models.BooleanField('is_user_message', null=False, default=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)

    class Meta:
        verbose_name = "LogLine"
        permissions = ()

    def __str__(self):
        return str(self.id)
