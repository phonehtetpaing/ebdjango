from django import template
register = template.Library()


@register.filter("to_string")
def to_string(value):
    return str(value)
