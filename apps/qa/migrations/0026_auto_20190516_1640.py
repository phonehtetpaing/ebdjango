# Generated by Django 2.0.5 on 2019-05-16 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0025_auto_20190514_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_text',
            field=models.CharField(default='', max_length=2048, verbose_name='question text'),
        ),
    ]