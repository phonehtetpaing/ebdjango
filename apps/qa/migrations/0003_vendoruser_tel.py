# Generated by Django 2.0.5 on 2019-03-08 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_vendoruser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendoruser',
            name='tel',
            field=models.CharField(max_length=32, null=True, verbose_name='tel'),
        ),
    ]