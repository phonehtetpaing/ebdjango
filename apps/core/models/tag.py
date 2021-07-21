# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.tag_category import TagCategory


class Tag(models.Model):
    """ TagUser """
    tag_category = models.ForeignKey(TagCategory, verbose_name='TagCategory', related_name='%(class)s_tag_category', null=True, on_delete=models.CASCADE)
    cd = models.CharField('tag code', null=True, max_length=256)
    name = models.CharField('tag name', null=True, max_length=256)
    display_order_num = models.IntegerField('display order', null=True)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Tag"
        ordering = ['id']
        permissions = ()

    def __str__(self):
        return self.name
