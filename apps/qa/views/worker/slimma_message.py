# -*- coding:utf-8 -*-

# import models
from apps.qa.models.ma_trigger_type import MaTriggerType
from apps.qa.models.ma_trigger import MaTrigger

# import views
from apps.qa.views.utilities.trigger_events import *


def send_slimma_message(trigger_type_id, batch_start_dt, worker_sqs_status):
    print("sending slimma message")

    # check datetime for target datetime
    # batch_buffer_min = 4
    # batch_start_dt_gt = batch_start_dt + datetime.timedelta(minutes=batch_buffer_min)
    # batch_start_dt_lt = batch_start_dt - datetime.timedelta(minutes=batch_buffer_min)

    # Get triggers
    try:
        trigger_type = MaTriggerType.objects.filter(id=trigger_type_id).first()

        if trigger_type.name == 'after joining':
            print("after joining trigger")
            after_registration_triggers = MaTrigger.objects.filter(trigger_type=trigger_type).all()
            for registration_trigger in after_registration_triggers:
                send_after_joining_type_message(registration_trigger)

        elif trigger_type.name == 'after taking survey':
            pass

        elif trigger_type.name == 'after using coupon':
            print("after using coupon")
            after_coupon_triggers = MaTrigger.objects.filter(trigger_type=trigger_type).all()
            for coupon_trigger in after_coupon_triggers:
                send_after_using_coupon_message(coupon_trigger)

        elif trigger_type.name == 'after no activity':
            after_no_activity_triggers = MaTrigger.objects.filter(trigger_type=trigger_type).all()
            for after_no_activity_trigger in after_no_activity_triggers:
                send_after_no_activity_message(after_no_activity_trigger)

        elif trigger_type.name == 'after new survey goes live':
            after_new_survey_triggers = MaTrigger.objects.filter(trigger_type=trigger_type).all()
            for after_new_survey_trigger in after_new_survey_triggers:
                send_after_no_activity_message(after_new_survey_trigger)

        elif trigger_type.name == 'after new coupon goes live':
            after_new_coupon_triggers = MaTrigger.objects.filter(trigger_type=trigger_type).all()
            for after_new_coupon_trigger in after_new_coupon_triggers:
                send_after_no_activity_message(after_new_coupon_trigger)

        elif trigger_type.name == 'before coupon expires':
            triggers = MaTrigger.objects.filter(trigger_type=trigger_type).all()
            for trigger in triggers:
                send_before_coupon_expires_message(trigger)

        elif trigger_type.name == 'before survey expires':
            triggers = MaTrigger.objects.filter(trigger_type=trigger_type).all()
            for trigger in triggers:
                send_before_survey_expires_message(trigger)

        elif trigger_type.name == 'before birthday':
            triggers = MaTrigger.objects.filter(trigger_type=trigger_type).all()
            for trigger in triggers:
                send_before_birthday_message(trigger)

        else:
            pass
        # worker
        worker_sqs_status.status = 4
        worker_sqs_status.save()

        return "Success"

    except Exception as e:
        print("slimma messaging exception")
        print('%s (%s)' % (e.message, type(e)))
        # 3: ERROR
        worker_sqs_status.status = 3
        worker_sqs_status.error_text = str(e)
        worker_sqs_status.save()

        return "Message Send ERROR"
