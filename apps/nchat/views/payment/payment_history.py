from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout
from django.db.models import Q

# import models
from apps.nchat.models.business import Business, BusinessPlan
from apps.nchat.models.payment import PaymentHistory

# import forms
from apps.nchat.forms.filter import PaymentHistoryFilter

# import use cases
from apps.nchat.usecases.user import AuthorizeUser


@login_required(login_url='/nchat/')
def list(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    user_business = service_info['business']
    vendor_email = service_info['vendor_user']

    business_plans = BusinessPlan.objects.filter(business=user_business, is_delete=False).all()

    payment_history = PaymentHistory.objects.filter(Q(from_business=user_business.id) |
                                                    Q(to_business=user_business.id)).all().order_by("-regist_dt")

    history_filter = PaymentHistoryFilter(request.GET, queryset=payment_history, request=request)
    filtered_qs = history_filter.qs
    paginator = Paginator(filtered_qs, 20)
    page = request.GET.get('page', 1)

    try:
        filtered_payment_history = paginator.page(page)
    except PageNotAnInteger:
        filtered_payment_history = paginator.page(1)
    except EmptyPage:
        filtered_payment_history = paginator.page(paginator.num_pages)

    context = {
        'title': 'Business Detail',
        'business': user_business,
        'business_plans': business_plans,
        'filter_form': history_filter.form,
        'filtered_payment_history': filtered_payment_history,
        'payment_history': payment_history,
        'user_business': user_business,
        'vendor_email': vendor_email,
        'namespace': 'nchat',
    }
    return render(request, "nchat/vendor/settings/payment_history_list.html", context)
