# Generated by Django 2.0.5 on 2019-12-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageflow', '0013_auto_20191212_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduserbotscenario',
            name='state',
            field=models.CharField(default='FIRST', max_length=256, verbose_name='state'),
        ),
    ]
