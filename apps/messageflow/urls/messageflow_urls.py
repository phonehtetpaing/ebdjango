from django.urls import path, register_converter
# import views
from apps.messageflow.views import bot, scenario, user, message


class OptionalStringConverter:
    # regex = '(\w+/)+(\w+.html)'
    # regex = "('.*')"
    regex = '((_)*[a-zA-Z]+)*'

    def to_python(self, value):
        if value:
            return str(value)
        else:
            return None

    def to_url(self, value):
        return str(value) if value is not None else ''


register_converter(OptionalStringConverter, 'opt_str')

urlpatterns = [
    # bot urls
    path('<opt_str:base_template>/bot/', bot.list, name='bot_list'),
    path('bot/', bot.list, name='bot_list'),
    path('<opt_str:base_template>/bot/add/', bot.edit, name='bot_add'),
    path('<opt_str:base_template>/bot/edit/<int:bot_id>/', bot.edit, name='bot_edit'),
    path('<opt_str:base_template>/bot/delete/<int:bot_id>/', bot.delete, name='bot_delete'),
    path('bot/toggle/', bot.toggle, name='bot_toggle'),

    # scenario urls
    path('<opt_str:base_template>/scenario/', scenario.list, name='scenario_list'),
    path('<opt_str:base_template>/scenario/add/', scenario.add, name='scenario_add'),
    path('<opt_str:base_template>/scenario/edit/<int:scenario_id>/', scenario.edit, name='scenario_edit'),
    path('<opt_str:base_template>/scenario/delete/<int:scenario_id>/', scenario.delete, name='scenario_delete'),

    # message urls
    path('scenario/message/', scenario.get_message_template, name='scenario_message_template'),
    path('scenario/message/option/', scenario.get_message_option_template, name='message_option_add'),
    path('scenario/message/block/add/', scenario.add_message_block, name='message_block_add'),
    path('scenario/message/block/order/', scenario.update_message_block_display_order, name='message_block_order'),
    path('scenario/message/block/set/', scenario.get_message_block_message_set, name='message_block_set'),

    # direct message urls
    path('<opt_str:base_template>/targeted/', message.targeted, name='targeted_message'),
    path('targeted/count', message.targeted_count, name='targeted_message_count'),
    path('message/direct/', user.send_direct_message, name='send_direct_message'),
    path('message/update/', user.get_log_lines, name='update_message'),

    # user urls
    path('<opt_str:base_template>/user/', user.list, name='user_list'),
    path('<opt_str:base_template>/user/edit/<int:user_id>/', user.edit, name='user_edit'),
]
