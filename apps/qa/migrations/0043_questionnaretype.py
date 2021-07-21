
from django.db import migrations, models


def generate_default_rows(apps, schema_editor):
    CouponType = apps.get_model('qa', 'CouponType')
    def_coupon_type = CouponType()
    def_coupon_type.name = 'questionnaire'
    def_coupon_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0042_multi_option_type'),
    ]

    operations = [
        migrations.RunPython(generate_default_rows),
    ]
