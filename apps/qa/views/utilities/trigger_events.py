from datetime import datetime as dt, timedelta

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# import models
from apps.qa.models.ma_trigger_type import MaTriggerType
from apps.qa.models.coupon import Coupon
from apps.qa.models.coupon_claim import CouponClaim
from apps.qa.models.questionnaire import Questionnaire
from apps.core.models.end_user import EndUser

# import views
from django.core.mail import send_mail


def send_after_joining_type_message(ma_trigger):

    # get specifics for this trigger
    now = dt.now()
    hours = ma_trigger.hours
    days = ma_trigger.days

    # oldest possible registration date
    old_time_threshold = now - timedelta(days, hours)
    # newest possible registration date
    new_time_threshold = now - timedelta(days, (hours-1))

    # get all users that are applicable for this event
    end_users = EndUser.objects.filter(vendor_branch=ma_trigger.message.vendor_branch, regist_dt__lt=new_time_threshold,
                                       regist_dt__gt=old_time_threshold, is_delete=False).all()

    recipient_list = []
    # loop over each user and collect their email, then add it to the email list
    for end_user in end_users:
        if end_user.email:
            try:
                validate_email(end_user.email)
            except ValidationError as e:
                print('invalid email encountered', end_user.email)
            else:
                recipient_list.append(end_user.email)

    # now send mail message to all found recipients
    subject = ma_trigger.message.subject
    message = ma_trigger.message
    from_email = 'no_reply@chatquest.app'

    try:
        send_mail(subject, message, html_message=message, from_email=from_email, recipient_list=recipient_list)
    except KeyError:
        print("error....")

# todo create a completed field? (or use logic but that is more expensive...)
def create_after_completing_questionnaire_message(end_user):
    """
    This should be called upon the completion of a questionnaire by an end_user.
    The function looks for ALL MessageTriggers that are of the the type "after completing questionnaire" and
    uses the trigger information to calculate when the associated message should be sent to the user.
    After determining when the messages should be sent they are added to a message queue to be sent at their
    determined send date times.
    :param end_user:
    """
    trigger_type = MaTriggerType.objects.filter(name='after taking survey').first()
    # # get all messages for this vendor
    # all_messages = Message.objects.filter(vendor_branch=end_user.vendor_branch)
    # # get all currently registered triggers of specified type
    # all_triggers = MaTrigger.objects.filter(trigger_type=trigger_type, message__in=all_messages)
    #
    # for trigger in all_triggers:
    #     # calculate send date time
    #     days = trigger.days
    #     hours = trigger.hours
    #     send_dt = dt.now() + timedelta(days, hours)
    #
    #     # add new message to the message queue so it can be collected later
    #     new_queued_message = MessageQueue(end_user=end_user, message=trigger.message, send_dt=send_dt)
    #     new_queued_message.save()


def send_after_using_coupon_message(ma_trigger):
    # get specifics for this trigger
    now = dt.now()
    hours = ma_trigger.hours
    days = ma_trigger.days

    # oldest possible claim date
    old_time_threshold = now - timedelta(days, hours)
    # newest possible claim date
    new_time_threshold = now - timedelta(days, (hours - 1))

    # get all users that are applicable for this event
    end_users = EndUser.objects.filter(vendor_branch=ma_trigger.message.vendor_branch, is_delete=False).all()

    claimed_coupons = CouponClaim.objects.filter(end_user__in=end_users, regist_dt__lt=new_time_threshold, regist_dt__gt=old_time_threshold, is_delete=False).all()
    recipient_list = []
    # loop over each user and collect their email, then add it to the email list
    for claim in claimed_coupons:
        if claim.end_user.email:
            try:
                validate_email(claim.end_user.email)
            except ValidationError as e:
                print('invalid email encountered', claim.end_user.email)
            else:
                recipient_list.append(claim.end_user.email)

    # now send mail message to all found recipients
    subject = ma_trigger.message.subject
    message = ma_trigger.message
    from_email = 'no_reply@chatquest.app'

    try:
        send_mail(subject, message, html_message=message, from_email=from_email, recipient_list=recipient_list)
    except KeyError:
        print("error....")


