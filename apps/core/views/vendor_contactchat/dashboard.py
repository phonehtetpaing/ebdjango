from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

# import models
from apps.core.models.todo import Todo

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def index(request):
    """ ContactChat Dashboard Index """
    user_obj = get_login_user_objects(request)

    todo_list = Todo.visible_pending.filter(vendor_branch=user_obj["vendor_branch"]).all()
    todocount = todo_list.count()

    page = request.GET.get('page', 1)

    paginator = Paginator(todo_list, settings.RESULTS_PER_PAGE)
    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        todos = paginator.page(1)
    except EmptyPage:
        todos = paginator.page(paginator.num_pages)

    context = {
        "title": "Dashboard",
        "todos": todos,
        "todocount": todocount,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/todo_list.html", context)
