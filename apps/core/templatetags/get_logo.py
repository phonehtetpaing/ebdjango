from django import template
register = template.Library()


@register.filter("get_logo")
def get_logo(request):
    try:
        path_list = request.path.split("/")
        service_name = path_list[1]
        return "core/assets/images/logo/" + service_name + ".png"

    except Exception as e:
        print("get_tag_ exception")
        print('%r' % e)
        return "core/assets/images/logo.png"
