# Generated by Django 2.0.5 on 2018-06-03 11:51

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('core', '0011_auto_20180603_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduser',
            name='tag',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='automessagecontroller',
            name='auto_message_trigger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagecontroller_auto_message_trigger', to='core.AutoMessageTrigger', verbose_name='auto_message_trigger'),
        ),
        migrations.AlterField(
            model_name='automessagehistory',
            name='auto_message_condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagehistory_auto_message_condition', to='core.AutoMessageCondition', verbose_name='auto_message_condition'),
        ),
        migrations.AlterField(
            model_name='automessagehistory',
            name='auto_message_trigger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagehistory_auto_message_trigger', to='core.AutoMessageTrigger', verbose_name='auto_message_trigger'),
        ),
        migrations.AlterField(
            model_name='automessagetrigger',
            name='auto_message_condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagetrigger_auto_message_condition', to='core.AutoMessageCondition', verbose_name='auto_message_condition'),
        ),
    ]
