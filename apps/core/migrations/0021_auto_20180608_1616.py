# Generated by Django 2.0.5 on 2018-06-08 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20180608_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='Name')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('vendor_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservationevent_vendor_branch', to='core.VendorBranch', verbose_name='vendor_branch')),
            ],
            options={
                'verbose_name': 'ReservationEvent',
                'permissions': (),
            },
        ),
        migrations.RemoveField(
            model_name='reservation',
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
        migrations.AddField(
            model_name='reservation',
            name='reservation_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_reservation_event', to='core.ReservationEvent', verbose_name='reservation_event'),
        ),
    ]
