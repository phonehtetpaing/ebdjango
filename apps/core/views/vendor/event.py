from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.utils import timezone

# import models
from apps.core.models.event import Event
from apps.core.models.event_reservation import EventReservation

# import views
from apps.core.views.vendor_common.login_user_info import *

# import forms
from apps.core.forms.event import EventForm, EventDateTimeForm, EventGCalSettingForm, EventCategoryGCalForm


@login_required
def list(request, event_category_id=None):
    """ list """
    user_obj = get_login_user_objects(request)

    event_category = EventCategory.objects.filter(id=event_category_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).first()
    event_list = Event.objects.filter(event_category_id=event_category.id, is_delete=False)
    page = request.GET.get('page', 1)

    paginator = Paginator(event_list, settings.RESULTS_PER_PAGE)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    context = {
        "title": "Event List",
        "path": ["Events", "Event Category", "Event List"],
        "event_category_id": event_category_id,
        "events": events,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/event_list.html", context)


@login_required
def detail(request, event_category_id=None, event_id=None):
    """ detail """
    user_obj = get_login_user_objects(request)
    
    event_category = EventCategory.objects.filter(id=event_category_id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).first()
    event = Event.objects.filter(id=event_id).first()

    form = EventForm(request.POST or None, instance=event)
    time_form = EventDateTimeForm(request.POST or None, instance=event)
    gcal_form = EventGCalSettingForm(request.POST or None, instance=event)

    cat_gcal_form = EventCategoryGCalForm(instance=event_category)
    context = {
        "title": "Event List",
        "path": ["Events", "Event Category", "Event List", "Event Details"],
        "event_category": event_category,
        "event": event,
        "form": form,
        "time_form": time_form,
        "gcal_form": gcal_form,
        "cat_gcal_form": cat_gcal_form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/event_detail.html", context)


@login_required
def edit(request, event_id=None):
    """ edit """
    user_obj = get_login_user_objects(request)
    event = Event.objects.filter(id=event_id).first()
    event_category = EventCategory.objects.filter(id=event.event_category_id, vendor_branch_id=user_obj["vendor_branch"].id,
                                                  is_delete=0).first()
    if event.event_category.event_minutes_csv:
        minutes_list = event.event_category.event_minutes_csv.split(",")
    else:
        minutes_list = []

    form = EventForm(request.POST or None, instance=event)
    time_form = EventDateTimeForm(request.POST or None, instance=event)
    gcal_form = EventGCalSettingForm(request.POST or None, instance=event)

    if form.is_valid() and (time_form.is_valid() or gcal_form.is_valid()):
        event = form.save(commit=False)
        event.update_dt = timezone.now()
        event.save()

        if time_form.is_valid():
            event = time_form.save(commit=False)
            event.update_dt = timezone.now()
            event.save()
        elif gcal_form.is_valid():
            event = gcal_form.save(commit=False)
            event.update_dt = timezone.now()
            event.save()

        redirect_url = "/" + user_obj["service_url"] + "/event/list/" + str(event.event_category.id) + "/"
        return redirect(redirect_url)
    else:
        print(time_form.errors)

    context = {
        "title": "Event List",
        "path": ["Events", "Event Category", "Event List", "Event Details"],
        "event_category": event_category,
        "event": event,
        "form": form,
        "time_form": time_form,
        "gcal_form": gcal_form,
        "minutes_list": minutes_list,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/event_detail.html", context)
  
    
@login_required
def add(request, event_category_id=None):
    """ Add """
    user_obj = get_login_user_objects(request)

    # Because of current LINE limitation prevent more than 4 events
    events = Event.objects.filter(event_category_id=event_category_id, is_delete=False).count()
    if events < 4:
        event = Event()
        event.event_category_id = event_category_id
        event.save()
        redirect_url = "/" + user_obj["service_url"] + "/event/" + str(event_category_id) + "/detail/" + str(event.id) + "/"
    else:
        redirect_url = "/" + user_obj["service_url"] + "/event/list/" + str(event_category_id) + "/"
    return redirect(redirect_url)


@login_required
def delete(request):
    user_obj = get_login_user_objects(request)

    if request.method == "POST":
        delete_ids = request.POST.getlist('select_item')
        event = Event.objects.filter(id__in=delete_ids, is_delete=0)

        # exclude events that already have reservations
        reserved_events = EventReservation.objects.filter(event_id__in=delete_ids).values_list('event_id', flat=True)
        event.exclude(id__in=reserved_events)
        event.update(is_delete=1)

    previous_page = request.META.get('HTTP_REFERER')
    if previous_page:
        redirect_url = previous_page
    else:
        redirect_url = "/" + user_obj["service_url"] + "/event/catagory/list/"

    return redirect(redirect_url)
