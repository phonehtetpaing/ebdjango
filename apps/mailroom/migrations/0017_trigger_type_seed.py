# Generated by Django 2.0.5 on 2019-10-10 02:11

from django.db import migrations, models
import django.db.models.deletion


def generate_trigger_type_rows(apps, schema_editor):
    MaTriggerType = apps.get_model('mailroom', 'MaTriggerType')

    trigger_type = MaTriggerType()
    trigger_type.name = 'after joining'
    trigger_type.save()

    trigger_type = MaTriggerType()
    trigger_type.name = 'after taking survey'
    trigger_type.save()

    trigger_type = MaTriggerType()
    trigger_type.name = 'after using coupon'
    trigger_type.save()

    trigger_type = MaTriggerType()
    trigger_type.name = 'after no activity'
    trigger_type.save()

    trigger_type = MaTriggerType()
    trigger_type.name = 'after new survey goes live'
    trigger_type.save()

    trigger_type = MaTriggerType()
    trigger_type.name = 'after new coupon goes live'
    trigger_type.save()

    trigger_type = MaTriggerType()
    trigger_type.name = 'before coupon expires'
    trigger_type.save()

    trigger_type = MaTriggerType()
    trigger_type.name = 'before survey expires'
    trigger_type.save()

    trigger_type = MaTriggerType()
    trigger_type.name = 'before birthday'
    trigger_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mailroom', '0016_messagehistory_send_dt'),
    ]

    operations = [
        migrations.RunPython(generate_trigger_type_rows),
    ]
