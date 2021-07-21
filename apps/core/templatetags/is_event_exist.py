from django import template
register = template.Library()

from apps.core.models.event import Event


@register.filter("is_event_exist")
def is_event_exist(value):

    # value : event_category_id
    events = Event.objects.filter(event_category_id=value, is_delete=False).all()

    if events:
        return True

    return False
