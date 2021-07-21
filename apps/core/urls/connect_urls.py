from django.urls import path
from django.conf.urls import url
from apps.core.views.bot_callback.fbms import fbms_smartsec_callback
from apps.core.views.bot_callback.line import line_smartsec_callback
from apps.core.views.vendor_connect import dashboard
from apps.core.views.vendor import logout
from apps.core.views.vendor import user
from apps.core.views.vendor import todo
from apps.core.views.vendor import auto_message
from apps.core.views.vendor import message_history
from apps.core.views.vendor import manual_message
from apps.core.views.vendor import settings_vendor
from apps.core.views.vendor import settings_tag
from apps.core.views.vendor import settings_vendor_account
from apps.core.views.vendor import system_initial_setup
from apps.core.views.worker import message_worker
from apps.core.views.vendor import block_message
from apps.core.views.worker import manual_message as worker_manual_message
from apps.core.views.vendor_common import end_user_registration


urlpatterns = [
    # callback
    path('fbms/<string>/', fbms_smartsec_callback.MessageView.as_view()),
    path('fbms2/<string>/', fbms_smartsec_callback.MessageView.as_view()),
    path('line/<int:code>/', line_smartsec_callback.callback),
    path('line2/<int:code>/', line_smartsec_callback.callback),

    # admin pages
    path('dashboard/', dashboard.index, name='dashboard_index'),
    # Login
    path('logout/', logout.index, name='logout'),
    # User
    path('user/list/', user.list, name='user_list'),
    path('user/detail/<int:end_user_id>/', user.detail, name='user_detail'),
    path('user/edit/<int:end_user_id>/', user.edit, name='user_edit'),
    path('user/delete/', user.delete, name='user_delete'),
    # TODOs
    path('todo/detail/<int:todo_id>/', todo.detail, name='todo_detail'),
    path('todo/edit/<int:todo_id>/', todo.edit, name='todo_edit'),
    # User Story / Block Message
    path('block/message/', block_message.detail, name='block_message'),
    path('block/message/add/', block_message.add, name='block_message_add'),
    path('block/message/detail/<int:message_block_id>/', block_message.detail, name='block_message_detail'),
    path('block/message/edit/<int:message_block_id>/', block_message.edit, name='block_message_edit'),
    path('block/message/delete/<int:message_block_id>/', block_message.delete, name='block_message_delete'),
    # Auto Mesasge
    path('auto/message/list/', auto_message.list, name='auto_message_list'),
    path('auto/message/detail/<int:auto_message_id>/', auto_message.detail, name='auto_message_detail'),
    path('auto/message/test/<int:auto_message_id>/', auto_message.send_test, name='auto_message_test'),
    path('auto/message/add/<int:auto_message_condition_id>/', auto_message.add, name='auto_message_add'),
    path('auto/message/add/confirm/<int:auto_message_id>/', auto_message.confirm, name='auto_message_confirm'),
    path('auto/message/edit/<int:auto_message_id>/', auto_message.edit, name='auto_message_edit'),
    path('auto/message/delete/', auto_message.delete, name='auto_message_delete'),
    path('auto/message/inactive/<int:auto_message_id>/', auto_message.inactive, name='auto_message_inactive'),
    path('auto/message/active/<int:auto_message_id>/', auto_message.active, name='auto_message_active'),
    path('auto/message/history/list/', message_history.list, name='auto_message_history_list'),
    path('auto/message/history/detail/<int:auto_message_history_id>/', message_history.detail, name='auto_message_history_detail'),
    # Manual Message
    path('manual/message/list/', manual_message.list, name='manual_message_list'),
    path('manual/message/detail/<int:message_id>/', manual_message.detail, name='manual_message_detail'),
    path('manual/message/test/<int:message_id>/', manual_message.send_test, name='manual_message_test'),
    path('manual/message/confirm/<int:message_id>/', manual_message.send_confirm, name='manual_message_confirm'),
    path('manual/message/send/<int:message_id>/', manual_message.send_message, name='manual_message_send'),
    path('manual/message/add/', manual_message.add, name='manual_message_add'),
    path('manual/message/edit/<int:message_id>/', manual_message.edit, name='manual_message_edit'),
    path('manual/message/delete/', manual_message.delete, name='manual_message_delete'),
    path('manual/message/history/detail/<int:manual_message_history_id>/', message_history.manual_detail, name='manual_message_history_detail'),
    # Settings
    path('settings/vendor/', settings_vendor.index, name='setting_vendor_index'),
    path('settings/vendor/edit/<int:vendor_id>/', settings_vendor.edit, name='setting_vendor_edit'),
    path('settings/organization/list/', settings_vendor.organization_list, name='settings_organization_list'),
    path('settings/organization/detail/<int:message_id>/', settings_vendor.organization_detail, name='settings_organization_detail'),
    path('settings/account/list/', settings_vendor.account_list, name='settings_account_list'),
    path('settings/account/detail/<int:vendor_user_id>/', settings_vendor_account.detail, name='settings_vendor_account_detail'),
    path('settings/account/add/', settings_vendor_account.add, name='settings_vendor_account_add'),
    path('settings/account/create/', settings_vendor_account.create_user, name='settings_vendor_account_create'),
    path('settings/account/edit/<int:vendor_user_id>/', settings_vendor_account.edit, name='settings_vendor_account_edit'),
    path('settings/account/login/detail/<int:vendor_user_id>/', settings_vendor_account.login_detail, name='settings_vendor_account_login_detail'),
    path('settings/account/login/edit/<int:vendor_user_id>/', settings_vendor_account.login_edit, name='settings_vendor_account_login_edit'),
    path('settings/tag/', settings_tag.index, name='setting_tag_index'),
    path('settings/tag/<int:tag_category_id>/detail/<int:tag_id>/', settings_tag.detail, name='settings_tag_detail'),
    path('settings/tag/<int:tag_category_id>/add/<int:tag_id>/', settings_tag.add, name='settings_tag_add'),
    path('settings/tag/<int:tag_category_id>/edit/<int:tag_id>/', settings_tag.edit, name='settings_tag_edit'),
    path('settings/tag/delete/', settings_tag.delete, name='settings_tag_delete'),

    # Registration
    path('registration/line/entry/', end_user_registration.line_entry, name='registration_line_entry'),
    path('registration/fbms/entry/', end_user_registration.fbms_entry, name='registration_fbms_entry'),
    path('registration/check/<int:end_user_id>/', end_user_registration.check, name='registration_check'),
    path('registration/update/', end_user_registration.update_affiliate, name='registration_update'),

    # System
    path('system/initial/setup/', system_initial_setup.list, name='system_initial_setup_list'),
    path('system/initial/setup/detail/<int:vendor_id>/', system_initial_setup.detail, name='system_initial_setup_detail'),
    path('system/initial/setup/edit/<int:vendor_id>/', system_initial_setup.edit, name='system_initial_setup_edit'),
    path('system/initial/setup/add/', system_initial_setup.add, name='system_initial_setup_add'),
    path('system/initial/setup/new/', system_initial_setup.new, name='system_initial_setup_new'),

    # Worker
    path('worker/send/message/', message_worker.send_message, name='worker_send_message'),
]
