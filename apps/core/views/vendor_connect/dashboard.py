from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.event import Event
from apps.core.models.event_category import EventCategory
from apps.core.models.todo_action_status import TodoActionStatus
from apps.core.models.todo import Todo

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def index(request):
    """ Dashboard Index """
    user_obj = get_login_user_objects(request)

    # get User numbers
    users = EndUser.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False)
    usercount = users.count()

    # get Event numbers
    event_categories = EventCategory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False)
    events = Event.objects.filter(event_category_id__in=event_categories, is_delete=False)
    eventcount = events.count()

    # get Todos numbers
    todo_action_status = TodoActionStatus.objects.filter(is_delete=False).exclude(name='DONE')
    todo_action_status_list = []
    for status in todo_action_status:
        todo_action_status_list.append(status.id)

    todos = Todo.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, todo_action_status_id__in=todo_action_status_list, is_delete=False)
    todocount = todos.count()

    context = {
        "title" : "Dashboard",
        "usercount" : usercount,
        "todocount" : todocount,
        "eventcount": eventcount,
        "todos": todos,
        "events": events,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor_connect/dashboard.html", context)



