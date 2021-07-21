from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.conf import settings
import json

from apps.core.models.file import File

# import views
from apps.core.views.vendor_common.login_user_info import *


class FileCreateView(CreateView):
    """
    Class based file create view.
    This view provides an upload form combined with a list view upon a GET request.
    POSTing uploads a file and validates it before returning the user from where they came.
    """
    model = File
    fields = ['upload', ]
    success_url = reverse_lazy('smart_sec:files')
    template_name = "forms/file_form.html"

    def form_valid(self, form):
        user_obj = get_login_user_objects(self.request)

        document = form.save(commit=False)
        document.vendor_branch_id = user_obj["vendor_branch"].id
        document.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        user_obj = get_login_user_objects(self.request)

        context = super().get_context_data(**kwargs)
        files = File.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id).order_by('uploaded_at')
        context['files'] = files
        context['namespace'] = user_obj["service_namespace"]
        return context


@login_required
def delete(request):
    """
    Delete view for files.
    TODO replace with API based function for asynchronous deletions.
    :param request:
    :return:
    """
    user_obj = get_login_user_objects(request)

    if request.method == "POST":
        delete_ids = request.POST.getlist('select_item')
        documents = File.objects.filter(id__in=delete_ids).all()
        for document in documents:
            document.upload.delete(save=False)
            document.upload.delete()
            document.delete()

    previous_page = request.META.get('HTTP_REFERER')
    if previous_page:
        redirect_url = previous_page
    else:
        redirect_url = "/" + user_obj["service_url"] + "/files/"

    return redirect(redirect_url)


@require_http_methods(["GET"])
def file_list(request):
    """
    API list view for files.
    This view can only be accessed by GET requests.
    Returns a queryset containing all of the files associated with the vendor_branch of the requesting user.
    :param request:
    :return:
    """
    # todo at some point improve the get_login_user function
    user_obj = get_login_user_objects(request)

    files = File.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id)

    return JsonResponse({"files": files, "total": files.count()})


@csrf_exempt
@require_http_methods(["POST"])
def file_upload(request):
    """
    API upload view for files.
    This view van only by accessed by POST requests, uploads one file at a time by looking for
    a 'file' key in the FILES portion of the request.
    :param request:
    :return:
    """
    user_obj = get_login_user_objects(request)

    # get file from POST data and upload
    file = File(upload=request.FILES['file'], vendor_branch_id=user_obj["vendor_branch"].id, size=len(request.FILES['file']))
    file.save()

    # return JSON response with file id and url
    return JsonResponse({"success": True, "file_id": file.id, "file_name": file.pretty_name, "file_url": file.upload.url})


@require_http_methods(["POST"])
def file_api(request):
    user_obj = get_login_user_objects(request)
    mode = request.POST["mode"]
    if mode == "download":
        files = list(File.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id)
                     .order_by('-uploaded_at').values_list('upload', flat=True))
        return JsonResponse({"method": "push", "mediaUrl": settings.MEDIA_URL, "files": files})
    if mode == "upload":
        print("---------------------44444444444444------------------------")
        print("request.FILES['file']", request.FILES['files'])
        file = File(upload=request.FILES['files'], vendor_branch_id=user_obj["vendor_branch"].id,
                    size=len(request.FILES['files']))
        file.save()
        print("-------------------------------------------file:", file)
        return JsonResponse({
            "method": "unshift",
            "mediaUrl": settings.MEDIA_URL,
            "files": [file.upload.url],
        })