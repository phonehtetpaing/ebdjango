# -*- coding: utf-8 -*-
from django.db import models


class MaTriggerType(models.Model):
    """ MaTriggerType """
    name = models.CharField('ma trigger type name', null=False, max_length=256)

    class Meta:
        verbose_name = "MaTriggerType"
        permissions = ()

    def __str__(self):
        return str(self.name)
