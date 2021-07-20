from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
# import models
from apps.core.models.event_reservation import EventReservation
from apps.core.models.event_reservation_status import EventReservationStatus
from apps.core.models.event import Event
from apps.core.models.end_user import EndUser

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def list(request, event_id=None):
    """ list """
    user_obj = get_login_user_objects(request)

    event = Event.objects.filter(id=event_id).first()
    event_category = EventCategory.objects.filter(id=event.id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)
    event_reservation_list = EventReservation.objects.filter(event_id=event.id, vendor_branch_id=user_obj["vendor_branch"].id, is_delete=0)
    page = request.GET.get('page', 1)

    paginator = Paginator(event_reservation_list, settings.RESULTS_PER_PAGE)
    try:
        event_reservations = paginator.page(page)
    except PageNotAnInteger:
        event_reservations = paginator.page(1)
    except EmptyPage:
        event_reservations = paginator.page(paginator.num_pages)

    context = {
        "title": "Event Reservations",
        "path": ["Events", "Event Category", "Event", "Event Reservations"],
        "event_reservations": event_reservations,
        "event": event,
        "event_category": event_category,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/event_reservation_list.html", context)


@login_required
def detail(request, vendor_user_id=None):
    """ detail """

    context = {
    }

    return render(request, "vendor/event_reservation_detail.html", context)


@login_required
def status_list(request):
    """ status list """

    context = {
    }

    return render(request, "vendor/reservation_status_list.html", context)
