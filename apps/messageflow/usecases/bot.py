# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _

# import models
from apps.messageflow.models.bot import Bot, BotScenario, Scenario

# import forms
from apps.messageflow.forms.bot import BotForm, ScenarioFormSet


class UserUnauthorizedError(Exception):
    pass


class BotNotFoundError(Exception):
    pass


class EditBot:
    """
    Use case for editing bot properties and operations.
    """

    def __init__(
            self,
            service_info,
            bot_id,
    ):
        # Set the internal state for the operation
        self._service_info = service_info
        self._bot = bot_id

    def execute(self):
        # TODO write actual use case
        return self.valid_data()

    def valid_data(self):
        # It is a public method to allow clients of this object to validate
        # the data even before to execute the use case.
        bot = Bot.objects.filtter(id=self._bot_id, owner_id=self._service_info['owner_id'], app_id=self._service_info['app_id']).first()
        if not bot:
            error_msg = (
                '{} Unable to perform this operation.'
            ).format(self._service_info['owner_id'])

            raise BotNotFoundError(_(error_msg))

        return True