def send_after_no_activity_message(ma_trigger):
    # get specifics for this trigger
    now = dt.now()
    hours = ma_trigger.hours
    days = ma_trigger.days

    # oldest possible claim date
    old_time_threshold = now - timedelta(days, hours)
    # newest possible claim date
    new_time_threshold = now - timedelta(days, (hours - 1))

    # get all users that are applicable for this event
    end_users = EndUser.objects.filter(vendor_branch=ma_trigger.message.vendor_branch, update_dt__lt=new_time_threshold, update_dt__gt=old_time_threshold, is_delete=False).all()

    recipient_list = []
    # loop over each user and collect their email, then add it to the email list
    for end_user in end_users:
        if end_user.email:
            try:
                validate_email(end_user.email)
            except ValidationError as e:
                print('invalid email encountered', end_user.email)
            else:
                recipient_list.append(end_user.email)

    # now send mail message to all found recipients
    subject = ma_trigger.message.subject
    message = ma_trigger.message
    from_email = 'no_reply@chatquest.app'

    try:
        send_mail(subject, message, html_message=message, from_email=from_email, recipient_list=recipient_list)
    except KeyError:
        print("error....")


def send_after_new_survey_goes_live_message(ma_trigger):
    # get specifics for this trigger
    now = dt.now()
    hours = ma_trigger.hours
    days = ma_trigger.days

    # oldest possible claim date
    old_time_threshold = now - timedelta(days, hours)
    # newest possible claim date
    new_time_threshold = now - timedelta(days, (hours - 1))

    # get all questionnaires that are about to go live
    questionnaires = Questionnaire.objects.filter(vendor_branch=ma_trigger.message.vendor_branch,
                                                  valid_from__lt=new_time_threshold, valid_from__gt=old_time_threshold,
                                                  is_delete=False).all()

    # get all users that are applicable for this event
    end_users = EndUser.objects.filter(vendor_branch=ma_trigger.message.vendor_branch, is_delete=False).all()

    recipient_list = []
    # loop over each user and collect their email, then add it to the email list
    for end_user in end_users:
        if end_user.email:
            try:
                validate_email(end_user.email)
            except ValidationError as e:
                print('invalid email encountered', end_user.email)
            else:
                recipient_list.append(end_user.email)

    # now send mail message to all found recipients
    subject = ma_trigger.message.subject
    message = ma_trigger.message
    from_email = 'no_reply@chatquest.app'

    try:
        for questionnaire in questionnaires:
            send_mail(subject, message, html_message=message, from_email=from_email, recipient_list=recipient_list)
    except KeyError:
        print("error....")


def create_after_new_coupon_goes_live_message(ma_trigger):
    # get specifics for this trigger
    now = dt.now()
    hours = ma_trigger.hours
    days = ma_trigger.days

    # oldest possible claim date
    old_time_threshold = now - timedelta(days, hours)
    # newest possible claim date
    new_time_threshold = now - timedelta(days, (hours - 1))

    # get all questionnaires that are about to go live
    coupons = Coupon.objects.filter(vendor_branch=ma_trigger.message.vendor_branch, valid_from__lt=new_time_threshold,
                                    valid_from__gt=old_time_threshold, is_delete=False).all()

    # get all users that are applicable for this event
    end_users = EndUser.objects.filter(vendor_branch=ma_trigger.message.vendor_branch, is_delete=False).all()

    recipient_list = []
    # loop over each user and collect their email, then add it to the email list
    for end_user in end_users:
        if end_user.email:
            try:
                validate_email(end_user.email)
            except ValidationError as e:
                print('invalid email encountered', end_user.email)
            else:
                recipient_list.append(end_user.email)

    # now send mail message to all found recipients
    subject = ma_trigger.message.subject
    message = ma_trigger.message
    from_email = 'no_reply@chatquest.app'

    try:
        for coupon in coupons:
            send_mail(subject, message, html_message=message, from_email=from_email, recipient_list=recipient_list)
    except KeyError:
        print("error....")


