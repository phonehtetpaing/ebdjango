# Generated by Django 2.0.5 on 2019-10-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailroom', '0008_auto_20191008_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplate',
            name='language_code',
            field=models.CharField(default='', max_length=32, verbose_name='message template category name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messagetemplatecategory',
            name='language_code',
            field=models.CharField(default='', max_length=32, verbose_name='message template category name'),
            preserve_default=False,
        ),
    ]