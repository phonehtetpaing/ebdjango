from django.urls import path
from apps.core.views.sample import samples


urlpatterns = [
    path('index/', samples.index, name='sample_index'),
    path('index/send_message_test/', samples.send_message_test, name='send_message_test'),
    path('entry/recome/', samples.entry_recome, name='entry_recome'),
    path('entry/check/recome/', samples.entry_check_recome, name='entry_check_recome'),
]
