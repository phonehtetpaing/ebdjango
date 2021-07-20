from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from apps.core.models.document import Document

# import views
from apps.core.views.vendor_common.login_user_info import *


class DocumentCreateView(CreateView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('contactchat:documents')
    template_name = "vendor_contactchat/document_form.html"

    def form_valid(self, form):
        user_obj = get_login_user_objects(self.request)

        document = form.save(commit=False)
        document.vendor_branch_id = user_obj["vendor_branch"].id
        document.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        user_obj = get_login_user_objects(self.request)

        context = super().get_context_data(**kwargs)
        documents = Document.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id)
        context['documents'] = documents
        context['namespace'] = user_obj["service_namespace"]
        return context
