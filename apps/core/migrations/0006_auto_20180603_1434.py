# Generated by Django 2.0.5 on 2018-06-03 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180603_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automessagecontroller',
            name='auto_message_trigger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagecontroller_auto_message_trigger', to='core.AutoMessageTrigger', verbose_name='auto_message_trigger'),
        ),
        migrations.AlterField(
            model_name='automessagetrigger',
            name='auto_message_condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagetrigger_auto_message_condition', to='core.AutoMessageCondition', verbose_name='auto_message_condition'),
        ),
    ]