from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from apps.core.models.document import Document


def document_view(request, access_url=None):
    redirect_url = "{0}{1}.css".format(settings.CSS_URL, access_url)

    response = HttpResponseRedirect(redirect_url)

    return response
