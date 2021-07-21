from django import template
from django.utils import translation
from django.db.models import Count

# import models
from apps.mailroom.models.message import Message, MessageTemplate, MessageTemplateCategory

register = template.Library()


@register.filter
def get_message_templates_category(request):
    language = translation.get_language_from_request(request)
    # MessageTemplate.objects.filter(message__app_id="mail_template", language_code=language)

    # template_category_list = MessageTemplateCategory.objects.filter(language_code=language)

    template_category_list = MessageTemplateCategory.objects.filter(language_code=language).prefetch_related('message_templates').all()

    return template_category_list
