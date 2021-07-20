import os
from django.db import models
from apps.core.models.vendor_branch import VendorBranch


def vendor_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/vendor_branch_<id>/<filename>
    return 'vendor_branch_{0}/{1}'.format(instance.vendor_branch.id, filename)


class Document(models.Model):
    vendor_branch = models.ForeignKey(VendorBranch, verbose_name='vendor_branch', related_name='%(class)s_vendor_branch', null=True, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to=vendor_directory_path)

    @property
    def pretty_name(self):
        return os.path.basename(self.upload.name)
