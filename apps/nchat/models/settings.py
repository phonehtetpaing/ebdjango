# -*- coding: utf-8 -*-
import ast

from django.db import models
from apps.nchat.models.business import Business

import json


class Settings(models.Model):
    business = models.ForeignKey(Business,
                                 verbose_name='business',
                                 related_name='nchat_%(class)s_business',
                                 null=False,
                                 on_delete=models.CASCADE)
    content_json = models.TextField(verbose_name='business', null=True)

    def get_content(self, key=None):
        if self.content_json is None or self.content_json == "":
            self.content_json = "{}"
            self.save()
        content_dict = ast.literal_eval(self.content_json)
        if not key:
            return content_dict
        else:
            return content_dict.get(key, None)

    def set_content(self, key, value):
        content_dict = self.get_content()
        content_dict[key] = value
        self.content_json = json.dumps(content_dict)
        self.save()

    class Meta:
        verbose_name = "Settings"
        permissions = ()

    def __str__(self):
        return str(self.id)
