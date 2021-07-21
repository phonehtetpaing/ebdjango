from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# import models
from apps.qa.models.notification import Notification
from apps.qa.models.notification_history import NotificationHistory

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects


def template_detail(request, template_id=None):
    if template_id is None:
        context = request_post(request, "template", None)

    else:
        context = request_get(request, "template", None, template_id)


@login_required(login_url='/qa/')
def detail(request, notification_id=None):
    user_obj = get_login_user_objects(request)

    try:
        notification = Notification.objects.get(id=notification_id)
        NotificationHistory.objects.filter(notification_id=notification_id, vendor_user_id=user_obj["vendor_user"]).update(seen=1)
    except Exception as e:
        print('invalid notification id: ', e)
        return redirect('/qa/list_notifications/')

    context = {
        "title": notification.title,
        "body": notification.body,
        "schedule_dt": notification.schedule_dt,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/notifications/notification_detail.html", context)


@login_required(login_url='/qa/')
def list(request):
    user_obj = get_login_user_objects(request)

    notification_history_list = NotificationHistory.objects.filter(vendor_user_id=user_obj["vendor_user"]).order_by("-notification__schedule_dt").all()

    context = {"notifications": notification_history_list,
               "namespace": user_obj["service_namespace"]
               }

    return render(request, "vendor/notifications/notification_list.html", context)

@login_required(login_url='/qa/')
@csrf_exempt
def set_all(request):
    user_obj = get_login_user_objects(request)

    NotificationHistory.objects.filter(vendor_user_id=user_obj["vendor_user"]).update(
        seen=1)

    return HttpResponse(status=204)
