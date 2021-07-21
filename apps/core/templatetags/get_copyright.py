from django import template
register = template.Library()

import datetime


@register.filter("get_copyright")
def get_copyright(request):
    year = datetime.datetime.now().strftime('%Y')
    company = "Peace Factory"

    try:
        path_list = request.path.split("/")
        service_name = path_list[1]

        if service_name == "smartsec":
            company = "Peace Factory"

        elif service_name == "magicbot":
            company = "KINTOUN"

        elif service_name == "connect":
            company = "Peace Factory (SMSK)"

        elif service_name == "contactchat":
            company = "Peace Factory"

        return str(year) + " " + company

    except Exception as e:
        print("get_logo_max_width exception")
        print('%r' % e)
        return str(year) + " " + company
