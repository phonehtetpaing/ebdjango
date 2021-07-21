# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.template.loader import get_template, TemplateDoesNotExist, render_to_string

from apps.messageflow.forms.scenario import MessageFormSet
from apps.messageflow.models import MessageBlock, MessageType
from apps.messageflow.usecases.user import UserUnauthorizedError
from apps.nchat.models.file import File


class MessageTypeDoesNotExist(Exception):
    pass


class RetrieveTemplates:
    """
    Use case for retrieving and validating a template for use with messageflow views.
    If the template is not found an exception is raised.
    """

    def __init__(
            self,
            service_info,
            view_name,
            base_template_name=None,
            template_name=None,
    ):
        # Set the internal state for the operation
        self._service_info = service_info
        self._view_name = view_name
        self._base_template_name = base_template_name
        self._template_name = template_name

    def execute(self):
        self.valid_data()
        return self._get_template_dict()

    def valid_data(self):
        # It is a public method to allow clients of this object to validate
        # the data even before to execute the use case.
        app_id = self._service_info['app_id']
        if not app_id:
            error_msg = (
                'The authenticated user, {}, is not registered or is not authorized to perform this operation.'
            ).format('')

            raise UserUnauthorizedError(_(error_msg))

        # verify that the view actually exists
        if not self._view_name or self._view_name == '':
            raise TemplateDoesNotExist

        # verify the template can be found
        self._get_template_dict()

        return True

    def _get_template(self, service_name, template_name):
        """ Verifies a template exists and then returns the path if it does or raised a TemplateDoesNotExist """
        print('debug service name at template', service_name)
        template_path = '{0}/{1}.html'.format(service_name, template_name)
        get_template(template_path)
        return template_path

    def _get_template_dict(self):
        """ Returns a dict containing the paths for base_template and template """
        app_id = self._service_info['app_id']
        print('getting service info app id', app_id)
        base_path = '{0}/messageflow'.format(app_id)
        # todo can we pass along default using url meta data?
        # if we override base
        if self._base_template_name:
            base_template = self._get_template(app_id+'/base', self._base_template_name)
        else:
            base_template = self._get_template('messageflow', 'base/blank')

        # if we overide main template
        if self._template_name:
            template = self._get_template(base_path, self._template_name)
        else:
            template = self._get_template('messageflow', self._view_name)

        return {
            'base_template': base_template,
            'template': template,
        }


class RetrieveMessageTemplate:
    def __init__(
        self,
        service_info,
        set_id,
        block_id,
        message_type,
        display_order,
    ):
        # Set the internal state for the operation
        self._service_info = service_info
        self._set_id = set_id
        self._block_id = block_id
        self._message_type = message_type
        self._display_order = display_order

    def execute(self):
        self.valid_data()
        return self._get_json_template(self._set_id)

    def valid_data(self):
        # It is a public method to allow clients of this object to validate
        # the data even before to execute the use case.

        # verify set_Id is passed
        if not self._set_id:
            error_msg = (
                'The value for set_id, {}, is not valid or malformed.'
            ).format(self._set_id)

            raise KeyError(_(error_msg))
        self._set_id = int(self._set_id)

        # verify scenario id is passed verify that it exists
        if not self._block_id:
            error_msg = (
                'The value for block_id, {}, is not valid or malformed.'
            ).format(self._block_id)

            raise KeyError(_(error_msg))
        self._block_id = int(self._block_id)

        message_block = MessageBlock.objects.filter(id=self._block_id).first()
        # if not message_block or not message_block.scenario.owner_id == self._service_info['owner_id'] or not message_block.scenario.app_id == self._service_info['app_id']:
        #     error_msg = (
        #         'The value for block_id, {}, is not valid or malformed.'
        #     ).format(self._block_id)
        #
        #     raise KeyError(_(error_msg))

        # verify that type exists
        if isinstance(self._message_type, str):
            message_type = MessageType.objects.filter(name=self._message_type).first()

        if isinstance(self._message_type, int) or (not message_type and not isinstance(self._message_type, MessageType)):
            message_type = int(self._message_type)
            message_type = MessageType.objects.filter(id=self._message_type).first()

        if not isinstance(message_type, MessageType):
            error_msg = (
                'The message type, {}, is not registered or malformed.'
            ).format(self._message_type)

            raise MessageTypeDoesNotExist(_(error_msg))
        else:
            self._message_type = message_type

        # verify display_order argument is passed verify that it is valid
        if self._display_order:
            self._display_order = int(self._display_order)

        if self._display_order is None or self._display_order < 0:
            error_msg = (
                'The value for display_order, {}, is not valid or malformed.'
            ).format(self._display_order)
            raise KeyError(_(error_msg))

        return True

    def _get_empty_formset(self):
        message_block = MessageBlock.objects.filter(id=self._block_id).first()
        message_type = self._message_type
        message_formset = MessageFormSet(instance=message_block, initial={'type': message_type})
        # hack workaround for the shortcomings of empty_form but these properties are still public so should be safe
        formset = message_formset.form(
            auto_id=message_formset.auto_id,
            prefix=message_formset.add_prefix(self._set_id),
            empty_permitted=False,
            use_required_attribute=False,
            **message_formset.get_form_kwargs(None)
        )
        message_formset.add_fields(formset, None)
        # Setting the initial value!
        formset.initial['type'] = message_type

        return formset

    def _get_json_template(self, set_id):
        context = {
            "message": self._get_empty_formset(),
            "message_counter": set_id,
            "message_blocks": self._get_message_blocks(),
        }
        if self._message_type.name == 'image' or self._message_type.name == 'file':
            context.update({"files": self._get_files()})

        return render_to_string('messageflow/messages/{}_message.html'.format(self._message_type.name), context)

    def _get_message_blocks(self):
        message_block = MessageBlock.objects.filter(id=self._block_id).first()
        return MessageBlock.objects.filter(scenario=message_block.scenario).all()

    # todo seperate this from nchat?
    def _get_files(self):
        files = File.objects.filter(app_id=self._service_info['app_id'], owner_id=self._service_info['owner_id']).all()
        return files
