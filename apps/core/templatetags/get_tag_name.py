from django import template
register = template.Library()

from apps.core.models.tag import Tag


@register.filter("get_tag_name")
def get_tag_name(value):
    tag_name = Tag.objects.filter(cd=value).first().name
    if tag_name:
        return tag_name
    else:
        return 'TAG_NOT_FOUND'
