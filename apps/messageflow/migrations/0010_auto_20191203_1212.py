# Generated by Django 2.0.5 on 2019-12-03 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageflow', '0009_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduser',
            name='email',
            field=models.CharField(max_length=255, verbose_name='email'),
        ),
    ]
