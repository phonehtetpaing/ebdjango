# Generated by Django 2.0.5 on 2019-06-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0032_auto_20190609_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivinghistory',
            name='memo',
            field=models.TextField(null=True, verbose_name='memo'),
        ),
        migrations.AlterField(
            model_name='receivinghistory',
            name='stats',
            field=models.IntegerField(default=0, null=True, verbose_name='status'),
        ),
    ]
