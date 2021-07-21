# Generated by Django 2.0.5 on 2019-05-07 04:44

import apps.qa.models.questionnaire
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0020_auto_20190507_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='valid_from',
            field=models.DateTimeField(default=apps.qa.models.questionnaire.get_formatted_now, verbose_name='valid from datetime'),
        ),
    ]