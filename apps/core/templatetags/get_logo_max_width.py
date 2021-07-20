from django import template
register = template.Library()


@register.filter("get_logo_max_width")
def get_logo_max_width(request):
    try:
        path_list = request.path.split("/")
        service_name = path_list[1]

        if service_name == "smartsec":
            return "max-width:50px;"

        elif service_name == "magicbot":
            return "max-width:200px;"

        elif service_name == "connect":
            return "max-width:50px;"

        elif service_name == "contactchat":
            return "max-width:200px;"

    except Exception as e:
        print("get_logo_max_width exception")
        print('%r' % e)
        return "max-width:200px;"
