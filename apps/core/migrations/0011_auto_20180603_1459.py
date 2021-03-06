# Generated by Django 2.0.5 on 2018-06-03 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180603_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorReservationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_start_time', models.TimeField(null=True, verbose_name='work start time')),
                ('work_end_time', models.TimeField(null=True, verbose_name='work end time')),
                ('day_off_csv', models.CharField(max_length=32, null=True, verbose_name='off day')),
                ('buffer_period', models.IntegerField(null=True, verbose_name='buffer minutes')),
                ('is_google_calender_oauth', models.BooleanField(default=0, verbose_name='google_calender_oauth_flg')),
                ('admin_text', models.TextField(null=True, verbose_name='memo for admin')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('vendor_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendorreservationsettings_vendor_branch', to='core.VendorBranch', verbose_name='vendor_branch')),
            ],
            options={
                'verbose_name': 'VendorReservationSettings',
                'permissions': (),
            },
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
