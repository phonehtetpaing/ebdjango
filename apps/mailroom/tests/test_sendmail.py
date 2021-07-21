import pytest
import string
import random
from django.contrib.auth.models import AnonymousUser

# import usecase
from apps.mailroom.usecases.mail import SendMail


service_info = {'owner_id': 'test', 'app_id': 'test'}


class EmailObject:
    pass


EmailObject.cleaned_data = {'recipients': ['chaz303@yahoo.com'], 'subject': 'ghost', 'message_text': '<p>ghost</p>',
                            'from_email': 'no_reply@google.com'}

use_case = SendMail(service_info=service_info, form=EmailObject)


def message_history_m(self, message, status):
    return {"status": status, "message": message}


def send_mass_mail_m(message_list):
    return message_list


@pytest.fixture
def mock_SendMail(mocker):
    mocker.patch.object(SendMail, '_save_message_history', side_effect=message_history_m('self', message=EmailObject, status=1))
    mocker.patch.object(SendMail, '_send_mass_html_mail', side_effect=send_mass_mail_m(EmailObject))


class TestValidData:
    # Test the _is_valid function used by the execute method on SendMail use case

    # test recipients field

    def test_with_no_recipients_key(self, mock_SendMail):
        del EmailObject.cleaned_data['recipients']
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_recipients_not_as_list(self, mock_SendMail):
        EmailObject.cleaned_data['recipients'] = 'fake@email.com'
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_recipients_not_as_strings_within_list(self, mock_SendMail):
        EmailObject.cleaned_data['recipients'] = ['fake@email.com', 3]
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_no_recipients(self, mock_SendMail):
        EmailObject.cleaned_data['recipients'] = ""
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_one_recipient(self, mock_SendMail):
        EmailObject.cleaned_data['recipients'] = ['fake@email.com']
        result = use_case._is_valid()
        assert result == True


    def test_with_two_recipients(self, mock_SendMail):
        EmailObject.cleaned_data['recipients'] = ['fake@email.com', 'another@fake.com']
        result = use_case._is_valid()
        assert result == True

    # test subject field

    def test_with_no_subject_key(self, mock_SendMail):
        del EmailObject.cleaned_data['subject']
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_subject_not_as_string(self, mock_SendMail):
        EmailObject.cleaned_data['subject'] = ["subject"]
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_no_subject(self, mock_SendMail):
        EmailObject.cleaned_data['subject'] = ""
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_too_long_subject(self, mock_SendMail):
        random_string_length = 256;
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random_string_length))
        EmailObject.cleaned_data['subject'] = random_string
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_good_subject(self, mock_SendMail):
        EmailObject.cleaned_data['subject'] = 'Another Boring email'
        result = use_case._is_valid()
        assert result == True

    # test message text field

    def test_with_no_message_text_key(self, mock_SendMail):
        del EmailObject.cleaned_data['message_text']
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_message_text_not_as_string(self, mock_SendMail):
        EmailObject.cleaned_data['message_text'] = ["Message body."]
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_no_message_text(self, mock_SendMail):
        EmailObject.cleaned_data['message_text'] = ""
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_too_long_message_text(self, mock_SendMail):
        random_string_length = 8001;
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random_string_length))
        EmailObject.cleaned_data['message_text'] = random_string
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_good_message_text(self, mock_SendMail):
        EmailObject.cleaned_data['message_text'] = 'Have you heard about exciting opportunities in DPRK real estate?'
        result = use_case._is_valid()
        assert result == True

    # test message from_email field

    def test_with_no_from_email_key(self, mock_SendMail):
        del EmailObject.cleaned_data['from_email']
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_from_email_not_as_string(self, mock_SendMail):
        EmailObject.cleaned_data['from_email'] = ["fake@email.com"]
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_no_from_email(self, mock_SendMail):
        EmailObject.cleaned_data['from_email'] = ""
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_too_long_from_email(self, mock_SendMail):
        random_string_length = 255;
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random_string_length))
        EmailObject.cleaned_data['from_email'] = random_string
        with pytest.raises(Exception):
            assert use_case._is_valid()

    def test_with_good_from_email(self, mock_SendMail):
        EmailObject.cleaned_data['from_email'] = 'no_reply@google.com'
        result = use_case._is_valid()
        assert result == True

# These tests were written for a function that was refactored and rolled into _send_mass_html_mail(),
# if mail message formatting is a concern, a formatting function can be made and use these tests
#
# class TestCreateMessageTupleList:
#     # Test the _is_valid function used by the execute method on SendMail use case
#
#     def test_with_one_recipient_type(self, mock_SendMail):
#         EmailObject.cleaned_data['recipients'] = ['fake@email.com']
#         assert type(use_case._create_message_tuple_list(subject=EmailObject.cleaned_data['subject'],
#                                                         message=EmailObject.cleaned_data['message_text'],
#                                                         from_email=EmailObject.cleaned_data['from_email'],
#                                                         recipient_list=EmailObject.cleaned_data['recipients'])) == list
#
#     def test_with_one_recipient_length(self, mock_SendMail):
#         EmailObject.cleaned_data['recipients'] = ['fake@email.com']
#         assert len(use_case._create_message_tuple_list(subject=EmailObject.cleaned_data['subject'],
#                                                        message=EmailObject.cleaned_data['message_text'],
#                                                        from_email=EmailObject.cleaned_data['from_email'],
#                                                        recipient_list=EmailObject.cleaned_data['recipients'])) == 1
#
#     def test_with_two_recipients_type(self, mock_SendMail):
#         EmailObject.cleaned_data['recipients'] = ['fake@email.com', 'another@fake.com']
#         assert type(use_case._create_message_tuple_list(subject=EmailObject.cleaned_data['subject'],
#                                                         message=EmailObject.cleaned_data['message_text'],
#                                                         from_email=EmailObject.cleaned_data['from_email'],
#                                                         recipient_list=EmailObject.cleaned_data['recipients'])) == list
#
#     def test_with_two_recipients_length(self, mock_SendMail):
#         EmailObject.cleaned_data['recipients'] = ['fake@email.com', 'another@fake.com']
#         assert len(use_case._create_message_tuple_list(subject=EmailObject.cleaned_data['subject'],
#                                                        message=EmailObject.cleaned_data['message_text'],
#                                                        from_email=EmailObject.cleaned_data['from_email'],
#                                                        recipient_list=EmailObject.cleaned_data['recipients'])) == 2
#
