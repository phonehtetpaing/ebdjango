# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand
from django.core.mail import send_mail


# extends BaseCommand
class Command(BaseCommand):
    help = 'test'
    # setting.DEBUG = False
    def handle(self, *args, **options):

        try:
            subject = 'test mail'
            message = 'テストです。'
            from_email = 'no_reply@chatquest.app'
            recipient_list = ['m.bruning@peacefactory.co.jp']

            send_mail(subject, message, from_email, recipient_list)

        except KeyError:
            print("error....")
