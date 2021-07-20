from django.urls import path

# import views
from apps.core.views.bot_callback.line import line_recome_callback
from apps.core.views.vendor_common import line_registration, line_update_registration

urlpatterns = [
    # callback
    path('line/<str:code>/', line_recome_callback.callback),
    path('registration/line/entry/', line_registration.entry, name='registration_line_entry'),
    path('registration/line/check/<int:user_id>/', line_registration.check, name='registration_line_check'),
    path('registration/line/update/', line_update_registration.user_registration_update, name='registration_line_update'),
]
