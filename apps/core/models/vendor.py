# -*- coding: utf-8 -*-
from django.db import models
from apps.core.models.service import Service


def vendor_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/vendor_branch_<id>/<filename>
    return 'vendor_{0}/avatar/{1}'.format(instance.id, filename)


class Vendor(models.Model):
    """ Vendor ( Client Company Information )"""
    service = models.ForeignKey(Service, verbose_name='Service', related_name='%(class)s_service', null=True, on_delete=models.CASCADE)
    cd = models.CharField('contract code', null=True, max_length=64)
    company_name = models.CharField('company name', null=True, max_length=256)
    company_name_kana = models.CharField('company name kana', null=True, max_length=256)
    company_url = models.CharField('company web site url', null=True, max_length=2048)
    picture_url = models.ImageField('picture url', null=True, max_length=2024, upload_to=vendor_directory_path)
    fbms_access_url_part = models.CharField('FB Messaneger Access URL', null=True, max_length=2048)
    fbms_access_token = models.CharField('FB Access Token', null=True, max_length=2048)
    fbms_verify_token = models.CharField('FB Verify Token', null=True, max_length=256)
    fbms_public_url = models.CharField('FB Public URL', null=True, max_length=1024)
    line_access_url_part = models.CharField('LINE Access URL', null=True, max_length=2048)
    line_access_token = models.CharField('LINE Access Token', null=True, max_length=2048)
    line_verify_token = models.CharField('LINE Verify Token', null=True, max_length=256)
    line_public_url = models.CharField('LINE Public URL', null=True, max_length=1024)
    contactchat_access_url_part = models.CharField('ContactChat Access URL', null=True, max_length=2048)
    contactchat_access_token = models.CharField('ContactChat Access Token', null=True, max_length=2048)
    contactchat_verify_token = models.CharField('ContactChat Verify Token', null=False, max_length=256, default='qwerty')
    contactchat_css = models.CharField('ContactChat CSS', null=True, max_length=1024)
    oem_service_url = models.CharField('OEM Service URL', null=True, max_length=256)
    oem_service_namespace = models.CharField('OEM Service Namespace', null=True, max_length=256)
    regist_dt = models.DateTimeField('regist datetime', null=True, auto_now_add=True)
    update_dt = models.DateTimeField('update datetime', null=True, auto_now=True)
    is_delete = models.BooleanField('delete flg', default=0)

    class Meta:
        verbose_name = "Vendor"
        permissions = ()

    def __str__(self):
        return self.cd
