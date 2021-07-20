import datetime as dt
import freezegun
import pytest
# import pytz

from django import urls
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
# from django.core.files.uploadedfile import SimpleUploadedFile
from django_dynamic_fixture import G
from django.utils import timezone

# import models
from apps.core.models.vendor_user import VendorUser
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.service import Service
from apps.core.models.vendor import Vendor, Preset

# import views
from apps.core.views.vendor_common.login_user_info import *

@pytest.mark.parametrize('url_name, url_kwargs', [
    ('contactchat:settings_style_index', None),
])

@pytest.mark.django_db
def test_protected_views(client, url_name, url_kwargs):
    """Verify cases views are protected from unauthenticated access"""
    url = urls.reverse(url_name, kwargs=url_kwargs)
    resp = client.get(url)
    assert resp.status_code == 302
    assert resp.url.startswith('/')

@freezegun.freeze_time('2019-01-26 7:00:00')
@pytest.mark.django_db
def test_preset(client):
    """Testing Presets in setting_style"""
    # Create a fake user
    user = G(User, username='test@test.com')
    user.set_password('my_password123')
    user.save()

    # Create a fake service
    service = G(Service, id=1, cd='00002')
    service.save()

    # Create a fake vendor
    vendor = G(Vendor, id=1,
               cd='test',
               service=1,
              )
    vendor.save()

    # Create a fake vendor branch
    vendor_branch = G(VendorBranch, id=1, vendor=1, cd='00002')
    vendor_branch.save()

    # Create a fake vendor user
    vendor_user = G(VendorUser,
                    id=1,
                    auth_user=1,
                    vendor_branch=1,
                    is_active=True,
                    is_delete=False,
                    email="test@test.com",
                    last_name='Phone')
    vendor_user.save()
    # Create a fake preset
    preset = G(Preset,
               preset_url='darkmode.css',
               preset_name='dark-mode',
               preset_css='{}',
               )
    preset.save()

    # Create a fake preset
    preset1 = G(Preset,
               preset_url='tokyo.css',
               preset_name='tokyo-mode',
               preset_css='{}',
               )
    preset1.save()

    # Log in true owner
    client.login(username='test@test.com', password='my_password123')
    settings_style_index_url = urls.reverse('contactchat:settings_style_index')

    # Go to the settings_style_index
    resp = client.get(settings_style_index_url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    select_tag = soup.find("select", {"id": "preset"})
    assert len(select_tag.find_all("option"))-1 == Preset.objects.all().count() # minus 1 for customized option
    assert resp.status_code == 200

    # Go to the settings_style_index with preset value
    resp = client.post(settings_style_index_url, {
        '--preset':'1',
    })
    # There should be a vendor with preset css
    vendor = Vendor.objects.filter(contactchat_css='{"preset_id": "1"}').first()
    # The vendor's last update  time should be set to the current time
    assert timezone.make_naive(vendor.update_dt, timezone.utc) == dt.datetime(2019, 1, 26, 7)
    assert resp.status_code == 200
