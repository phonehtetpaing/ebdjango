from django import template
from apps.qa.views.common.login_user_info import get_login_user_objects
register = template.Library()

# Notification Alert dependencies
from apps.qa.models.notification_history import NotificationHistory
from apps.qa.models.notification import Notification

@register.filter
def get_vendor_image(request):
    try:
        user_obj = get_login_user_objects(request)
        vendor = user_obj['vendor_branch'].vendor
        if vendor.picture_url:
            return vendor.picture_url.url
        else:
            return False
    except Exception as e:
        print('qa_core exception: ', e)
        return False


@register.filter
def get_vendor_user_name(request):
    try:
        user_obj = get_login_user_objects(request)
        vendor_user = user_obj["vendor_user"]
        return vendor_user.get_full_name()
    except Exception as e:
        print('qa_core exception: ', e)
        return 'John Doe'


@register.filter
def get_notifications_list(request):
    user_obj = get_login_user_objects(request)

    notification_history_list = NotificationHistory.objects.filter(seen=0, vendor_user_id=user_obj["vendor_user"]).order_by("-notification__schedule_dt").all()

    notification_history_dict = {"notifications": notification_history_list, "unread_count": len(notification_history_list)}

    return notification_history_dict

