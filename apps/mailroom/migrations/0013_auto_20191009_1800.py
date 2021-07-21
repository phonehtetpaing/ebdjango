# Generated by Django 2.0.5 on 2019-10-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailroom', '0012_auto_20191009_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagehistory',
            name='date',
        ),
        migrations.AddField(
            model_name='messagehistory',
            name='send_dt',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='send_dt'),
        ),
        migrations.AlterField(
            model_name='messagehistory',
            name='recipients',
            field=models.TextField(null=True, verbose_name='message recipients'),
        ),
        migrations.AlterField(
            model_name='messagehistory',
            name='status',
            field=models.IntegerField(null=True, verbose_name='status'),
        ),
    ]
