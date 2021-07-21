import ast

from django import template
register = template.Library()


@register.filter("to_string")
def to_string(value):
    return str(value)


@register.filter("to_dictionary")
def to_dictionary(value):
    if value:
        return ast.literal_eval(value)
    return value