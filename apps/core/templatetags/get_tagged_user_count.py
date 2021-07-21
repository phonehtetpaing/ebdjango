from django import template
register = template.Library()

from apps.core.models.tag import Tag
from apps.core.models.end_user import EndUser


@register.filter("get_tagged_user_cont")
def get_tagged_user_cont(value):
    if value:
        tag_id_list = value.split(",")
        tags = Tag.objects.filter(id__in=tag_id_list).all()
        tag_code_list = []
        for tag in tags:
            tag_code_list.append(tag.cd)

        tagged_user_count = EndUser.objects.filter(tag__name__in=tag_code_list, is_delete=0).distinct().count()
        return tagged_user_count

    else:
        return 0
