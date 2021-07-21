from django.db import transaction
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout
from datetime import datetime

# import models
from apps.nchat.models.business import Business
from apps.nchat.models.payment import PaymentHistory

# import forms
from apps.nchat.forms.business import BusinessForm

# import use cases
from apps.nchat.usecases.user import AuthorizeUser


@login_required(login_url='/nchat/')
def detail(request, business_id=None):
    """ Business Edit """
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']
    print('we have business', user_business, service_info['vendor_user'])

    all_business_subsidiaries = user_business.get_descendants(include_self=False)
    if not business_id:
        business_id = user_business.id

    if user_business.id == business_id:
        business = user_business
    else:
        business = all_business_subsidiaries.filter(id=business_id, is_delete=False).first()

    direct_business_subsidiaries = Business.objects.filter(parent_id=business_id, is_delete=False).all()

    today = datetime.today()
    active_plan = PaymentHistory.objects.filter(from_business=user_business, expiration_dt__gte=today)\
        .order_by("expiration_dt").first()

    print("this is active plan: ", active_plan )

    if request.POST:
        form = BusinessForm(request.POST, request.FILES, instance=user_business)
        if form.is_valid():
            form.save()
            redirect_url = "/nchat/business/detail/" + str(user_business.id) + "/"
            return redirect(redirect_url)
    else:
        form = BusinessForm(instance=user_business)

    context = {
        'form': form,
        'title': 'Business Edit',
        'business': business,
        'business_subsidiaries': direct_business_subsidiaries,
        'active_plan': active_plan,
        'namespace': 'nchat',
    }

    return render(request, "nchat/vendor/business/business_detail.html", context)


@login_required(login_url='/nchat/')
def delete(request, business_id):
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']
    all_business_subsidiaries = user_business.get_descendants(include_self=False)

    if user_business.id == business_id:
        business = user_business
        #TODO delete self and logout?
    else:
        business = all_business_subsidiaries.filter(id=business_id, is_delete=False).first()
        business.is_delete = True
        business.save()

    redirect_url = "/nchat/business/detail/" + str(user_business.id) + "/"
    return redirect(redirect_url)

