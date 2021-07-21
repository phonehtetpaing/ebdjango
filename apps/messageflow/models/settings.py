# -*- coding: utf-8 -*-
from django.db import models


class Settings(models.Model):
    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)
    line_access_url_part = models.CharField('line_access_url_part', null=True, max_length=2048)
    line_channel_access_token = models.CharField('line_channel_access_token', null=True, max_length=2048)
    line_channel_secret = models.CharField('line_channel_secret', null=True, max_length=256)

    class Meta:
        verbose_name = "Settings"
        permissions = ()

    def __str__(self):
        return str(self.id)
