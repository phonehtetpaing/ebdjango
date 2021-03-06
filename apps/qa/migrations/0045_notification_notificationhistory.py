# Generated by Django 2.0.5 on 2019-09-09 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0044_auto_20190730_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='notification title')),
                ('body', models.TextField(verbose_name='notification body')),
                ('priority', models.IntegerField(default=0, verbose_name='notification priority')),
                ('schedule_dt', models.DateTimeField(verbose_name='schedule datetime')),
            ],
            options={
                'verbose_name': 'Notification',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='NotificationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False, verbose_name='seen')),
                ('seen_dt', models.DateTimeField(blank=True, null=True, verbose_name='seen datetime')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificationhistory_notification', to='qa.Notification', verbose_name='notification')),
                ('vendor_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificationhistory_vendor_user', to='qa.VendorUser', verbose_name='vendor_user')),
            ],
            options={
                'verbose_name': 'NotificationHistory',
                'permissions': (),
            },
        ),
    ]