def send_before_coupon_expires_message(ma_trigger):
    # get specifics for this trigger
    now = dt.now()
    hours = ma_trigger.hours
    days = ma_trigger.days

    # oldest possible claim date
    old_time_threshold = now - timedelta(days, hours)
    # newest possible claim date
    new_time_threshold = now - timedelta(days, (hours - 1))

    # get all questionnaires that are about to go live
    coupons = Coupon.objects.filter(vendor_branch=ma_trigger.message.vendor_branch, valid_until__lt=new_time_threshold,
                                    valid_until__gt=old_time_threshold, is_delete=False).all()

    # get all users that are applicable for this event
    end_users = EndUser.objects.filter(vendor_branch=ma_trigger.message.vendor_branch, is_delete=False).all()

    recipient_list = []
    # loop over each user and collect their email, then add it to the email list
    for end_user in end_users:
        if end_user.email:
            try:
                validate_email(end_user.email)
            except ValidationError as e:
                print('invalid email encountered', end_user.email)
            else:
                recipient_list.append(end_user.email)

    # now send mail message to all found recipients
    subject = ma_trigger.message.subject
    message = ma_trigger.message
    from_email = 'no_reply@chatquest.app'

    try:
        for coupon in coupons:
            send_mail(subject, message, html_message=message, from_email=from_email, recipient_list=recipient_list)
    except KeyError:
        print("error....")


def send_before_survey_expires_message(ma_trigger):
    # get specifics for this trigger
    now = dt.now()
    hours = ma_trigger.hours
    days = ma_trigger.days

    # oldest possible claim date
    old_time_threshold = now - timedelta(days, hours)
    # newest possible claim date
    new_time_threshold = now - timedelta(days, (hours - 1))

    # get all questionnaires that are about to go live
    questionnaires = Questionnaire.objects.filter(vendor_branch=ma_trigger.message.vendor_branch
                                                  , valid_until__lt=new_time_threshold,
                                                  valid_until__gt=old_time_threshold, is_delete=False).all()

    # get all users that are applicable for this event
    end_users = EndUser.objects.filter(vendor_branch=ma_trigger.message.vendor_branch, is_delete=False).all()

    recipient_list = []
    # loop over each user and collect their email, then add it to the email list
    for end_user in end_users:
        if end_user.email:
            try:
                validate_email(end_user.email)
            except ValidationError as e:
                print('invalid email encountered', end_user.email)
            else:
                recipient_list.append(end_user.email)

    # now send mail message to all found recipients
    subject = ma_trigger.message.subject
    message = ma_trigger.message
    from_email = 'no_reply@chatquest.app'

    try:
        for questionnaire in questionnaires:
            send_mail(subject, message, html_message=message, from_email=from_email, recipient_list=recipient_list)
    except KeyError:
        print("error....")


def send_before_birthday_message(ma_trigger):
    # get specifics for this trigger
    now = dt.now()

    hours = ma_trigger.hours
    days = ma_trigger.days

    # oldest possible claim date
    old_time_threshold = now - timedelta(days, hours)
    # newest possible claim date
    new_time_threshold = now - timedelta(days, (hours - 1))

    # get all users that are applicable for this event
    end_users = EndUser.objects.filter(vendor_branch=ma_trigger.message.vendor_branch,
                                       birth_date__lt=old_time_threshold, birth_date__gt=new_time_threshold,
                                       is_delete=False).all()

    recipient_list = []
    # loop over each user and collect their email, then add it to the email list
    for end_user in end_users:
        if end_user.email:
            try:
                validate_email(end_user.email)
            except ValidationError as e:
                print('invalid email encountered', end_user.email)
            else:
                recipient_list.append(end_user.email)

    # now send mail message to all found recipients
    subject = ma_trigger.message.subject
    message = ma_trigger.message
    from_email = 'no_reply@chatquest.app'

    try:
        send_mail(subject, message, html_message=message, from_email=from_email, recipient_list=recipient_list)
    except KeyError:
        print("error....")

