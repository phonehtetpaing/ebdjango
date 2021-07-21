from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

import ast

# import views
from django.views.generic.edit import CreateView

# import models
from apps.nchat.models.settings import Settings
from apps.messageflow.models.settings import Settings as LineSettings
from apps.messageflow.models.bot import Bot
from apps.nchat.models.file import File

# import forms
from apps.nchat.forms.settings import WebhookSettings, WidgetSettings, LineWebhookSettings

# import use cases
from apps.nchat.usecases.user import AuthorizeUser


@login_required(login_url='/nchat/')
def index(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']
    user_settings = Settings.objects.filter(business_id=user_business.id).first()

    if not user_settings:
        user_settings = Settings(business=user_business)

    if request.POST:
        settings_form = WidgetSettings(request.POST, instance=user_settings)
        if settings_form.is_valid():
            settings_form.save()
        else:
            print("form is not valid: ", settings_form)
    else:
        settings_form = WidgetSettings(instance=user_settings)

    settings_dict = user_settings.get_content()

    context = {
        "namespace": service_info["namespace"],
        'settings_form': settings_form,
        'settings_dict': settings_dict
    }

    return render(request, "nchat/vendor/settings/settings_index.html", context)


@login_required(login_url='/nchat/')
def webhooks(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']
    user_settings = LineSettings.objects.filter(owner_id=request.user.id, app_id='nchat').first()
    bot_list = Bot.objects.filter(owner_id=request.user.id, app_id='nchat')
    bot_list_length = bot_list.count()

    if not user_settings:
        user_settings = LineSettings(owner_id=request.user.id, app_id='nchat')

    if request.POST:
        settings_form = LineWebhookSettings(request.POST, instance=user_settings)
        if settings_form.is_valid():
            settings_form.save()
        else:
            print("form is not valid: ", settings_form)
    else:
        settings_form = LineWebhookSettings(instance=user_settings)

    context = {
        "namespace": service_info["namespace"],
        "user_business": user_business,
        'settings_form': settings_form,
        "bot_list": bot_list,
        "bot_list_length": bot_list_length,
        "line_access_url_part": user_settings.line_access_url_part
    }

    return render(request, "nchat/vendor/settings/settings_webhooks.html", context)


# import views
# todo remove this
from apps.core.views.vendor_common.login_user_info import *


class FileCreateView(CreateView):
    model = File
    fields = ['upload', ]
    success_url = reverse_lazy('nchat:settings_files')
    template_name = "nchat/vendor/settings/settings_files.html"

    def post(self, request, *args, **kwargs):
        print('doing post', request.POST, request.FILES)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        service_info = AuthorizeUser(self.request.user, self.request.path).execute()
        print('getting form valid for file view')
        document = form.save(commit=False)
        document.app_id = service_info["app_id"]
        document.owner_id = service_info["owner_id"]
        document.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        service_info = AuthorizeUser(self.request.user, self.request.path).execute()

        context = super().get_context_data(**kwargs)
        context["files"] = File.objects.filter(app_id=service_info["app_id"], owner_id=service_info["owner_id"])
        context["namespace"] = service_info["namespace"]
        return context


@login_required(login_url='/nchat/')
def file_delete(request):
    service_info = AuthorizeUser(request.user, request.path).execute()

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
        redirect_url = "/" + service_info["namespace"] + "/settings/files/"

    return redirect(redirect_url)