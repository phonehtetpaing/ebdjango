from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# import models
from apps.core.models.end_user import EndUser
from apps.core.models.event import Event
from apps.core.models.vendor import Vendor
from apps.core.models.message_block import MessageBlock
from apps.core.models.todo_action_status import TodoActionStatus
from apps.core.models.todo import Todo
from apps.core.models.summary_log_end_users import SummaryLogEndUsers

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def index(request):
    user_obj = get_login_user_objects(request)
    vendor_branch_id = user_obj["vendor_branch"].id
    vendor_id = user_obj["vendor_branch"].vendor.id

    """ Dashboard Index """
    BG_COLOR_PRESET_LIST = ["#1FB6E9", "#F15424", "#29C4A9", "#F6FB4E", "#242D3C", "#E2DADB", "#C52F72"]
    BG_PROGRESS_BAR_TYPE_LIST = ["bg-danger", "bg-info", "bg-success", "bg-primary", "bg-warning"]

    user_obj = get_login_user_objects(request)

    # Total Conversation Rate
    try:
        sql_total_conversion_file = settings.BASE_DIR + "/apps/core/views/vendor_contactchat/statistics_sql/total_conversation_rate.sql"
        sql_total_conversion_base = open(sql_total_conversion_file, 'r').read()
        sql_total_conversion = sql_total_conversion_base.format(vendor_id=str(vendor_id))
        print("sql_total_conversion ====================")
        print(sql_total_conversion)

        summary_log_end_user = SummaryLogEndUsers.objects.raw(sql_total_conversion)[0]
        total_conversion_rate = round(summary_log_end_user.conversion_rate, 2)
    except Exception as e:
        total_conversion_rate = 0

    # Total Visitors
    try:
        sql_total_visitor_file = settings.BASE_DIR + "/apps/core/views/vendor_contactchat/statistics_sql/total_visitors.sql"
        sql_total_visitor_base = open(sql_total_visitor_file, 'r').read()
        sql_total_visitor = sql_total_visitor_base.format(vendor_id=str(vendor_id))
        print("sql_total_visitor ====================")
        print(sql_total_visitor)
        summary_log_end_user = SummaryLogEndUsers.objects.raw(sql_total_visitor)[0]
        total_visitors = summary_log_end_user.visitor_cnt
    except Exception as e:
        total_visitors = 0
    print("★")
    print(total_visitors)

    # get Todos numbers
    todo_action_status = TodoActionStatus.objects.filter(is_delete=False).exclude(name='DONE')
    todo_action_status_list = []
    for status in todo_action_status:
        todo_action_status_list.append(status.id)

    todos = Todo.objects.filter(vendor_branch_id=user_obj["vendor_branch"].id, todo_action_status_id__in=todo_action_status_list, is_delete=False)
    todocount = todos.count()

    # Weekly Conversion
    sql_weekly_conversion_file = settings.BASE_DIR + "/apps/core/views/vendor_contactchat/statistics_sql/weekly_conversion_rate.sql"
    sql_weekly_conversion_base = open(sql_weekly_conversion_file, 'r').read()
    sql_weekly_conversion = sql_weekly_conversion_base.format(vendor_id=str(vendor_id))
    print("sql_weekly_conversion ====================")
    print(sql_weekly_conversion)
    summary_log_end_users = SummaryLogEndUsers.objects.raw(sql_weekly_conversion)

    label_list = []
    data_list = []
    bg_color_list = []
    days_list = ["SUN", "MON", "TUE", "WEB", "THU", "FRI", "SAT"]

    # Should be 7 elements
    match_flg = 0
    for i in range(0, 7):
        label_list.append("\"" + days_list[i] + "\"")
        bg_color_list.append("\"" + BG_COLOR_PRESET_LIST[i] + "\"")

        for cv in summary_log_end_users:
            match_flg = 0
            if i == int(cv.log_day):
                if cv.conversion_rate is not None:
                    data_list.append(cv.conversion_rate)
                else:
                    data_list.append(0)
                match_flg = 1
                break

        if match_flg == 0:
            data_list.append(0)

        print("data_list --------")
        print(data_list)

    w_cv_label_list_string = ','.join(map(str, label_list))
    w_cv_data_list_string = ','.join(map(str, data_list))
    w_cv_bg_color_list_string = ','.join(map(str, bg_color_list))

    w_cv_rate_chart = {
        "labels": w_cv_label_list_string,
        "data": w_cv_data_list_string,
        "bg_color": w_cv_bg_color_list_string,
    }


    # Weekly Visitors
    sql_weekly_visitors_file = settings.BASE_DIR + "/apps/core/views/vendor_contactchat/statistics_sql/weekly_visitors.sql"
    sql_weekly_visitors_base = open(sql_weekly_visitors_file, 'r').read()
    sql_weekly_visitors = sql_weekly_visitors_base.format(vendor_id=str(vendor_id))
    print("sql_weekly_visitors ====================")
    print(sql_weekly_visitors)
    summary_log_end_users = SummaryLogEndUsers.objects.raw(sql_weekly_visitors)

    label_list = []
    data_list = []
    bg_color_list = []
    days_list = ["SUN", "MON", "TUE", "WEB", "THU", "FRI", "SAT"]

    # Should be 7 elements
    match_flg = 0
    for i in range(0,7):
        label_list.append("\"" + days_list[i] + "\"")
        bg_color_list.append("\"" + BG_COLOR_PRESET_LIST[i] + "\"")

        for visitor in summary_log_end_users:
            match_flg = 0
            if i == int(visitor.log_day):
                data_list.append(visitor.weekly_visitor_cnt)
                match_flg = 1
                break

        if match_flg == 0:
            data_list.append(0)

    w_visitor_label_list_string = ','.join(map(str, label_list))
    w_visitor_data_list_string = ','.join(map(str, data_list))
    w_visitor_bg_color_list_string = ','.join(map(str, bg_color_list))

    w_visitor_rate_chart = {
        "labels": w_visitor_label_list_string,
        "data": w_visitor_data_list_string,
        "bg_color": w_visitor_bg_color_list_string,
    }

    # Device Rate > 1: mobile 2: tablet  3: pc  4: other
    sql_device_file = settings.BASE_DIR + "/apps/core/views/vendor_contactchat/statistics_sql/device_rate.sql"
    sql_device_rate_base = open(sql_device_file, 'r').read()
    sql_device_rate = sql_device_rate_base.format(vendor_id=str(vendor_id))
    print("sql_device_rate ====================")
    print(sql_device_rate)
    summary_log_end_users = SummaryLogEndUsers.objects.raw(sql_device_rate)
    label_list = []
    data_list = []
    bg_color_list = []
    for device in summary_log_end_users:
        if device.device_type == 1:
            label_list.append("\"" + "Mobile" + "\"")
            bg_color_list.append("\"" + BG_COLOR_PRESET_LIST[0] + "\"")

        elif device.device_type == 2:
            label_list.append("\"" + "Tablet" + "\"")
            bg_color_list.append("\"" + BG_COLOR_PRESET_LIST[1] + "\"")

        elif device.device_type == 3:
            label_list.append("\"" + "PC" + "\"")
            bg_color_list.append("\"" + BG_COLOR_PRESET_LIST[2] + "\"")

        else:
            label_list.append("\"" + "Other" + "\"")
            bg_color_list.append("\"" + BG_COLOR_PRESET_LIST[3] + "\"")

        data_list.append(device.os_family_cnt)

    # Convert List to String
    device_label_list_string = ','.join(map(str, label_list))
    device_bg_color_list_string = ','.join(map(str, bg_color_list))
    device_data_list_string = ','.join(map(str, data_list))

    device_rate_chart = {
        "labels": device_label_list_string,
        "data": device_data_list_string,
        "bg_color": device_bg_color_list_string,
    }
    print("device_rate_chart ==== ")
    print(device_rate_chart)

    # OS Rate
    sql_os_file = settings.BASE_DIR + "/apps/core/views/vendor_contactchat/statistics_sql/os_rate.sql"
    sql_os_rate_base = open(sql_os_file, 'r').read()
    sql_os_rate = sql_os_rate_base.format(vendor_id=str(vendor_id))
    print("sql_os_rate_base ====================")
    print(sql_os_rate)
    summary_log_end_users = SummaryLogEndUsers.objects.raw(sql_os_rate)
    label_list = []
    data_list = []
    bg_color_list = []

    for i, os in enumerate(summary_log_end_users):
        label_list.append("\"" + os.os_family + "\"")
        data_list.append(os.os_family_cnt)
        bg_color_index = i % 6
        bg_color_list.append("\"" + BG_COLOR_PRESET_LIST[bg_color_index] + "\"")

    # Convert List to String
    os_label_list_string = ','.join(map(str, label_list))
    os_data_list_string = ','.join(map(str, data_list))
    os_bg_color_list_string = ','.join(map(str, bg_color_list))

    os_rate_chart = {
        "labels": os_label_list_string,
        "data": os_data_list_string,
        "bg_color": os_bg_color_list_string,
    }

    print("os_rate_chart ==== ")
    print(os_rate_chart)

    # Browser Rate
    sql_browser_file = settings.BASE_DIR + "/apps/core/views/vendor_contactchat/statistics_sql/browser_rate.sql"
    sql_browser_rate_base = open(sql_browser_file, 'r').read()
    sql_browser_rate = sql_browser_rate_base.format(vendor_id=str(vendor_id))
    print("sql_browser_rate ====================")
    print(sql_browser_rate)
    summary_log_end_users = SummaryLogEndUsers.objects.raw(sql_browser_rate)
    label_list = []
    data_list = []
    bg_color_list = []

    for i, browser in enumerate(summary_log_end_users):
        label_list.append("\"" + browser.browser_family + "\"")
        data_list.append(browser.browser_family_cnt)
        bg_color_index = i % 6
        bg_color_list.append("\"" + BG_COLOR_PRESET_LIST[bg_color_index] + "\"")

    # Convert List to String
    browser_label_list_string = ','.join(map(str, label_list))
    browser_data_list_string = ','.join(map(str, data_list))
    browser_bg_color_list_string = ','.join(map(str, bg_color_list))

    browser_rate_chart = {
        "labels": browser_label_list_string,
        "data": browser_data_list_string,
        "bg_color": browser_bg_color_list_string,
    }

    print("browser_rate_chart ==== ")
    print(browser_rate_chart)

    # Conversation_Percent
    sql_conversation_rate_file = settings.BASE_DIR + "/apps/core/views/vendor_contactchat/statistics_sql/conversation_rate.sql"
    sql_conversation_rate_base = open(sql_conversation_rate_file, 'r').read()

    conversation_bar_list = []
    message_blocks = MessageBlock.objects.filter(vendor_branch_id=vendor_branch_id, is_delete=False).all()
    for message_block in message_blocks:
        tmp_bar_dict = {
            "message_block_name": message_block.admin_text,
            "progress_numerator_list": [],
            "progress_denominator_list": []
        }

        sql_conversation_rate = sql_conversation_rate_base.format(vendor_id=str(vendor_id), message_block_id=str(message_block.id))
        print("debug: sql_conversation_rate")
        print(sql_conversation_rate)
        summary_log_end_users = SummaryLogEndUsers.objects.raw(sql_conversation_rate)

        for cv in summary_log_end_users:
            tmp_bar_dict["progress_numerator_list"].append(int(cv.progress_numerator))
            tmp_bar_dict["progress_denominator_list"].append(int(cv.progress_denominator))

        conversation_bar_list.append(tmp_bar_dict)

    print("conversation_bar_list =========")
    print(conversation_bar_list)

    conversation_rate_list = []
    for i, cv in enumerate(conversation_bar_list):
        if len(cv["progress_denominator_list"]) == 0:
            percentage = 0
        else:
            percentage = (sum(cv["progress_numerator_list"]) / sum(cv["progress_denominator_list"])) * 100

        tmp_dict = {
            "message_block_name": cv["message_block_name"],
            "bg_type": BG_PROGRESS_BAR_TYPE_LIST[i % len(BG_PROGRESS_BAR_TYPE_LIST)],
            "percentage": str(int(percentage))
        }

        conversation_rate_list.append(tmp_dict)

    print("conversation_rate_list")
    print(conversation_rate_list)

    context = {
        "title" : "Dashboard",
        "total_conversion_rate": total_conversion_rate,
        "total_visitors": total_visitors,
        "todocount" : todocount,
        "todos": todos,
        "w_cv_rate_chart": w_cv_rate_chart,
        "w_visitor_rate_chart": w_visitor_rate_chart,
        "device_rate_chart": device_rate_chart,
        "os_rate_chart": os_rate_chart,
        "browser_rate_chart": browser_rate_chart,
        "conversation_rate_list": conversation_rate_list,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor_contactchat/dashboard.html", context)



