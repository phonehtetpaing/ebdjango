import pytest
from django_mock_queries.query import MockSet

from apps.core.models.vendor import Preset

class TestPreset:
    @pytest.fixture()
    def mocked_models(self, mocker):
      preset = Preset(
          id=1,
          preset_url='dark_mode_chat.css',
          preset_name='dark_mode',
          preset_css='{}'
      ) 
      preset_qs_mock = MockSet(preset, model=Preset)
      mocker.patch.object(
          Preset.objects,
          'get_queryset',
          return_value=preset_qs_mock
      )

    def test_url_max_length(self, mocker, mocked_models):
        preset = Preset.objects.filter(pk=1).first()
        max_length = preset._meta.get_field('preset_url').max_length
        assert max_length == 1024

    def test_name_max_length(self, mocker, mocked_models):
        preset = Preset.objects.filter(pk=1).first()
        max_length = preset._meta.get_field('preset_name').max_length
        assert max_length == 1024

    def test_preset_css_max_length(self, mocker, mocked_models):
        preset = Preset.objects.filter(pk=1).first()
        max_length = preset._meta.get_field('preset_css').max_length
        assert max_length == 1024

    def test___str__is_last_name_space_first_name(self, mocker, mocked_models):
        preset = Preset.objects.filter(pk=1).first()
        assert str(preset) == 'dark_mode'
