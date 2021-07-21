from django.db import transaction
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import HttpResponseNotFound
from random import randint
from django.utils.translation import ugettext_lazy as _

# import models
from apps.nchat.models.vendor_user import VendorUser
from apps.nchat.models.business import Business
from apps.messageflow.models.settings import Settings as LineSettings
from apps.messageflow.models.bot import Bot, BotScenario, Scenario

# import forms
from apps.nchat.forms.login import LoginForm
from apps.nchat.forms.login import RegistrationForm

# import views
from apps.nchat.views.common.service_platform_info import get_service_platform_info_by_id


def service_login(request, service_name=None):
    """ Login Index """
    registration_business = Business.objects.filter(service_name=service_name, is_delete=False).first()
    if not service_name or not registration_business:
        return HttpResponseNotFound()

    service_info = get_service_platform_info_by_id(service_name)

    form = LoginForm(request.POST or None, initial={'service': service_name })
    if request.POST and form.is_valid():
        print('was valid')
        user = form.login(request)
        vendor_user = VendorUser.objects.filter(auth_user_id=user.id, is_active=True, is_delete=False).first()
        line_settings = LineSettings.objects.filter(owner_id=user.id).first()
        if user and vendor_user and user.is_active and vendor_user.is_active:
            django_login(request, user)
            if line_settings.line_channel_access_token and line_settings.line_channel_secret:
                return redirect('/nchat/business/detail/')
            else:
                return redirect('/nchat/settings/webhooks/')

    context = {
        'form': form,
        'title': '{0} Login'.format(service_info['service_name']),
        'namespace': service_info['namespace'],
        'service_name': service_info['service_name'],
        'service_logo': service_info['service_logo'],
    }
    return render(request, "nchat/vendor/common/login.html", context)


def login(request):
    """ Login Index """
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        print('was valid')
        user = form.login(request)
        vendor_user = VendorUser.objects.filter(auth_user_id=user.id, is_active=True, is_delete=False).first()
        line_settings = LineSettings.objects.filter(owner_id=user.id).first()
        if user and vendor_user and user.is_active and vendor_user.is_active:
            django_login(request, user)
            if line_settings.line_channel_access_token and line_settings.line_channel_secret:
                return redirect('/nchat/business/detail/')
            else:
                return redirect('/nchat/settings/webhooks/')

    context = {
        'form': form,
        'title': 'Login',
    }
    return render(request, "nchat/vendor/common/login.html", context)


@login_required(login_url='/nchat/')
def logout(request):
    """ Logout active user """
    redirect_url = "/nchat/"
    django_logout(request)

    return redirect(redirect_url)


def register(request, service_name=None):
    """ Registration Index """
    registration_business = Business.objects.filter(service_name=service_name, is_delete=False).first()
    if not service_name or not registration_business:
        return HttpResponseNotFound()

    service_info = get_service_platform_info_by_id(service_name)
    # clean the data in the form and check all data is valid
    registration_form = RegistrationForm(request.POST or None)
    if request.POST and registration_form.is_valid():
        vendor_user = registration_form.save(service_name=service_name)
        vendor_user.save()

        line_access_url_part = randint(10000000000000000000, 99999999999999999999)
        user_settings = LineSettings(owner_id=vendor_user.auth_user_id, app_id='nchat', line_access_url_part=line_access_url_part)
        user_settings.save()

        bot = Bot(name=_('Bot1'), owner_id=vendor_user.auth_user_id, app_id='nchat', is_active=1)
        bot.save()
        scenario = Scenario(name=_('Scenario1'), owner_id=vendor_user.auth_user_id, app_id='nchat')
        scenario.save()
        bot_scenario = BotScenario(bot_id=bot.id, scenario_id=scenario.id, weight=100)
        bot_scenario.save()

        return redirect('/nchat/{0}'.format(service_name))

    context = {
        "registration_form": registration_form,
        'title': '{0} Login'.format(service_info['service_name']),
        'namespace': service_info['namespace'],
        'service_name': service_info['service_name'],
        'service_logo': service_info['service_logo'],
    }

    return render(request, "nchat/vendor/common/register.html", context)



