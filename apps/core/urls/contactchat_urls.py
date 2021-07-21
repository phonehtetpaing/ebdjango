from django.urls import path
from apps.core.views.bot_callback.fbms import fbms_smartsec_callback
from apps.core.views.bot_callback.line import line_smartsec_callback
from apps.core.views.bot_callback.contactchat import contactchat_callback
from apps.core.views.vendor_contactchat import dashboard
from apps.core.views.vendor_contactchat import analytics
from apps.core.views.vendor import logout, files
from apps.core.views.vendor import todo
from apps.core.views.vendor_contactchat import settings_vendor
from apps.core.views.vendor import settings_tag
from apps.core.views.vendor import settings_vendor_account
from apps.core.views.vendor_contactchat import settings_style
from apps.core.views.vendor_contactchat import system_initial_setup
from apps.core.views.worker import message_worker
from apps.core.views.vendor_contactchat import block_message
from apps.core.views.vendor_contactchat import direct_message
from apps.core.views.vendor_common import end_user_registration
from apps.core.views.vendor.files import FileCreateView

urlpatterns = [
    # callback
    path('fbms/<string>/', fbms_smartsec_callback.MessageView.as_view()),
    path('fbms2/<string>/', fbms_smartsec_callback.MessageView.as_view()),
    path('line/<int:code>/', line_smartsec_callback.callback),
    path('line2/<int:code>/', line_smartsec_callback.callback),
    path('contactchat/<string>/', contactchat_callback.MessageView.as_view()),

    # admin pages
    path('dashboard/', dashboard.index, name='dashboard_index'),
    # Login
    path('logout/', logout.index, name='logout'),
    # TODOs
    path('todo/list/', todo.list, name='todo_list'),
    path('todo/detail/<int:todo_id>/', todo.detail, name='todo_detail'),
    path('todo/edit/<int:todo_id>/', todo.edit, name='todo_edit'),
    # User Story / Block Message
    path('block/message/', block_message.detail, name='block_message'),
    path('block/message/add/', block_message.add, name='block_message_add'),
    path('block/message/detail/<int:message_block_id>/', block_message.detail, name='block_message_detail'),
    path('block/message/edit/<int:message_block_id>/', block_message.edit, name='block_message_edit'),
    path('block/message/delete/<int:message_block_id>/', block_message.delete, name='block_message_delete'),
    path('block/message/template/', block_message.get_message_template, name='block_message_template'),

    # Documents
    path('files/', FileCreateView.as_view(), name='files'),
    path('files/delete/', files.delete, name='file_delete'),

    # Direct Message
    path('direct/message/', direct_message.index, name='direct_message'),

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
    path('settings/style/', settings_style.index, name='settings_style_index'),

    # Analytics
    path('analytics/', analytics.index, name='analytics_index'),

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
