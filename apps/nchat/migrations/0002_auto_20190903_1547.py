# Generated by Django 2.0.5 on 2019-09-03 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nchat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='parent_business',
            new_name='parent',
        ),
    ]