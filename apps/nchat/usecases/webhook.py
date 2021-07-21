from linebot import WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from django.http import HttpResponse

# import  models
from linebot.models import JoinEvent, MessageEvent, PostbackEvent

# import usecases
from apps.nchat.usecases.settings import get_line_token_dict_from_path
from apps.nchat.usecases.user import CreateOrUpdateEndUser
from apps.messageflow.usecases.message import process_user_bot_scenario_sequence


class ImproperUsageException(Exception):
    pass


class HandleCallback:
    """
    General use case for dealing with messaging platform callbacks.
    Currently supported platforms:
    #   LINE
    """
    def __init__(
            self,
            request,
            access_url_part,
    ):
        # Set the internal state for the operation
        self._request = request
        self._access_url_part = access_url_part

    def execute(self):
        self.valid_data()

        if self._get_platform(self._request.path):
            return self._handle_line_events()
        else:
            # TODO other services
            raise ImproperUsageException('unknown platform usage! {}'.format(self._get_platform(self._request.path)))

    def valid_data(self):
        if not self._request or not self._request.method == 'POST':
            raise ImproperUsageException('api only handles POST request')
        if not self._access_url_part:
            raise ImproperUsageException('access_url_part is a required argument')
        return True

    @staticmethod
    def _get_platform(request_path):
        path_list = request_path.split("/")
        platform = path_list[3]
        return platform

    def _handle_line_events(self):
        # assume usecase is tested
        line_token_dict = get_line_token_dict_from_path(self._request.path)
        line_events = LINEParseRequestBody(self._request).execute()
        for event in line_events:
            print("this is event.source: ", event.source.user_id)
            if event.source.user_id == "Udeadbeefdeadbeefdeadbeefdeadbeef":
                return HttpResponse()
            if isinstance(event, JoinEvent):
                end_user_info = {
                    'line_token_dict': line_token_dict,
                    'end_user_obj': CreateOrUpdateEndUser(event.source.user_id, line_token_dict).execute(),
                }
                # todo we need to pass along a bot id
                process_user_bot_scenario_sequence({
                    'payload': "GET_STARTED_PAYLOAD",
                    'text': None,
                }, end_user_info)

            elif isinstance(event, PostbackEvent):
                print('DEBUG Postback EVENT', event, PostbackEvent)
                # Save postback data
                payload = event.postback.data
                end_user = CreateOrUpdateEndUser(event.source.user_id, line_token_dict).execute()
                # end_user.set_attribute_json('line_postback_payload', payload)
                # end_user.save()
                # end_user.set_attribute_json('line_postback_payload', 'None')

                end_user_info = {
                    'line_token_dict': line_token_dict,
                    'end_user_obj': end_user,
                }

                process_user_bot_scenario_sequence({
                    'payload': payload,
                    'text': None,
                }, end_user_info)

            elif isinstance(event, MessageEvent):
                print('DEBUG Message EVENT', event, MessageEvent)
                end_user = CreateOrUpdateEndUser(event.source.user_id, line_token_dict).execute()
                # retrieve postback data if it exists and then delete it
                payload = end_user.get_attribute_json('line_postback_payload')
                end_user.set_attribute_json('line_postback_payload', 'None')
                end_user.save()

                end_user_info = {
                    'line_token_dict': line_token_dict,
                    'end_user_obj': end_user,
                }

                process_user_bot_scenario_sequence({
                    'payload': payload,
                    'text': event.message.text,
                }, end_user_info)
                print('=== debug got LINE message')
            else:
                print('not implemented!')

        # todo call individual event use cases


class LINEParseRequestBody:
    """
    Use case for parsing the body of a LINE callback request
    """

    def __init__(
            self,
            request,
    ):
        # Set the internal state for the operation
        self._request = request

    def execute(self):
        self.valid_data()

        return self._parse_body_to_events()

    def valid_data(self):
        # It is a public method to allow clients of this object to validate
        # the data even before to execute the use case.
        signature = self._request.META['HTTP_X_LINE_SIGNATURE']
        body = self._request.body

        if not signature:
            raise InvalidSignatureError

        if not body:
            raise LineBotApiError

        return True

    def _parse_body_to_events(self):
        signature = self._request.META['HTTP_X_LINE_SIGNATURE']
        body = self._request.body.decode('utf-8')
        line_token_dict = get_line_token_dict_from_path(self._request.path)
        parser = WebhookParser(line_token_dict["line_channel_secret"])
        events = parser.parse(body, signature)
        return events

