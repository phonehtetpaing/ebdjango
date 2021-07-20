# Generated by Django 2.0.5 on 2018-10-19 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0082_auto_20181019_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='summarylogvendorusers',
            name='level',
            field=models.CharField(max_length=64, null=True, verbose_name='LEVEL'),
        ),
        migrations.AddField(
            model_name='summarylogvendorusers',
            name='log_dt',
            field=models.CharField(max_length=128, null=True, verbose_name='Log Datetime (String)'),
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
