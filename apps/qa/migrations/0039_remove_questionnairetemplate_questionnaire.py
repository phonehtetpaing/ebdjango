# Generated by Django 2.0.5 on 2019-06-19 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0038_questionnairetemplate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnairetemplate',
            name='questionnaire',
        ),
    ]
