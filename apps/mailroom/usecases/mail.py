# -*- coding: utf-8 -*-

from django.utils.translation import gettext as _
from django.core.mail import get_connection, EmailMultiAlternatives
from apps.mailroom.models.message_history import MessageHistory
from django.utils.html import strip_tags
import traceback


class SendMail:

    def __init__(self, service_info, form):
        self._service_info = service_info
        self._form = form
        # print("init")

    def execute(self):
        from_email = 'no_reply@chatquest.app'
        self._form.cleaned_data['from_email'] = from_email

        ''' returns status or data '''
        self._is_valid()

        try:
            self._send_mass_html_mail(subject=self._form.cleaned_data['subject'],
                                      text_content=strip_tags(self._form.cleaned_data['message_text']),
                                      html_content=self._format_email_html(self._form.cleaned_data['subject'],
                                                                           self._form.cleaned_data['message_text']),
                                      from_email=self._form.cleaned_data['from_email'],
                                      recipient_list=self._form.cleaned_data['recipients'])
            self._save_message_history(
                status=1,
                subject=self._form.cleaned_data['subject'],
                message=self._form.cleaned_data['message_text'],
                from_email=self._form.cleaned_data['from_email'],
                recipient_list=self._form.cleaned_data['recipients']
            )
        except Exception as e:
            print("Unable to send email", e)
            print(traceback.format_exc())
            # this adds a sent message to message history if it is unsuccessful
            self._save_message_history(
                status=0,
                subject=self._form.cleaned_data['subject'],
                message=self._form.cleaned_data['message_text'],
                from_email=self._form.cleaned_data['from_email'],
                recipient_list=self._form.cleaned_data['recipients']
            )
        return True

    def _is_valid(self):
        if 'owner_id' not in self._service_info or 'app_id' not in self._service_info:
            raise Exception("service_info is incomplete.")

        if 'subject' not in self._form.cleaned_data \
                or 'recipients' not in self._form.cleaned_data \
                or 'message_text' not in self._form.cleaned_data \
                or 'from_email' not in self._form.cleaned_data:
            raise Exception("Message parameters are incomplete.")

        if type(self._form.cleaned_data['recipients']) != list:
            raise Exception("Recipients is not of type 'list.'")

        for recipient in self._form.cleaned_data['recipients']:
            if type(recipient) != str:
                raise Exception("At least one recipient is not of type 'str.'")

        if len(self._form.cleaned_data['recipients']) == 0:
            raise Exception("There are no message recipients.")

        if type(self._form.cleaned_data['subject']) != str:
            raise Exception("Subject is not of type 'str.'")

        if len(self._form.cleaned_data['subject']) == 0:
            raise Exception("The message subject has no text.")

        if len(self._form.cleaned_data['subject']) > 255:
            raise Exception("The message subject is too long.")

        if len(self._form.cleaned_data['subject']) == 0:
            raise Exception("The message body has no text.")

        if type(self._form.cleaned_data['message_text']) != str:
            raise Exception("The message body is not of type 'str.'")

        if len(self._form.cleaned_data['message_text']) == 0:
            raise Exception("The message body has no text.")

        if len(self._form.cleaned_data['message_text']) > 8000:
            raise Exception("The message body is too long.")

        if type(self._form.cleaned_data['from_email']) != str:
            raise Exception("The sender address is not of type 'str.'")

        if len(self._form.cleaned_data['from_email']) == 0:
            raise Exception("The message has no sender address.")

        if len(self._form.cleaned_data['from_email']) > 254:
            raise Exception("The message sender address is too long.")

        return True

    def _format_email_html(self, subject, message):
        return '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" ' \
                '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">' \
                '<html xmlns="http://www.w3.org/1999/xhtml">' \
                '<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />' \
                f'<title>{subject}</title>' \
                '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>' \
                '</head>' \
                f'<body>{message}</body>' \
                '</html>'

    def _send_mass_html_mail(self, subject, text_content, html_content, from_email, recipient_list, user=None,
                             password=None):
        """
        Given a datatuple of (subject, text_content, html_content, from_email,
        recipient_list), sends each message to each recipient list. Returns the
        number of emails sent.

        If from_email is None, the DEFAULT_FROM_EMAIL setting is used.
        If auth_user and auth_password are set, they're used to log in.
        If auth_user is None, the EMAIL_HOST_USER setting is used.
        If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.

        """
        connection = get_connection(username=user, password=password, fail_silently=False)
        messages = []
        for recipient in recipient_list:
            message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=from_email,
                                             to=[recipient], connection=connection)
            message.attach_alternative(html_content, 'text/html')
            messages.append(message)
        return connection.send_messages(messages)

    def _save_message_history(self, **kwargs):
        message_history = MessageHistory(owner_id=self._service_info["owner_id"],
                                         app_id=self._service_info["app_id"],
                                         subject=kwargs["subject"],
                                         recipients=kwargs["recipient_list"],
                                         message_text=kwargs["message"],
                                         status=kwargs['status']
                                         )
        message_history.save()
