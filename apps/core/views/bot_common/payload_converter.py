# -*- coding: utf-8 -*-
import json
from datetime import datetime
import time

# import models
from apps.core.models.payload import Payload


def get_payload_value(vendor_branch, value_alt):

    payload = Payload.objects.filter(vendor_branch=vendor_branch, value_alt=value_alt).first()
    if payload:
        return payload.value

    else:
        return None
