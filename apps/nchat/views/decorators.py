from functools import wraps
from datetime import datetime
from django.shortcuts import redirect
from apps.nchat.models.payment import PaymentHistory
from apps.nchat.usecases.user import AuthorizeUser


def paid_up_account_required(function=None, payment_url=None):
    actual_decorator = user_has_paid(test_func=payment_checker, payment_url=payment_url)
    if function:
        return actual_decorator(function)
    return actual_decorator


def user_has_paid(test_func, payment_url=None):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request):
                return view_func(request, *args, **kwargs)
            return redirect(payment_url)
        return _wrapped_view
    return decorator


def payment_checker(request):
    today = datetime.today()
    service_info = AuthorizeUser(request.user, request.path).execute()
    vendor_user = service_info['vendor_user']
    purchase_history = PaymentHistory.objects.filter(from_business=vendor_user.business, expiration_dt__gte=today,
                                                     status__lte=2).order_by("-expiration_dt")
    if purchase_history:
        return True
    return False
