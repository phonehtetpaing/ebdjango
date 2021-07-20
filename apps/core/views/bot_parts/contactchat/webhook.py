# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass
import base64
import hashlib
import hmac
import inspect
import json

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


# Error types

class BaseError(with_metaclass(ABCMeta, Exception)):
    """Base Exception class."""

    def __init__(self, message='-'):
        """__init__ method.

        :param str message: Human readable message
        """
        self.message = message

    def __repr__(self):
        """repr.

        :return:
        """
        return str(self)

    def __str__(self):
        """str.

        :rtype: str
        :return:
        """
        return '<{0} [{1}]>'.format(
            self.__class__.__name__, self.message)


class InvalidSignatureError(BaseError):
    """When Webhook signature does NOT match, this error will be raised."""

    def __init__(self, message='-'):
        """__init__ method.

        :param str message: Human readable message
        """
        super(InvalidSignatureError, self).__init__(message)


# Validators


class SignatureValidator(object):
    """Signature validator.
    """

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
        gen_signature = hmac.new(
            self.channel_secret,
            body.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        return compare_digest(
            signature, gen_signature
        )


# Parsers


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