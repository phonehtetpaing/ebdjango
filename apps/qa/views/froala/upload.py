import json
# from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
import os
from django.utils.translation import ugettext_lazy as _
from django.utils.module_loading import import_string


# Allow for a custom storage backend defined in settings.
from apps.qa.views.common.login_user_info import get_login_user_objects


def get_storage_class():
    return import_string(getattr(settings, 'FROALA_STORAGE_BACKEND', 'django.core.files.storage.DefaultStorage'))()


def vendor_directory_path(vendor_branch):
    # file will be uploaded to MEDIA_ROOT/vendor_branch_<id>/<filename>
    return 'vendor_branch_{0}/froala/'.format(vendor_branch.id)


storage = get_storage_class()


def image_upload(request):
    user_obj = get_login_user_objects(request)
    vendor_branch = user_obj["vendor_branch"]

    if 'file' in request.FILES:
        the_file = request.FILES['file']
        allowed_types = [
            'image/jpeg',
            'image/jpg',
            'image/pjpeg',
            'image/x-png',
            'image/png',
            'image/gif'
        ]
        if not the_file.content_type in allowed_types:
            return HttpResponse(json.dumps({'error': _('You can only upload images.')}),
                                content_type="application/json")
        # Other data on the request.FILES dictionary:
        # filesize = len(file['content'])
        # filetype = file['content-type']

        upload_to = vendor_directory_path(vendor_branch)
        path = storage.save(os.path.join(upload_to, the_file.name), the_file)
        link = request.build_absolute_uri(storage.url(path))

        # return JsonResponse({'link': link})
        return HttpResponse(json.dumps({'link': link}), content_type="application/json")


def file_upload(request):
    user_obj = get_login_user_objects(request)
    vendor_branch = user_obj["vendor_branch"]

    if 'file' in request.FILES:
        the_file = request.FILES['file']
        upload_to = vendor_directory_path(vendor_branch)
        path = storage.save(os.path.join(upload_to, the_file.name), the_file)
        link = storage.url(path)
        return HttpResponse(json.dumps({'link': link}), content_type="application/json")
