# Generated by Django 2.0.5 on 2018-08-02 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_merge_20180802_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automessagecondition',
            options={'ordering': ['id'], 'permissions': (), 'verbose_name': 'AutoMessageCondition'},
        ),
        migrations.AlterModelOptions(
            name='automessagecontroller',
            options={'ordering': ['id'], 'permissions': (), 'verbose_name': 'AutomessageController'},
        ),
        migrations.AlterModelOptions(
            name='automessagehistory',
            options={'ordering': ['send_dt'], 'permissions': (), 'verbose_name': 'AutoMessageHistory'},
        ),
        migrations.AlterModelOptions(
            name='automessagetrigger',
            options={'ordering': ['trigger_days_num', 'trigger_time', 'is_trigger_after'], 'permissions': (), 'verbose_name': 'AutomessageTrigger'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-id'], 'permissions': (), 'verbose_name': 'Event'},
        ),
        migrations.AlterModelOptions(
            name='eventcategory',
            options={'ordering': ['-id'], 'permissions': (), 'verbose_name': 'EventCategory'},
        ),
        migrations.AlterModelOptions(
            name='eventreservation',
            options={'ordering': ['-id'], 'permissions': (), 'verbose_name': 'EventReservation'},
        ),
        migrations.AlterModelOptions(
            name='manualmessagehistory',
            options={'ordering': ['send_dt'], 'permissions': (), 'verbose_name': 'ManualMessageHistory'},
        ),
        migrations.AlterModelOptions(
            name='manualmessageoverview',
            options={'ordering': ['-id'], 'permissions': (), 'verbose_name': 'ManualMessageOverview'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id'], 'permissions': (), 'verbose_name': 'Tag'},
        ),
        migrations.RemoveField(
            model_name='enduserstate',
            name='vendor_branch',
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
