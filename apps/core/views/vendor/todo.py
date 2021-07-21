import ast
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

# import models
from apps.core.models.todo_action_status import TodoActionStatus
from apps.core.models.todo import Todo

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def list(request):
    """ todo list """
    user_obj = get_login_user_objects(request)

    todo_list = Todo.visible.filter(vendor_branch=user_obj["vendor_branch"]).all()
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
        "todos": todos,
        "todocount": todocount,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/todo_list.html", context)


@login_required
def detail(request, todo_id=None):
    """ todo detail """
    user_obj = get_login_user_objects(request)

    todo = Todo.objects.filter(id=todo_id, vendor_branch=user_obj["vendor_branch"]).first()
    todo_action_status = TodoActionStatus.objects.filter(is_delete=False).order_by("display_order_num").exclude(name='Hidden').all()
    if todo.end_user_reply:
        user_replies = ast.literal_eval(todo.end_user_reply)
    else:
        user_replies = []

    context = {
        "todo": todo,
        "user_replies": user_replies,
        "todo_action_status": todo_action_status,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/todo_detail.html", context)


@login_required
def edit(request, todo_id=None):
    """ todo detail """
    user_obj = get_login_user_objects(request)

    memo = request.POST["memo"]
    todo_action_status = request.POST["todo_action_status"]

    todo = Todo.objects.filter(id=todo_id).first()
    todo.memo = memo
    todo.todo_action_status_id = int(todo_action_status)
    todo.save()

    redirect_url = "/" + user_obj["service_url"] + "/dashboard/"
    return redirect(redirect_url)
