from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, get_object_or_404

# import models
from django.template.loader import render_to_string

from apps.messageflow.models import LogLine
from apps.messageflow.models.end_user import EndUser

# import usecases
from apps.messageflow.usecases.message import SendDirectMessage
from apps.messageflow.usecases.user import AuthorizeUser
from apps.messageflow.usecases.template import RetrieveTemplates


@login_required()
def list(request, base_template=None, template=None):
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'user/user_list', base_template, template).execute()

    end_users = EndUser.objects.filter(owner_id=service_info['owner_id'], app_id=service_info['app_id']).all()

    context = {
        'object_list': end_users,
        'namespace': service_info['namespace'],
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        }
    }

    return render(request, template_info['template'], context)


@login_required()
def edit(request, base_template=None, template=None, user_id=None):
    service_info = AuthorizeUser(request.user, request.path).execute()
    template_info = RetrieveTemplates(service_info, 'user/user_edit', base_template, template).execute()

    # retrieve object and make sure it belongs to this context of owner and app
    user = get_object_or_404(EndUser, pk=user_id, owner_id=service_info['owner_id'], app_id=service_info['app_id'])

    # get chat log illustrating the recorded message history for this user instance
    loglines = LogLine.objects.filter(user_id=user.id, owner_id=service_info['owner_id'], app_id=service_info['app_id']).all()

    context = {
        'user': user,
        'loglines': loglines,
        'namespace': service_info['namespace'],
        'base_template': template_info['base_template'],
        'args': {
            'base_template': base_template,
            'template': template,
        }
    }

    return render(request, template_info['template'], context)


@login_required()
def send_direct_message(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    try:
        if request.POST:
            user_id = request.POST['user_id']
            message = request.POST['message']
            user = get_object_or_404(EndUser, id=user_id)

            SendDirectMessage(request, user, message).execute()
            return HttpResponse(200)
        else:
            return HttpResponseBadRequest()
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()


@login_required()
def get_log_lines(request):
    service_info = AuthorizeUser(request.user, request.path).execute()
    # retrieve object and make sure it belongs to this context of owner and app
    user = get_object_or_404(EndUser, pk=request.GET['user_id'], owner_id=service_info['owner_id'], app_id=service_info['app_id'])

    # get chat log illustrating the recorded message history for this user instance
    loglines = LogLine.objects.filter(user_id=user.id, owner_id=service_info['owner_id'],
                                      app_id=service_info['app_id']).all()

    context = {
        'user': user,
        'loglines': loglines,
    }
    return JsonResponse({'template': render_to_string('messageflow/user/log_lines.html', context)})
