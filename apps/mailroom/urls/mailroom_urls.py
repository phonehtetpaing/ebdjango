from django.urls import path
from apps.mailroom.views import trigger_message
from apps.mailroom.views import direct_message
from apps.mailroom.views import message_history
from apps.mailroom.views import index

urlpatterns = [
    path('', index.index, name='ma_editor'),
    path('trigger/list/', trigger_message.list, name='trigger_message_list'),
    path('trigger/edit/<int:trigger_id>/', trigger_message.edit, name='trigger_message_edit'),
    path('trigger/delete/', trigger_message.delete, name='trigger_message_delete'),
    path('trigger/toggle/', trigger_message.toggle, name='trigger_message_toggle'),

    path('direct/edit/<int:message_id>/', direct_message.edit, name='direct_message_edit'),

    path('message_add/', trigger_message.add, name='message_add'),

    path('message_history/list/', message_history.list, name='message_history'),
    path('message_history/detail/<int:trigger_id>/', message_history.detail, name='message_history_detail'),
    path('message_history/delete/', message_history.delete, name='message_history_delete'),
]
