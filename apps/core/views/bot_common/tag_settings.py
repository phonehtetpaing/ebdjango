# -*- coding: utf-8 -*-
import json
from datetime import datetime
import time

# import models
from apps.core.models.tag_category import TagCategory
from apps.core.models.tag import Tag


def set_tag(end_user, payload):
    tag_name = ""
    try:
        tag_name = payload.tag_name
    except AttributeError:
        tag_name = payload['tag']

    if tag_name:

        tag_categories = TagCategory.objects.filter(vendor_branch=end_user.vendor_branch, is_delete=False).all()
        tag = Tag.objects.filter(tag_category__in=tag_categories, name=tag_name).first()

        if tag:
            end_user.tag.add(tag.cd)

        else:
            tag_category = TagCategory.objects.filter(vendor_branch=end_user.vendor_branch, is_delete=False).first()
            if not tag_category:
                tag_category = TagCategory(name="__default", vendor_branch=end_user.vendor_branch)
                tag_category.save()

            new_tag = Tag(tag_category=tag_category, name=tag_name)
            new_tag.save()
            code = str(end_user.vendor_branch.id) + "-" + str(new_tag.id)
            new_tag.cd = code
            new_tag.save()

            end_user.tag.add(new_tag.cd)
    return True


def remove_tag(end_user, payload):
    try:
        tag_name = payload.tag_name
    except AttributeError:
        tag_name = payload['tag']

    if tag_name:

        tag_categories = TagCategory.objects.filter(vendor_branch=end_user.vendor_branch, is_delete=False).all()
        tag = Tag.objects.filter(tag_category__in=tag_categories, name=tag_name).first()

        if tag:
            end_user.tag.remove(tag.cd)
            # todo cleanup unused tags?

    return True


def set_tag_from_input(end_user_info, input_text):

    end_user = end_user_info["end_user_obj"]
    user_state_cd = end_user.end_user_state.cd
    vendor_branch = end_user_info["vendor_branch"]

    if user_state_cd == "WAIT_TEXT_TAG":
        tag_categories = TagCategory.objects.filter(vendor_branch=vendor_branch, is_delete=False).all()
        tag = Tag.objects.filter(tag_category__in=tag_categories, name=input_text).first()

        if tag:
            end_user.tag.add(tag.cd)

        else:
            tag_category = TagCategory.objects.filter(vendor_branch=end_user.vendor_branch, is_delete=False).first()
            if not tag_category:
                tag_category = TagCategory(name="__default", vendor_branch=end_user.vendor_branch)
                tag_category.save()

            new_tag = Tag(tag_category=tag_category, name=input_text)
            new_tag.save()
            code = str(end_user.vendor_branch.id) + "-" + str(new_tag.id)
            new_tag.cd = code
            new_tag.save()

            end_user.tag.add(new_tag.cd)






    return None