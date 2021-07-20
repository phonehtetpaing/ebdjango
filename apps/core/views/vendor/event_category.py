from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.utils import timezone

# import models
from apps.core.models.event_category import EventCategory
from apps.core.models.event import Event

# import forms
from apps.core.forms.event import EventCategoryForm, EventCategoryGCalForm

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def list(request):
    """ list """
    user_obj = get_login_user_objects(request)
    event_category_list = EventCategory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).order_by("display_order_num")
    page = request.GET.get('page', 1)

    paginator = Paginator(event_category_list, settings.RESULTS_PER_PAGE)
    try:
        event_categories = paginator.page(page)
    except PageNotAnInteger:
        event_categories = paginator.page(1)
    except EmptyPage:
        event_categories = paginator.page(paginator.num_pages)

    # TODO: Number of Event in each Event Category

    context = {
        "title": "Event Category List",
        "path": ["Events", "Event Category List"],
        "event_categories": event_categories,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/event_category_list.html", context)


@login_required
def detail(request, event_category_id=None):
    """ detail """
    user_obj = get_login_user_objects(request)

    event_category = EventCategory.objects.filter(id=event_category_id, vendor_branch_id=user_obj["vendor_branch"].id).first()
    form = EventCategoryForm(request.POST or None, instance=event_category)
    gcal_form = EventCategoryGCalForm(request.POST or None, instance=event_category)

    context = {
        "title": "Event Category Details",
        "path": ["Events", "Event Category List", "Event Category Details"],
        "event_category": event_category,
        "form": form,
        "gcal_form": gcal_form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/event_category_detail.html", context)


@login_required
def edit(request, event_category_id=None):
    """ Update EventCategory """
    user_obj = get_login_user_objects(request)

    event_category = EventCategory.objects.filter(id=event_category_id, vendor_branch_id=user_obj["vendor_branch"].id).first()
    form = EventCategoryForm(request.POST or None, instance=event_category)
    gcal_form = EventCategoryGCalForm(request.POST or None, instance=event_category)
    if form.is_valid() and (not event_category.vendor_branch.is_google_calendar_ready or gcal_form.is_valid()):
        event = form.save(commit=False)
        event.update_dt = timezone.now()
        event.save()
        redirect_url = "/" + user_obj["service_url"] + "/event/category/list/"
        return redirect(redirect_url)

    context = {
        "title": "Event Category Details",
        "path": ["Events", "Event Category List", "Event Category Details"],
        "event_category": event_category,
        "form": form,
        "gcal_form": gcal_form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/event_category_detail.html", context)


@login_required
def add(request):
    """ Add EventCategory """
    user_obj = get_login_user_objects(request)

    # Because of current LINE limitation prevent more than 4 categories
    event_categories = EventCategory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0).count()
    if event_categories < 4:
        event_category = EventCategory()
        event_category.vendor_branch = user_obj["vendor_branch"]
        event_category.save()
        redirect_url = "/" + user_obj["service_url"] + "/event/category/detail/" + event_category.id.__str__() + "/"
    else:
        redirect_url = "/" + user_obj["service_url"] + "/event/category/list/"
    return redirect(redirect_url)


@login_required
def delete(request):
    """ Delete """
    user_obj = get_login_user_objects(request)

    if request.method == "POST":
        delete_ids = request.POST.getlist('select_item')
        event_category = EventCategory.objects.filter(id__in=delete_ids, vendor_branch_id=user_obj["vendor_branch"].id)

        # exclude categories that already have events
        existing_events = Event.objects.filter(event_category_id__in=delete_ids).values_list('event_category_id', flat=True)
        event_category.exclude(id__in=existing_events)
        event_category.update(is_delete=1)

    redirect_url = "/" + user_obj["service_url"] + "/event/category/list/"
    return redirect(redirect_url)
