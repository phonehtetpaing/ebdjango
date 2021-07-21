from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout
from django.db.models import Q
from dateutil.relativedelta import *
from datetime import datetime
import stripe
# imports for webhook
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

# import models
from apps.nchat.models.business import Business, BusinessPlan
from apps.nchat.models.payment import PaymentHistory

# import forms

# import use cases
from apps.nchat.usecases.user import AuthorizeUser


@login_required(login_url='/nchat/')
def edit(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    vendor_user = service_info['vendor_user']

    # todo add .parent for production code
    print('debug parent:', vendor_user.business.parent)
    if vendor_user.business.parent is not None:
        business_plans = BusinessPlan.objects.filter(business=vendor_user.business.parent, is_delete=False).all()
    else:
        return redirect('nchat:business_plan_detail')

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
    business_plan = BusinessPlan.objects.filter(business=vendor_user.business.parent,
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
        new_purchase = PaymentHistory(from_business=vendor_user.business,
                                      to_business=business_plan.business,
                                      plan_name=business_plan.name,
                                      amount=business_plan.price,
                                      expiration_dt=expiration_date,
                                      regist_dt=datetime.now(),
                                      status=0)
        new_purchase.save()
        stripe.Charge.create(
            amount=business_plan.price,
            currency='jpy',
            description=business_plan.name,
            source=request.POST['stripeToken'],
            metadata={
                'user_id': vendor_user.auth_user.id,
                'payment_history_id': new_purchase.id,
            }
        )

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

@csrf_exempt
def webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    event_history_id = event.data.object.metadata.payment_history_id
    event_history = PaymentHistory.objects.filter(id=event_history_id).first()
    print(event_history.plan_name)

    # Handle the event
    if event.type == 'charge.failed':
        # payment_intent = event.data.object  # contains a stripe.PaymentIntent
        event_history.status = 4
        event_history.save()
        print("Charge failed!")
    elif event.type == 'charge.pending':
        event_history.status = 1
        event_history.save()
        print("Charge pending!")
    elif event.type == 'charge.refunded':
        event_history.status = 3
        event_history.save()
        print("Charge refunded!")
    elif event.type == 'charge.succeeded':
        event_history.status = 2
        event_history.save()
        print("Charge refunded!")
    elif event.type == 'charge.dispute.created':
        event_history.status = 5
        event_history.save()
        print("Charge dispute created!")
    elif event.type == 'charge.refund.updated':
        event_history.status = 6
        event_history.save()
        print("Charge refund updated!")
    else:
        # Unexpected event type
        print("Unexpected event type: ", event.type)
        return HttpResponse(status=400)
    return HttpResponse(status=200)
