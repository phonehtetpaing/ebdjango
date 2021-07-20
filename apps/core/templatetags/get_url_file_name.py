from django import template
register = template.Library()


@register.filter("get_url_file_name")
def get_url_file_name(value):
    file_name = value.rsplit('/', 1)[-1]
    if file_name:
        return file_name
    else:
        return 'File_not found'