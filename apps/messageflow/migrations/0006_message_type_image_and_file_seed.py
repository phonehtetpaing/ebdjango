# Generated by Django 2.0.5 on 2019-10-10 02:11

from django.db import migrations


def generate_message_type_rows(apps, schema_editor):
    MessageType = apps.get_model('messageflow', 'MessageType')

    trigger_type = MessageType()
    trigger_type.name = 'image'
    trigger_type.save()

    trigger_type = MessageType()
    trigger_type.name = 'file'
    trigger_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('messageflow', '0005_auto_20191114_1227'),

    ]

    operations = [
        migrations.RunPython(generate_message_type_rows),
    ]
