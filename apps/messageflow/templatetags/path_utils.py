from django import template
from django.shortcuts import resolve_url, reverse, redirect
from pathlib import Path
register = template.Library()


@register.simple_tag(name='partial_url')
def partial_url(viewname, *args, **kwargs):
    kwargs['base_template'] = Path(kwargs['base_template']).stem if 'base_template' in kwargs and not kwargs['base_template'] is None else None
    kwargs['template'] = Path(kwargs['template']).stem if 'template' in kwargs and not kwargs['template'] is None else None

    return reverse(viewname, kwargs=kwargs)


@register.filter()
def path_to_name(path):
    return Path(path).stem if path is not None else None
