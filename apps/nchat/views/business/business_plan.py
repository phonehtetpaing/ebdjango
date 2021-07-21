from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout
from django.db.models import Q

# import models
from apps.nchat.models.business import Business, BusinessPlan
from apps.nchat.models.payment import PaymentHistory

# import forms
from apps.nchat.forms.business import BusinessPlanForm

# import use cases
from apps.nchat.usecases.user import AuthorizeUser


@login_required(login_url='/nchat/')
def detail(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']
    vendor_email = service_info['vendor_user']

    business_plans = BusinessPlan.objects.filter(business=user_business, is_delete=False).all()

    payment_history = PaymentHistory.objects.filter(Q(from_business=user_business.id) |
                                                    Q(to_business=user_business.id)).all().order_by("-regist_dt")
    context = {
        'title': 'Business Detail',
        'business': user_business,
        'business_plans': business_plans,
        'payment_history': payment_history,
        'user_business': user_business,
        'vendor_email': vendor_email,
        'namespace': 'nchat',
    }
    return render(request, "nchat/vendor/settings/business_plan_detail.html", context)


@login_required(login_url='/nchat/')
def list(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']

    business_plans = BusinessPlan.objects.filter(business=user_business, is_delete=False).all()

    context = {
        'title': 'Whitelabel',
        'business': user_business,
        'business_plans': business_plans,
        'namespace': 'nchat',
    }
    return render(request, "nchat/vendor/settings/whitelabel_list.html", context)


@login_required(login_url='/nchat/')
def add(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']

    # create new business plan
    new_business_plan = BusinessPlan(business=user_business, name="New Plan")
    new_business_plan.save()

    redirect_url = "/nchat/plan/edit/" + str(new_business_plan.id) + "/"
    return redirect(redirect_url)


@login_required(login_url='/nchat/')
def edit(request, plan_id=None):
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']

    business_plan = BusinessPlan.objects.filter(business=user_business, id=plan_id).first()
    business_plan_form = BusinessPlanForm(instance=business_plan)

    if request.POST:
        business_plan_form = BusinessPlanForm(request.POST, instance=business_plan)
        if business_plan_form.is_valid():
            business_plan_form.save()
            redirect_url = "/nchat/plan/list/"
            return redirect(redirect_url)
        else:
            redirect_url = "/nchat/plan/list/"
            return redirect(redirect_url)

    context = {
        'title': 'Whitelabel',
        'business': user_business,
        'business_plan': business_plan,
        'namespace': 'nchat',
        'business_plan_form': business_plan_form,
    }
    return render(request, "nchat/vendor/settings/whitelabel_edit.html", context)



@login_required(login_url='/nchat/')
def delete(request, plan_id=None):
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']

    # delete business plan
    if plan_id:
        deleted_business_plan = BusinessPlan.objects.filter(business=user_business, id=plan_id).first()
        deleted_business_plan.is_delete = True
        deleted_business_plan.save()

    redirect_url = "/nchat/plan/list/"
    return redirect(redirect_url)