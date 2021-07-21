from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout
from django.db.models import Q
from dateutil.relativedelta import *
from datetime import datetime
import stripe

# import models
from apps.nchat.models.business import Business, BusinessPlan
from apps.nchat.models.payment import PaymentHistory

# import views
from apps.nchat.views.common.login_user_info import get_login_user_objects

# import use cases
from apps.nchat.usecases.user import AuthorizeUser


@login_required(login_url='/nchat/')
def edit(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    vendor_user = service_info['vendor_user']

    # todo add .parent for production code
    business_plans = BusinessPlan.objects.filter(business=vendor_user.business, is_delete=False).all()

    context = {
        'title': 'Business Detail',
        'business_plans': business_plans,
        'vendor_user': vendor_user,
        'namespace': 'nchat',
    }

    return render(request, "nchat/vendor/settings/payment_option_edit.html", context)

@login_required(login_url='/nchat/')
def checkout(request, plan_id=None):
    service_info = AuthorizeUser(request.user, request.path).execute()
    vendor_user = service_info['vendor_user']

    # todo add .parent for production code
    business_plan = BusinessPlan.objects.filter(business=vendor_user.business,
                                                id=plan_id,
                                                is_delete=False).first()
    if not business_plan:
        return redirect('nchat:payment_edit')

    # calculate expiration/"renewal" date of plan being purchased
    duration_of_plan = business_plan.duration
    previous_purchase = PaymentHistory.objects.filter(from_business=vendor_user.business)\
        .order_by("-expiration_dt").first()
    if previous_purchase:
        have_previous_purchase = True
        start_date = previous_purchase.expiration_dt
    else:
        have_previous_purchase = False
        start_date = datetime.now()
    expiration_date = start_date + relativedelta(months=+(duration_of_plan))

    # add purchase to history
    if request.POST:
        # todo add .parent for production code
        stripe.Charge.create(
            amount=business_plan.price,
            currency='jpy',
            description=business_plan.name,
            source=request.POST['stripeToken']
        )
        new_purchase = PaymentHistory(from_business=vendor_user.business,
                                      to_business=vendor_user.business,
                                      plan_name=business_plan.name,
                                      amount=business_plan.price,
                                      expiration_dt=expiration_date,
                                      regist_dt=datetime.now(),
                                      status=0)
        new_purchase.save()
        return redirect('nchat:payment_history_list')

    stripe_key = settings.STRIPE_PUBLISHABLE_KEY

    context = {
        'title': 'Business Detail',
        'business_plan': business_plan,
        'vendor_user': vendor_user,
        'namespace': 'nchat',
        'stripe_key': stripe_key,
        'have_previous_purchase': have_previous_purchase,
        'previous_expiration_date': start_date,
        'expiration_date': expiration_date,
    }
    return render(request, "nchat/vendor/settings/payment_checkout.html", context)

