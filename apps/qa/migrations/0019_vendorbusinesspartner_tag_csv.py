# Generated by Django 2.0.5 on 2019-05-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0018_auto_20190501_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorbusinesspartner',
            name='tag_csv',
            field=models.CharField(max_length=256, null=True, verbose_name='Tag CSV'),
        ),
    ]
