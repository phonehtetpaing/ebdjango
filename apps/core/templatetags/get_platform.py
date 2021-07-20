from django import template
register = template.Library()

# import models
from apps.core.models.end_user_facebook import EndUserFacebook
from apps.core.models.end_user_line import EndUserLINE


@register.filter("get_platform")
def get_platform(end_user_id):
    try:
        platform_list = []
        end_user_facebook = EndUserFacebook.objects.filter(end_user_id=end_user_id).first()
        if end_user_facebook:
            platform_list.append("Facebook")
        end_user_line = EndUserLINE.objects.filter(end_user_id=end_user_id).first()
        if end_user_line:
            platform_list.append("LINE")

        if len(platform_list) == 0:
            return ""

        else:
            return "/".join(map(str, platform_list))

    except Exception as e:
        print("get_tag_ exception")
        print('%r' % e)
        return ""
