# -*- coding: utf-8 -*-
from django.utils.translation import gettext as _
from django.template.loader import get_template, TemplateDoesNotExist, render_to_string

from apps.mailroom.usecases.user import UserUnauthorizedError


class RetrieveTemplates:
    """
    Use case for retrieving and validating a template for use with mailroom views.
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
        base_path = '{0}/mailroom'.format(app_id)
        # todo can we pass along default using url meta data?
        # if we override base
        if self._base_template_name:
            base_template = self._get_template(app_id+'/base', self._base_template_name)
        else:
            base_template = self._get_template('mailroom', 'base/blank')

        # if we overide main template
        if self._template_name:
            template = self._get_template(base_path, self._template_name)
        else:
            template = self._get_template('mailroom', self._view_name)

        return {
            'base_template': base_template,
            'template': template,
        }