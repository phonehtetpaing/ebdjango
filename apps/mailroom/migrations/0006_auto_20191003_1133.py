# Generated by Django 2.0.5 on 2019-10-03 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailroom', '0005_auto_20191002_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recipients',
        ),
        migrations.AddField(
            model_name='matrigger',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
    ]
