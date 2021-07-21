from django import template
register = template.Library()


@register.filter("get_page_title")
def get_page_title(request):
    try:
        path_list = request.path.split("/")
        service_name = path_list[1]

        if service_name == "smartsec":
            return "Smart Sec"

        elif service_name == "magicbot":
            return "Magic bot"

        elif service_name == "connect":
            return "Connect"

        elif service_name == "contactchat":
            return "ContactChat"

    except Exception as e:
        print("get_page_title exception")
        print('%r' % e)
        return "powered by SmartBy"
