from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

# import models
from apps.core.models.vendor_user import VendorUser

# import views
from apps.core.views.vendor_common.login_user_info import *

# import forms
from apps.core.forms.vendor_user import VendorUserForm


@login_required
def detail(request, vendor_user_id=None):
    """ Vendor User Detail """
    user_obj = get_login_user_objects(request)
    vendor_user = VendorUser.objects.filter(id=vendor_user_id, vendor_branch_id=user_obj["vendor_branch"].id).first()

    if request.method == "POST":
        form = VendorUserForm(request.POST, instance=vendor_user)
        if form.is_valid():
            vendor_user = form.save(commit=False)
            vendor_user.update_dt = timezone.now()
            vendor_user.save()

            redirect_url = "/" + user_obj["service_url"] + "/settings/vendor/"
            return redirect(redirect_url)
    else:
        form = VendorUserForm(instance=vendor_user)

    context = {
        "vendor_user": vendor_user,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }
    return render(request, "vendor/settings_vendor_account_detail.html", context)


@login_required
def edit(request, vendor_user_id=None):
    user_obj = get_login_user_objects(request)
    vendor_user = VendorUser.objects.filter(id=vendor_user_id, vendor_branch_id=user_obj["vendor_branch"].id).first()

    if request.method == "POST":
        form = VendorUserForm(request.POST, instance=vendor_user)
        if form.is_valid():
            vendor_user = form.save(commit=False)
            vendor_user.update_dt = timezone.now()
            vendor_user.save()

            redirect_url = "/" + user_obj["service_url"] + "/settings/vendor/"
            return redirect(redirect_url)
    else:
        form = VendorUserForm(instance=vendor_user)
    
    context = {
        "vendor_user": vendor_user,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }
    return render(request, "vendor/settings_vendor_account_detail.html", context)


@login_required
def add(request):
    """ New Vendor User Page """
    user_obj = get_login_user_objects(request)
    
    context = {
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings_vendor_new_account_index.html", context)


@login_required
def login_detail(request, vendor_user_id=None):
    """ Login Edit Page """
    user_obj = get_login_user_objects(request)
    vendor_user = VendorUser.objects.filter(id=vendor_user_id, vendor_branch_id=user_obj["vendor_branch"].id).first()

    context = {
        "vendor_user": vendor_user,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings_vendor_account_login_detail.html", context)


@login_required
def login_edit(request, vendor_user_id=None):
    """ Login Update """
    user_obj = get_login_user_objects(request)
    vendor_user = VendorUser.objects.filter(id=vendor_user_id, vendor_branch_id=user_obj["vendor_branch"].id).first()

    password = request.POST['password']
    password_confirm = request.POST['password_confirm']

    if password != "" and password == password_confirm:
        # Reset Password
        try:
            # Update a Vendor User
            auth_user = vendor_user.auth_user
            auth_user.set_password(password)
            auth_user.save()

            redirect_url = "/" + user_obj["service_url"] + "/settings/vendor/"
            return redirect(redirect_url)

        except Exception as e:
            print('%r' % e)
            # TODO: add error obj
            redirect_url = "/" + user_obj["service_url"] + "/settings/account/login/detail/" + vendor_user.id + "/"
            return redirect(redirect_url)


@login_required
def create_user(request):
    """ Create Vendor Users """
    user_obj = get_login_user_objects(request)
    # POST DATA
    last_name = request.POST['last_name']
    first_name = request.POST['first_name']
    email = request.POST['email']
    password = request.POST['password']
    password_confirm = request.POST['password_confirm']

    if last_name != "" and first_name != "" and email != "" and password != "" and password == password_confirm:

        try:
            # Create a Django Login User
            auth_user = User.objects.create_user(username=email, email=email, password=password)
            auth_user.is_active = True
            auth_user.save()
        except Exception as e:
            print('%r' % e)
            # TODO: add error obj
            redirect_url = "/" + user_obj["service_url"] + "/settings/account/add/"
            return redirect(redirect_url)

        try:
            # Create a Vendor User
            vendor_user = VendorUser()
            vendor_user.vendor_branch = user_obj["vendor_branch"]
            vendor_user.auth_user = auth_user
            vendor_user.last_name = last_name
            vendor_user.first_name = first_name
            vendor_user.email = email
            vendor_user.save()

            redirect_url = "/" + user_obj["service_url"] + "/settings/vendor/"
            return redirect(redirect_url)
            
        except Exception as e:
            print('%r' % e)
            auth_user.delete()
            # TODO: add error obj
            redirect_url = "/" + user_obj["service_url"] + "/settings/account/add/"
            return redirect(redirect_url)

    else:
        # TODO: add error obj
        redirect_url = "/" + user_obj["service_url"] + "/settings/account/add/"
        return redirect(redirect_url)
