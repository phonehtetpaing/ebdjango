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

import logging
import re
import sys

LOGGER = logging.getLogger('contactchat')

PY3 = sys.version_info[0] == 3


def to_snake_case(text):
    """Convert to snake case.

    :param str text:
    :rtype: str
    :return:
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camel_case(text):
    """Convert to camel case.

    :param str text:
    :rtype: str
    :return:
    """
    split = text.split('_')
    return split[0] + "".join(x.title() for x in split[1:])


def safe_compare_digest(val1, val2):
    """safe_compare_digest method.

    :param val1: string or bytes for compare
    :type val1: str | bytes
    :param val2: string or bytes for compare
    :type val2: str | bytes
    """
    if len(val1) != len(val2):
        return False

    result = 0
    if PY3 and isinstance(val1, bytes) and isinstance(val2, bytes):
        for i, j in zip(val1, val2):
            result |= i ^ j
    else:
        for i, j in zip(val1, val2):
            result |= (ord(i) ^ ord(j))

    return result == 0
