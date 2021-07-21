from django.urls import path, include
from apps.nchat.views import index
from apps.nchat.views.business import business, business_plan
from apps.nchat.views.payment import payment_history, payment
from apps.nchat.views import webhook
from apps.nchat.views import settings

urlpatterns = [
    # top/login
    path('', index.login, name='login_index'),
    path('<str:service_name>/', index.service_login, name='login_index'),
    path('logout/', index.logout, name='logout_index'),
    path('register/', index.register, name='register_index'),
    path('register/<str:service_name>/', index.register, name='register_index'),

    path('settings/', settings.index, name='settings_index'),
    path('settings/webhooks/', settings.webhooks, name='settings_webhooks'),
    path('settings/files/', settings.FileCreateView.as_view(), name='settings_files'),
    path('settings/files/delete/', settings.file_delete, name='file_delete'),

    path('business/detail/<int:business_id>/', business.detail, name='business_detail'),
    path('business/detail/', business.detail, name='business_detail'),

    path('plan/detail/', business_plan.detail, name='business_plan_detail'),
    path('plan/list/', business_plan.list, name='business_plan_list'),
    path('plan/add/', business_plan.add, name='business_plan_add'),
    path('plan/edit/<int:plan_id>/', business_plan.edit, name='business_plan_edit'),
    path('plan/delete/<int:plan_id>/', business_plan.delete, name='business_plan_delete'),

    path('payment/history/list/', payment_history.list, name='payment_history_list'),
    path('payment/edit/', payment.edit, name='payment_edit'),
    path('payment/checkout/<int:plan_id>/', payment.checkout, name='payment_checkout'),
    path('payment/webhook/', payment.webhook, name='payment_webhook'),

    # message flow
    path('messageflow/', include(('apps.messageflow.urls.messageflow_urls', 'messageflow'), namespace='messageflow')),

    # mailroom
    path('mailroom/', include(('apps.mailroom.urls.mailroom_urls', 'mailroom'), namespace='mailroom')),

    # line
    path('webhooks/line/<int:access_url_part>/<int:bot_id>/', webhook.line_callback, name='line_webhook'),
    path('webhooks/line/<int:access_url_part>/', webhook.line_callback, name='line_webhook'),
    path('webhooks/line/', webhook.line),

]
