# Generated by Django 2.0.5 on 2019-11-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nchat', '0011_enduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduser',
            name='app_id',
            field=models.CharField(default=1, max_length=256, verbose_name='app_id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enduser',
            name='owner_id',
            field=models.IntegerField(default=1, verbose_name='owner_id'),
            preserve_default=False,
        ),
    ]
