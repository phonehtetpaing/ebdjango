# -*- coding: utf-8 -*-
import os
from django.db import models


def vendor_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/vendor_branch_<id>/<filename>
    return f'{instance.app_id}/{instance.owner_id}/{filename}'


class File(models.Model):
    owner_id = models.IntegerField('owner_id', null=False)
    app_id = models.CharField('app_id', null=False, max_length=256)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to=vendor_directory_path)

    @property
    def pretty_name(self):
        return os.path.basename(self.upload.name)
