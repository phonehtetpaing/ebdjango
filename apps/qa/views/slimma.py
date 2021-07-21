from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

# import models
from apps.qa.models.ma_trigger_type import MaTriggerType
from apps.qa.models.ma_trigger import MaTrigger
from apps.qa.models.message import Message

# import views
from apps.qa.views.common.login_user_info import get_login_user_objects
from django.core.mail import send_mail
from apps.core.models.end_user import EndUser

# import forms
from apps.qa.forms.ma_message import MaTriggerForm
from apps.qa.forms.ma_message import MaMessageForm
from apps.qa.forms.ma_message import MaDirectMessageForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='/qa/')
def index(request):
    """ Slim ma """
    user_obj = get_login_user_objects(request)

    messages = Message.objects.filter(vendor_branch=user_obj["vendor_branch"]).values_list('id', flat=True)
    triggers = MaTrigger.objects.filter(message_id__in=messages).all()
    trigger_types = MaTriggerType.objects.filter().all()

    page = request.GET.get('page', 1)
    paginator = Paginator(triggers, 5)
    try:
        triggers = paginator.page(page)
    except PageNotAnInteger:
        triggers = paginator.page(1)
    except EmptyPage:
        triggers = paginator.page(paginator.num_pages)

    context = {
        "title": "Slim MA",
        "namespace": user_obj["service_namespace"],
        "trigger_types": trigger_types,
        "triggers": triggers,
    }

    return render(request, "vendor/ma/ma_index.html", context)


@login_required(login_url='/qa/')
def edit(request, trigger_id=None):
    """ Slim ma edit """
    user_obj = get_login_user_objects(request)

    messages = Message.objects.filter(vendor_branch=user_obj["vendor_branch"]).values_list('id', flat=True)
    triggers = MaTrigger.objects.filter(message_id__in=messages).all()

    page = request.GET.get('page', 1)
    paginator = Paginator(triggers, 5)
    try:
        triggers = paginator.page(page)
    except PageNotAnInteger:
        triggers = paginator.page(1)
    except EmptyPage:
        triggers = paginator.page(paginator.num_pages)

    trigger_types = MaTriggerType.objects.filter().all()
    # todo we are pronbably better off asigning the vendor branch to the trigger instead of the message
    selected_trigger = MaTrigger.objects.filter(id=trigger_id).first()
    # todo fix this if else after debugging
    if selected_trigger:
        selected_message = selected_trigger.message
    else:
        selected_message = None

    if request.POST:
        trigger_form = MaTriggerForm(request.POST, instance=selected_trigger)
        message_form = MaMessageForm(request.POST, instance=selected_message)
        if trigger_form.is_valid() and message_form.is_valid():
            selected_trigger = trigger_form.save()
            selected_message = message_form.save()
    else:
        trigger_form = MaTriggerForm(instance=selected_trigger)
        message_form = MaMessageForm(instance=selected_message)

    context = {
        "title": "Slim MA",
        "namespace": user_obj["service_namespace"],
        "trigger_types": trigger_types,
        "trigger_form": trigger_form,
        "message_form": message_form,
        "triggers": triggers,
        "selected_trigger": selected_trigger,
    }

    return render(request, "vendor/ma/ma_index.html", context)


@login_required(login_url='/qa/')
def add(request):
    """ Slim ma add trigger message """
    user_obj = get_login_user_objects(request)

    # create new message and trigger instances
    new_message = Message(vendor_branch=user_obj["vendor_branch"])
    new_message.save()
    new_trigger = MaTrigger(message=new_message, trigger_type_id=1)
    new_trigger.save()

    redirect_url = "/" + user_obj["service_url"] + "/slimma/edit/" + str(new_trigger.id) + "/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def delete(request, trigger_id):
    """ Delete existing slimma trigger message """
    user_obj = get_login_user_objects(request)

    selected_trigger = MaTrigger.objects.filter(id=trigger_id).first()
    selected_message = selected_trigger.message

    number_of_triggers = MaTrigger.objects.filter(message=selected_message).count()
    # if this is the last trigger reference to the message delete it too
    if number_of_triggers == 1:
        selected_message.delete()

    selected_trigger.delete()

    redirect_url = "/" + user_obj["service_url"] + "/slimma/"
    return redirect(redirect_url)


@login_required(login_url='/qa/')
def direct(request, message_id=None):
    """
        Slim ma direct message
        Sends message directly to a selected group of users
     """
    user_obj = get_login_user_objects(request)

    messages = Message.objects.filter(vendor_branch=user_obj["vendor_branch"]).values_list('id', flat=True)
    triggers = MaTrigger.objects.filter(message_id__in=messages).all()

    # load email contacts for auto complete
    email_contacts = list(EndUser.objects.filter(vendor_branch=user_obj["vendor_branch"]).exclude(email__isnull=True).exclude(email__exact='').values_list('email', flat=True).all())

    if settings.DEBUG:
        fake_addresses = ["ebassi@outlook.com", "rddesign@outlook.com", "jbarta@msn.com", "isotopian@mac.com",
            "niknejad@sbcglobal.net", "pajas@msn.com", "mkearl@optonline.net", "frederic@gmail.com",
            "ryanvm@hotmail.com", "matloff@me.com", "imightb@hotmail.com", "skythe@icloud.com", "curly@verizon.net",
            "starstuff@hotmail.com", "cremonini@me.com", "sumdumass@att.net", "moxfulder@outlook.com", "msherr@comcast.net",
            "research@comcast.net", "heckerman@mac.com", "gslondon@aol.com", "fmerges@gmail.com", "notaprguy@comcast.net",
            "janusfury@mac.com", "syrinx@verizon.net", "mhanoh@live.com", "jsmith@verizon.net", "morain@comcast.net",
            "nwiger@att.net", "cmdrgravy@outlook.com", "cisugrad@hotmail.com", "facet@aol.com", "afeldspar@outlook.com",
            "jfreedma@yahoo.ca", "ijackson@yahoo.com", "grossman@live.com"]
        email_contacts.extend(fake_addresses)

    selected_message = None

    if request.POST:
        message_form = MaDirectMessageForm(request.POST, instance=selected_message, request=request)
        if message_form.is_valid():
            message_form.save(commit=False)
            subject = message_form.cleaned_data['subject']
            message = message_form.cleaned_data['message_text']
            from_email = 'no_reply@chatquest.app'
            recipient_list = message_form.cleaned_data['recipients'] or ['']
            try:
                send_mail(subject, message, html_message=message, from_email=from_email, recipient_list=recipient_list)
            except KeyError:
                print("error....")

            redirect_url = "/" + user_obj["service_url"] + "/slimma/"
            return redirect(redirect_url)
    else:
        message_form = MaDirectMessageForm(instance=selected_message, request=request)

    context = {
        "title": "Slim MA",
        "namespace": user_obj["service_namespace"],
        "message_form": message_form,
        "triggers": triggers,
        "email_contacts": email_contacts,
    }

    return render(request, "vendor/ma/ma_direct.html", context)


def vendor_directory_path(vendor_branch):
    #todo right now froala file upload doesn't use s3 boto backend right now.
    # file will be uploaded to MEDIA_ROOT/vendor_branch_<id>/<filename>
    return 'vendor_branch_{0}/froala/'.format(vendor_branch.id)
