from django.utils import timezone

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
# import models
from apps.core.models.tag import Tag
from apps.core.models.tag_category import TagCategory

# import views
from apps.core.views.vendor_common.login_user_info import *

# import forms
from apps.core.forms.tag import TagForm


@login_required
def index(request):
    """ list """
    user_obj = get_login_user_objects(request)
    tag_categories = TagCategory.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, is_delete=False).order_by("display_order_num").all()
    tag_category_list = []
    for tag_category in tag_categories:
        tag_category_list.append(tag_category.id)

    tag_list = Tag.objects.filter(tag_category_id__in=tag_category_list, is_delete=False).order_by("id").all()
    page = request.GET.get('page', 1)

    paginator = Paginator(tag_list, settings.RESULTS_PER_PAGE)
    try:
        tags = paginator.page(page)
    except PageNotAnInteger:
        tags = paginator.page(1)
    except EmptyPage:
        tags = paginator.page(paginator.num_pages)

    context = {
        "title": "Tag List",
        "path": ["Settings", "Tag List"],
        "tags": tags,
        "tag_categories": tag_categories,
        "tag_category_id": tag_categories.first().id,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings_tag_index.html", context)


@login_required
def detail(request, tag_category_id=None, tag_id=None):
    """ tag detail """
    user_obj = get_login_user_objects(request)

    tag = Tag.objects.filter(id=tag_id).first()

    form = TagForm(request.POST or None, instance=tag)
    if form.is_valid():
        tag = form.save(commit=False)
        tag.update_dt = timezone.now()
        tag.save()

    context = {
        "title": "Tag Details",
        "path": ["Settings", "Tag List", "Tag Details"],
        "tag": tag,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings_tag_detail.html", context)


@login_required
def add(request, tag_category_id=None, tag_id=None):
    """ New Tag Page """
    user_obj = get_login_user_objects(request)

    tag = Tag()
    tag_category = TagCategory.objects.filter(id=tag_category_id).first()
    tag.tag_category = tag_category
    tag.save()
    form = TagForm(request.POST or None, instance=tag)

    context = {
        "title": "Tag Details",
        "path": ["Settings", "Tag List", "Tag Details"],
        "tag": tag,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings_tag_detail.html", context)


@login_required
def edit(request, tag_category_id=None, tag_id=None):
    """ tag edit """
    user_obj = get_login_user_objects(request)
    tag_category = TagCategory.objects.filter(id=tag_category_id).first()

    tag = Tag.objects.filter(id=tag_id).first()

    form = TagForm(request.POST or None, instance=tag)
    if form.is_valid():
        tag = form.save(commit=False)
        tag.update_dt = timezone.now()
        # CODE: vendor_branch_id - tag_id
        code = str(user_obj["vendor_branch"].id) + "-" + str(tag.id)
        tag.cd = code
        tag.save()

        redirect_url = "/" + user_obj["service_url"] + "/settings/tag/"
        return redirect(redirect_url)

    context = {
        "title": "Tag Details",
        "path": ["Settings", "Tag List", "Tag Details"],
        "tag": tag,
        "form": form,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor/settings_tag_detail.html", context)


@login_required
def delete(request):
    """ tag edit """
    user_obj = get_login_user_objects(request)

    if request.method == "POST":
        delete_ids = request.POST.getlist('select_item')
        tag = Tag.objects.filter(id__in=delete_ids)
        tag.update(is_delete=1)

    redirect_url = "/" + user_obj["service_url"] + "/settings/tag/"
    return redirect(redirect_url)
