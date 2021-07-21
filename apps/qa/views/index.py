from django.db import transaction
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

# import models
from django.contrib.auth.models import User
from apps.core.models.vendor_user import VendorUser as CoreVendorUser
from apps.qa.models.vendor_user import VendorUser
from apps.qa.models.notification_service import NotificationService
from apps.qa.models.notification_setting import NotificationSetting

# import forms
from apps.qa.forms.login import LoginForm
from apps.qa.forms.login import RegistrationForm

from apps.qa.forms.ma_message import MaDirectMessageForm

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects
from apps.qa.views.common.tokens import account_activation_token


def index(request):
    """ Login Index """
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        vendor_user = VendorUser.objects.filter(auth_user_id=user.id, is_active=True, is_delete=False).first()
        if user and vendor_user and user.is_active and vendor_user.is_active:
            login(request, user)
            return redirect('/qa/dashboard/')

    context = {
        'form': form,
        'title': 'Login',
        'namespace': 'qa',
    }
    return render(request, "vendor/common/login.html", context)


def register(request):
    """ Registration Index """

    # clean the data in the form and check all data is valid
    registration_form = RegistrationForm(request.POST or None)
    if request.POST and registration_form.is_valid():
        # ensure nothing is saved when any of the operations fail
        with transaction.atomic():
            # create vendor
            vendor_data = registration_form.register_vendor()
            vendor = vendor_data['vendor']
            vendor.save()

            # create vendor branch
            vendor_branch = vendor_data['vendor_branch']
            vendor_branch.vendor = vendor
            vendor_branch.save()

            # register vendor service type and payment plan
            vendor_service = registration_form.register_vendor_service(vendor=vendor).save()
            vendor_plan = registration_form.register_vendor_plan(vendor=vendor).save()

            # register auth user
            user = registration_form.register_user()
            if user:
                user.save()

            # register vendor user
            vendor_user = registration_form.register_vendor_user(vendor_branch=vendor_data['vendor_branch'], user=user)
            vendor_user.save()
            initialize_settings(vendor_user)

            # if this is a new registration send email to user
            if vendor_data['is_new']:
                send_confirmation_email(request, user, [user.email])
            # if this registration is for an existing vendor send email to vendor admin to confirm usage
            else:
                vendor_admin = CoreVendorUser.objects.filter(vendor_branch=vendor_branch, is_delete=False).first()
                # todo what to do if we have no existing vendor admin?
                send_confirmation_email(request, user, [vendor_admin.email])

            return redirect('/qa/account_activation_sent')

    context = {
        "title": "Register",
        "registration_form": registration_form,
        "namespace": 'qa',
    }

    return render(request, "vendor/common/register.html", context)


@login_required(login_url='/qa/')
def logout(request):
    """ Logout active user """
    redirect_url = "/qa/"
    django_logout(request)

    return redirect(redirect_url)


def initialize_settings(vendor_user):
    print('debugging initialize settings', vendor_user)
    """ Initialize settings for new users """
    services = NotificationService.objects.all()
    for service in services:
        has_setting = NotificationSetting.objects.filter(notification_service=service, vendor_user=vendor_user).first()
        if not has_setting:
            setting = NotificationSetting()
            setting.vendor_user = vendor_user
            setting.notification_service = service
            setting.save()

    return


def send_confirmation_email(request, user, to_email):
    current_site = get_current_site(request)
    subject = 'Activate Your ChatQuest Account'
    message = render_to_string('vendor/common/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'namespace': 'qa',
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token': account_activation_token.make_token(user),
    })
    from_email = 'no_reply@chatquest.app'
    print('debugging activation email', message)
    send_mail(subject, message, from_email, to_email)
