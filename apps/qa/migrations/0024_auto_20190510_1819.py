# Generated by Django 2.0.5 on 2019-05-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0023_auto_20190510_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrigger',
            name='days',
            field=models.IntegerField(default=0, verbose_name='days'),
        ),
        migrations.AddField(
            model_name='matrigger',
            name='hours',
            field=models.IntegerField(default=0, verbose_name='days'),
        ),
    ]
