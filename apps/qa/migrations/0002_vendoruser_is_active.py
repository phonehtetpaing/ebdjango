# Generated by Django 2.0.5 on 2019-03-05 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendoruser',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='active flg'),
        ),
    ]
