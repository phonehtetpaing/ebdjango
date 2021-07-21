from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# import models


# import views

@login_required
def index(request):
    """ Direct Message Index """

    context = {
    }

    return render(request, "vendor/directmesasge.html", context)
