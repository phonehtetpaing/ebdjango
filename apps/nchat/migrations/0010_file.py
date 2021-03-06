# Generated by Django 2.0.5 on 2019-11-07 03:55

import apps.nchat.models.file
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nchat', '0009_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.IntegerField(verbose_name='owner_id')),
                ('app_id', models.CharField(max_length=256, verbose_name='app_id')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(upload_to=apps.nchat.models.file.vendor_directory_path)),
            ],
        ),
    ]
