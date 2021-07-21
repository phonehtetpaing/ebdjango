from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_contactchat import EndUserContactChat

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects


@login_required(login_url='/qa/')
def index(request):
    """ Dashboard Index """
    user_obj = get_login_user_objects(request)

    # build up this list with users that signed up in the last week
    past_7_days = date.today() - timedelta(days=7)
    users = EndUser.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=False).all()
    end_users = EndUserContactChat.objects.filter(end_user__in=users, regist_dt__gte=past_7_days).order_by('-regist_dt')[:10]

    context = {
        "title": "Dashboard",
        "namespace": user_obj["service_namespace"],
        "end_users": end_users
    }

    return render(request, "vendor/common/dashboard.html", context)
