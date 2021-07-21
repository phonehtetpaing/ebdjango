from django import template
register = template.Library()

from apps.core.models.event_reservation import EventReservation


@register.filter("is_event_reservation_exist")
def is_event_reservation_exist(value):

    # value : event_id
    event_reservations = EventReservation.objects.filter(event_id=value).all()

    if event_reservations:
        return True

    return False
