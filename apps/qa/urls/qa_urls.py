from django.urls import path, include
from apps.qa.views import index
from apps.qa.views import dashboard
from apps.qa.views import user
from apps.qa.views import slimma
from apps.qa.views import questionnaire
from apps.qa.views import coupon
from apps.qa.views import reservation
from apps.qa.views import settings
from apps.qa.views import notification
from apps.qa.views.common import activation
from apps.qa.views import business_partner
from apps.qa.views.product import product_category
from apps.qa.views.product import space
from apps.qa.views.product import product
from apps.qa.views.product import stock
from apps.qa.views.product import receiving
from apps.qa.views.product import shipping


urlpatterns = [
    # top/login
    path('', index.index, name='login_index'),
    path('register/', index.register, name='register_index'),
    path('account_activation_sent/', activation.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', activation.activate, name='activate'),
    path('logout/', index.logout, name='logout_index'),
    # admin pages
    path('dashboard/', dashboard.index, name='dashboard_index'),
    # QA
    path('questionnaire/add/<int:template_id>/', questionnaire.add, name='questionnaire_add'),
    path('questionnaire/edit/<int:questionnaire_id>/', questionnaire.edit, name='questionnaire_edit'),
    path('questionnaire/delete/<int:questionnaire_id>/', questionnaire.delete, name='questionnaire_delete'),
    path('questionnaire/list/', questionnaire.list, name='questionnaire_list'),
    path('questionnaire/summary/', questionnaire.summary, name='questionnaire_summary'),
    path('questionnaire/summary/<int:questionnaire_id>/', questionnaire.summary, name='questionnaire_summary'),
    path('questionnaire/question/', questionnaire.get_question_template, name='questionnaire_question_template'),
    path('questionnaire/summary/<int:questionnaire_id>/report/respondents/', questionnaire.get_respondent_report, name='questionnaire_report_respondents'),
    path('questionnaire/summary/<int:questionnaire_id>/<int:end_user_id>/responses/', questionnaire.get_respondent_responses, name='questionnaire_respondent_responses'),
    # Users
    path('user/<int:end_user_id>/', user.list, name='user_list'),
    path('user/', user.list, name='user_list'),

    # Coupons
    path('coupon/<int:coupon_id>/', coupon.edit, name='coupon_edit'),
    path('coupon/', coupon.edit, name='coupon_edit'),
    path('coupon/add', coupon.add, name='coupon_add'),
    path('coupon/delete/<int:coupon_id>/', coupon.delete, name='coupon_delete'),
    path('coupon/<int:coupon_id>/print/', coupon.print_coupon, name='coupon_print'),

    # Coupon redirecting
    path('coupon/claim/<int:coupon_id>/', coupon.claim, name='coupon_claim'),

    # Slim MA
    path('slimma/', slimma.index, name='ma_editor'),
    path('slimma/edit/<int:trigger_id>/', slimma.edit, name='ma_edit'),
    path('slimma/add', slimma.add, name='ma_add'),
    path('slimma/delete/<int:trigger_id>/', slimma.delete, name='ma_delete'),
    path('slimma/direct/<int:message_id>/', slimma.direct, name='ma_direct'),

    # Reservation
    path('reservation/', reservation.index, name='reservation_index'),
    path('reservation/template/list/', reservation.template_list, name='reservation_template_list'),
    path('reservation/template/', reservation.template_detail, name='reservation_template_new'),
    path('reservation/template/once/', reservation.template_once, name='reservation_template_once'),
    path('reservation/template/create/once/', reservation.template_create_once, name='reservation_template_create_once'),
    path('reservation/template/<int:template_id>/', reservation.template_detail, name='reservation_template_detail'),
    path('reservation/template/edit/<int:template_id>/', reservation.template_edit, name='reservation_template_edit'),
    path('reservation/template/delete/<int:template_id>/', reservation.template_edit, name='reservation_template_delete'),
    path('reservation/template/add/', reservation.template_add, name='reservation_template_add'),
    path('reservation/settings', reservation.settings, name='reservation_settings'),
    path('reservation/update/settings/', reservation.update_team_setting, name='reservation_update_settings'),
    path('reservation/account/', reservation.account_detail, name='reservation_account_detail'),
    path('reservation/account/update/', reservation.update_account_setting, name='reservation_update_account_setting'),
    path('reservation/schedule/now/list/', reservation.schedule_now_list, name='reservation_schedule_now_list'),
    path('reservation/schedule/past/list/', reservation.schedule_past_list, name='reservation_schedule_past_list'),
    path('reservation/schedule/delete/<int:schedule_history_id>/<str:mode_menu>/', reservation.schedule_delete, name='reservation_schedule_delete'),

    # Settings
    path('settings/profile/', settings.profile, name='settings_profile'),
    path('settings/plan/', settings.plan, name='settings_plan'),
    path('settings/notification/<int:service_id>/', settings.notification, name='settings_notification'),
    path('settings/notification/', settings.notification, name='settings_notification'),
    path('settings/style/', settings.style, name='settings_style'),

    # Notification
    path('notification/detail/<int:notification_id>/', notification.detail, name='notification_detail'),
    path('notification/list/', notification.list, name='notification_read'),
    path('notification/set_all_read/', notification.set_all, name='notification_set_all'),

    # Business Partner
    path('bp/list/', business_partner.list, name='bp_list'),
    path('bp/<int:bp_id>/', business_partner.edit, name='bp_edit'),
    path('bp/', business_partner.edit, name='bp_edit'),
    path('bp/add/', business_partner.add, name='bp_add'),
    path('bp/delete/<int:bp_id>/', business_partner.delete, name='bp_delete'),
    path('bp/tag/list/', business_partner.tag_list, name='bp_tag_list'),
    path('bp/tag/<int:bp_tag_id>/', business_partner.tag_edit, name='bp_tag_edit'),
    path('bp/tag/', business_partner.tag_edit, name='bp_tag_edit'),
    path('bp/tag/add/', business_partner.tag_add, name='bp_tag_add'),
    path('bp/tag/delete/<int:bp_tag_id>/', business_partner.tag_delete, name='bp_tag_delete'),

    # Product Category
    path('product/category/list/', product_category.list, name='pc_list'),
    path('product/category/', product_category.edit, name='pc_edit'),
    path('product/category/<int:pc_id>/', product_category.edit, name='pc_edit'),
    path('product/category/add/', product_category.add, name='pc_add'),
    path('product/category/delete/<int:pc_id>/', product_category.delete, name='pc_delete'),

    # Stock Space
    path('product/space/list/', space.list, name='ss_list'),
    path('product/space/', space.edit, name='ss_edit'),
    path('product/space/<int:ss_id>/', space.edit, name='ss_edit'),
    path('product/space/add/', space.add, name='ss_add'),
    path('product/space/delete/<int:ss_id>/', space.delete, name='ss_delete'),

    # Product
    path('product/list/', product.list, name='product_list'),
    path('product/', product.edit, name='product_edit'),
    path('product/<int:product_id>/', product.edit, name='product_edit'),
    path('product/add/', product.add, name='product_add'),
    path('product/delete/<int:product_id>/', product.delete, name='product_delete'),

    # Stock
    path('stock/list/', stock.list, name='stock_list'),
    path('stock/', stock.edit, name='stock_edit'),
    path('stock/<int:stock_id>/', stock.edit, name='stock_edit'),
    path('stock/add/', stock.add, name='stock_add'),
    path('stock/delete/<int:stock_id>/', stock.delete, name='stock_delete'),

    # Receiving
    path('receiving/entry/', receiving.entry, name='receiving_entry'),
    path('receiving/add/', receiving.add, name='receiving_add'),
    path('receiving/history/list/', receiving.history_list, name='receiving_history_list'),
    path('receiving/history/<int:history_id>/', receiving.history_detail, name='receiving_history_detail'),

    # Shipping
    path('shipping/entry/', shipping.entry, name='shipping_entry'),
    path('shipping/add/', shipping.add, name='shipping_add'),
    path('shipping/history/list/', shipping.history_list, name='shipping_history_list'),
    path('shipping/history/<int:history_id>/', shipping.history_detail, name='shipping_history_detail'),

]
