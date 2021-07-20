# Generated by Django 2.0.5 on 2018-06-03 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180603_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualMessageController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messaging_api_param_json', models.TextField(null=True, verbose_name='api parameter')),
                ('run_order_num', models.IntegerField(null=True, verbose_name='run order')),
                ('admin_text', models.TextField(null=True, verbose_name='memo for admin')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
            ],
            options={
                'verbose_name': 'ManualMessageController',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ManualMessageOverview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='name')),
                ('is_share', models.BooleanField(default=0, verbose_name='share flog for the same vendor')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('vendor_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manualmessageoverview_vendor_branch', to='core.VendorBranch', verbose_name='vendor_branch')),
            ],
            options={
                'verbose_name': 'ManualMessageOverview',
                'permissions': (),
            },
        ),
        migrations.RemoveField(
            model_name='automessagecontroller',
            name='automessage_trigger',
        ),
        migrations.RemoveField(
            model_name='automessagetrigger',
            name='automessage_condition',
        ),
        migrations.AddField(
            model_name='automessagecontroller',
            name='admin_text',
            field=models.TextField(null=True, verbose_name='memo for admin'),
        ),
        migrations.AddField(
            model_name='automessagecontroller',
            name='auto_message_trigger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagecontroller_auto_message_trigger', to='core.AutoMessageTrigger', verbose_name='auto_message_trigger'),
        ),
        migrations.AddField(
            model_name='automessagetrigger',
            name='auto_message_condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagetrigger_auto_message_condition', to='core.AutoMessageCondition', verbose_name='auto_message_condition'),
        ),
        migrations.AddField(
            model_name='manualmessagecontroller',
            name='manual_message_overview',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manualmessagecontroller_manual_message_overview', to='core.ManualMessageOverview', verbose_name='manual_message_overview'),
        ),
        migrations.AddField(
            model_name='manualmessagecontroller',
            name='messaging_api_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manualmessagecontroller_messaging_api_type', to='core.MessagingAPIType', verbose_name='messaging_api_type'),
        ),
    ]
