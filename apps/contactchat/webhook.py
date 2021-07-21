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

from __future__ import unicode_literals
from .exceptions import InvalidSignatureError
from .security import SignatureValidator

import json


class CCWebhookParser(object):
    """Webhook Parser."""

    def __init__(self, channel_secret):
        """__init__ method.

        :param str channel_secret: Channel secret (as text)
        """
        self.signature_validator = SignatureValidator(channel_secret)

    def parse(self, body, signature):
        """Parse webhook request body as text.

        :param str body: Webhook request body (as text)
        :param str signature: X-ContactChat-Signature value (as text)
        :return:
        """
        if not self.signature_validator.validate(body, signature):
            raise InvalidSignatureError(
                'Invalid signature. signature=' + signature)

        return json.loads(body)
