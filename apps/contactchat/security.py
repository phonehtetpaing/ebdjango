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

import base64
import hashlib
import hmac
from .utils import safe_compare_digest

if hasattr(hmac, "compare_digest"):
    def compare_digest(val1, val2):
        """compare_digest function.

        If hmac module has compare_digest function, use it.

        :param val1: string or bytes for compare
        :type val1: str | bytes
        :param val2: string or bytes for compare
        :type val2: str | bytes
        :rtype: bool
        :return: result
        """
        return hmac.compare_digest(val1, val2)
else:
    def compare_digest(val1, val2):
        """compare_digest function.
        If hmac module has compare_digest function, use it.
        Or not, use contactchat.utils.safe_compare_digest.
        :param val1: string or bytes for compare
        :type val1: str | bytes
        :param val2: string or bytes for compare
        :type val2: str | bytes
        :rtype: bool
        :return: result
        """
        return safe_compare_digest(val1, val2)


class SignatureValidator(object):
    """Signature validator."""

    def __init__(self, channel_secret):
        """__init__ method.

        :param str channel_secret: Channel secret (as text)
        """
        self.channel_secret = channel_secret.encode('utf-8')

    def validate(self, body, signature):
        """Check signature.

        :param str body: Request body (as text)
        :param str signature: X-ContactChat-Signature value (as text)
        :rtype: bool
        :return: result
        """
        print('debug signature validate body: ', body)
        gen_signature = self.gen_signature(body)

        return compare_digest(
            signature.encode('utf-8'), gen_signature.encode('utf-8')
        )

    def gen_signature(self, body):
        """ Generate new signature
        :param str body: Request body (as text)
        :rtype str
        :return: signature
        """
        return hmac.new(
            self.channel_secret,
            body.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
