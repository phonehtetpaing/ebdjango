# Generated by Django 2.0.5 on 2019-10-01 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='app_id',
            field=models.CharField(max_length=256, verbose_name='app_id'),
        ),
    ]
