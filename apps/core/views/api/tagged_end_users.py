import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from copy import deepcopy

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.tag import Tag

# import views
from apps.core.views.vendor_common.login_user_info import *

# TODO: active CSRF
@csrf_exempt
def get_user_list(request):
    user_obj = get_login_user_objects(request)

    try:
        tag_id_list = request.GET.getlist('tag_id[]')

        if tag_id_list:
            tags = Tag.objects.filter(id__in=tag_id_list).all()
            tag_code_list = []
            for tag in tags:
                tag_code_list.append(tag.cd)

            end_users = EndUser.objects.filter(tag__name__in=tag_code_list, vendor_branch=user_obj["vendor_branch"], is_delete=0).distinct()

        else:
            end_users = EndUser.objects.filter(vendor_branch=user_obj["vendor_branch"], is_delete=0).all()

        display_user_list = []
        display_user_dict = {
            "id": None,
            "first_name": None,
            "last_name": None,
            "tag_id": None,
            "href_url_detail": None,
        }

        for user in end_users:
            tmp_dict = deepcopy(display_user_dict)
            tmp_dict['id'] = user.id
            tmp_dict['first_name'] = user.first_name
            tmp_dict['last_name'] = user.last_name
            tmp_dict['regist_dt'] = user.regist_dt.__str__()
            tmp_dict['href_url_detail'] = '/' + user_obj["service_url"] + '/user/detail/' + str(user.id) + '/'
            display_user_list.append(tmp_dict)

        status = 200
        result_data = {"users": display_user_list, "tag_list": tag_id_list}
        result_json = json.dumps(result_data)

    except Exception as e:
        status = 400
        result_data = {"result": "NG", "reason": '%r' % e}
        result_json = json.dumps(result_data)

    return HttpResponse(result_json, content_type='application/json; charset=UTF-8', status=status)