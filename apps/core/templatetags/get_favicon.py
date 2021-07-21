from django import template
register = template.Library()


@register.filter("get_favicon")
def get_favicon(request):
    try:
        path_list = request.path.split("/")
        service_name = path_list[1]
        return "core/assets/images/favicon/" + service_name + ".ico"

    except Exception as e:
        print("get_favicon exception")
        print('%r' % e)
        return "core/assets/images/favicon.ico"
