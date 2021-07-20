# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import json
import requests
from .security import SignatureValidator


class ContactChatApi(object):

    DEFAULT_API_ENDPOINT = ''
    DEFAULT_TIMEOUT = 5

    def __init__(self, channel_access_token, channel_secret, endpoint=DEFAULT_API_ENDPOINT, timeout=DEFAULT_TIMEOUT):
        """__init__ method.

                :param str channel_access_token: Your channel access token
                :param str endpoint: (optional) Defaults
                :param timeout: (optional) How long to wait for the server
                    to send data before giving up, as a float,
                    or a (connect timeout, read timeout) float tuple.
                    Default is DEFAULT_TIMEOUT
                :type timeout: float | tuple(float, float)
                """
        self.endpoint = endpoint
        self.channel_access_token = channel_access_token
        self.channel_secret = channel_secret
        self.signature_validator = SignatureValidator(channel_secret)
        self.timeout = timeout
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'smartby_api'
        }

    def push_message(self, to, message, timeout=None):
        """push message API.

        Send messages to users, groups, and rooms at any time.

        :param str to: ID of the receiver
        :param message: Message.
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
        :type timeout: float | tuple(float, float)
        """

        msg_data = {
            "recipient": {"id": to},
            "message": message
        }
        print('debug push_message contactchat api', msg_data)
        return self._post(
            'v1/bot/', data=json.dumps(msg_data, ensure_ascii=False, separators=(",", ":")), timeout=timeout
        )

    def _post(self, url, data=None, timeout=None):
        """POST request.

        :param str url: Request url
        :param data: (optional) Dictionary, bytes, or file-like object to send in the body
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`RequestsHttpResponse`
        :return: RequestsHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        print('debug _post contactchat api dumps:', data)
        # update headers with signature
        headers = {'X-CONTACTCHAT-SIGNATURE': self.signature_validator.gen_signature(data)}
        headers.update(self.headers)

        post_message_url = self.endpoint + url + self.channel_access_token + '/'
        print('debug _post contactchat api type ', type(data))
        print('debug _post contactchat api ', post_message_url, headers, data)
        response = requests.post(
            post_message_url, headers=headers, data=data.encode('utf-8'), timeout=timeout
        )

        return response
