# Generated by Django 2.0.5 on 2019-12-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageflow', '0014_auto_20191213_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduserbotscenario',
            name='state',
            field=models.CharField(default='INITIAL', max_length=256, verbose_name='state'),
        ),
    ]
