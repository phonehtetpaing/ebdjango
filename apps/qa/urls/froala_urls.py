from django.conf.urls import url
from apps.qa.views.froala import upload

urlpatterns = [
    url(r'^image_upload/$', upload.image_upload, name='froala_editor_image_upload'),
    url(r'^file_upload/$', upload.file_upload, name='froala_editor_file_upload'),
]
