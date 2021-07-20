from django import template
register = template.Library()
from django.conf import settings


from apps.core.models.affiliate import Affiliate


@register.filter("get_affiliate_line_url")
def get_affiliate_line_url(value):
    if value:
        affiliate = Affiliate.objects.filter(id=int(value)).first()

        # https://xxxx.com/registration/entry/<string>/&openExternalBrowser=1
        # Generate Affiliate URL
        root_rul = settings.ROOT_URL
        service_name = affiliate.vendor_branch.vendor.service.name
        code = affiliate.url_part

        if settings.MODE == 'LOCAL':
            root_rul = settings.ROOT_URL_PUBLIC

        affiliate_url = root_rul + "/" + service_name + "/registration/line/entry/?code=" + code + "&di=" + str(affiliate.id) + "&openExternalBrowser=1"

        return affiliate_url

    else:
        return ""


@register.filter("get_affiliate_fbms_url")
def get_affiliate_fbms_url(value):
    if value:
        affiliate = Affiliate.objects.filter(id=int(value)).first()

        # https://xxxx.com/registration/entry/<string>/&openExternalBrowser=1
        # Generate Affiliate URL
        root_rul = settings.ROOT_URL
        service_name = affiliate.vendor_branch.vendor.service.name
        code = affiliate.url_part + str(affiliate.id)

        if settings.MODE == 'LOCAL':
            root_rul = settings.ROOT_URL_PUBLIC

        affiliate_url = root_rul + "/" + service_name + "/registration/fbms/entry/?code=" + code + "&di=" + str(affiliate.id) + "&openExternalBrowser=1"

        return affiliate_url

    else:
        return ""


