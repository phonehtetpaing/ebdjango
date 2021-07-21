from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# import models
from apps.core.models.end_user import EndUser
from apps.qa.models.end_user_questionnaire import EndUserQuestionnaire

# import forms
from apps.qa.forms.end_user import EndUserForm

# import views
from apps.qa.views.common.login_user_info import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='/qa/')
def list(request, end_user_id=None):
    """ User List """
    user_obj = get_login_user_objects(request)
    end_users = EndUser.objects.filter(vendor_branch=user_obj["vendor_branch"]).all()

    # pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(end_users, 20)
    try:
        end_users = paginator.page(page)
    except PageNotAnInteger:
        end_users = paginator.page(1)
    except EmptyPage:
        end_users = paginator.page(paginator.num_pages)

    # load correct user profile
    end_user = None
    if not end_user_id:
        end_user = EndUser.objects.filter(vendor_branch=user_obj["vendor_branch"]).first()
        if end_user:
            end_user_id = end_user.id
    if end_user_id:
        end_user = EndUser.objects.filter(id=end_user_id, vendor_branch=user_obj["vendor_branch"]).first()
        end_user_form = EndUserForm(instance=end_user)
        questionnaires = EndUserQuestionnaire.objects.filter(end_user=end_user).all()

        context = {
            "title": "User List",
            "end_users": end_users,
            "end_user": end_user,
            "form": end_user_form,
            "statistics": get_dummy_statistic(),
            "questionnaires": questionnaires,
            "namespace": "qa"
        }
    else:
        context = {
            "title": "User List",
            "end_users": end_users,
            "namespace": "qa"
        }

    return render(request, "vendor/users/user_list.html", context)


def get_dummy_statistic():
    return {
        "completed": 7,
        "received": 10,
        "claimed": 33,
        "complete_rate": 70,
        "claim_rate": 82,
    }
