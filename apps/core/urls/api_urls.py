from django.urls import path
from django.conf.urls import url
from apps.core.views.api import tagged_end_users, data, message
from apps.core.views.api.stats import load_files, logs_history, run_athena_query

urlpatterns = [
    path('tagged_end_users/', tagged_end_users.get_user_list, name='tagged_end_users'),
    path('data/platforms/', data.get_platforms, name='data_platforms'),
    path('data/tag/ranking/', data.get_tag_ranking, name='data_tag_ranking'),

    path('message/block/list/', message.get_message_blocks, name='data_message_blocks'),
    path('stats/load_csv/', load_files.load_to_rds, name='load_to_rds'),
    path('stats/logs/insert/', logs_history.insert_history, name='log_insert_history'),
    path('stats/athena/query/', run_athena_query.run_query, name='run_athena_query'),
]
