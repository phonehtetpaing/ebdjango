# Generated by Django 2.0.5 on 2019-11-19 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messageflow', '0007_enduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='', null=True, verbose_name='response')),
                ('user_id', models.IntegerField(verbose_name='user_id')),
                ('owner_id', models.IntegerField(verbose_name='owner_id')),
                ('app_id', models.CharField(max_length=256, verbose_name='app_id')),
                ('is_user_message', models.BooleanField(default=True, verbose_name='is_user_message')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('end_user_bot_scenario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='messageflow.EndUserBotScenario', verbose_name='end_user_bot_scenario')),
            ],
            options={
                'verbose_name': 'LogLine',
                'permissions': (),
            },
        ),
        migrations.RemoveField(
            model_name='response',
            name='end_user_bot_scenario',
        ),
        migrations.RemoveField(
            model_name='response',
            name='message',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
