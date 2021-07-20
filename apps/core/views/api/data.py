from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

# import Models
from apps.core.models import EndUser, EndUserLINE, EndUserFacebook, TagCategory, Tag

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def get_platforms(request, *args, **kwargs):
    user_obj = get_login_user_objects(request)

    all_users = EndUser.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False)
    all_line_user = EndUserLINE.objects.filter(end_user_id__in=all_users, is_delete=False)
    all_facebook_user = EndUserFacebook.objects.filter(end_user_id__in=all_users, is_delete=False)

    only_line = all_line_user.exclude(end_user_id__in=all_facebook_user.values_list('end_user_id', flat=True))
    only_facebook = all_facebook_user.exclude(end_user_id__in=all_line_user.values_list('end_user_id', flat=True))
    # this is technically all users that are not exclusive to one platform so that includes users
    # with no platform at all. This should never occur in reality though as users sign up through a platform
    both_platforms = all_users.exclude(id__in=only_facebook.values_list('end_user_id', flat=True))
    both_platforms = both_platforms.exclude(id__in=only_line.values_list('end_user_id', flat=True))

    data = {
        "labels": ["Multiple Platforms", "FaceBook", "Line"],
        "default": [both_platforms.count(), only_facebook.count(), only_line.count()],
        "colors": [],
    }

    return JsonResponse(data)


@login_required
def get_tag_ranking(request, *args, **kwargs):
    user_obj = get_login_user_objects(request)

    all_users = EndUser.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False)
    top_tag = EndUser.tag.most_common(
        min_count=1, extra_filters={
            'enduser__in': all_users
        }
    )

    values = []
    labels = []
    for tag in top_tag:
        labels.append(get_tag_name(tag.name))
        values.append(tag.num_times)

    data = {
        "labels": labels,
        "default": values,
        "colors": [],
    }
    return JsonResponse(data)


def get_tag_name(value):
    tag_name = Tag.objects.filter(cd=value).first().name
    if tag_name:
        return tag_name
    else:
        return 'TAG_NOT_FOUND'