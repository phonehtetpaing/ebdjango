from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from apps.qa.models.vendor_user import VendorUser

from apps.qa.views.common.tokens import account_activation_token


def account_activation_sent(request):
    """ renders a notification page after user registration """
    return render(request, 'vendor/common/account_activation_sent.html')


def activate(request, uidb64, token):
    """
        try to activate a user with the provided token information. If the information is invalid, the token has expired
        or the user has already been activated, redirect to an error page instead.
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        vendor_user = VendorUser.objects.get(auth_user=user)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and vendor_user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        vendor_user.is_active = True

        user.save()
        vendor_user.save()
        login(request, user)
        return redirect('/qa/')
    else:
        return render(request, 'vendor/common/account_activation_invalid.html')