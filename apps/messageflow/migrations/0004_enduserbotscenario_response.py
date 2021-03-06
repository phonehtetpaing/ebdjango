# Generated by Django 2.0.5 on 2019-11-13 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messageflow', '0003_message_type_seed'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndUserBotScenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='user_id')),
                ('owner_id', models.IntegerField(verbose_name='owner_id')),
                ('app_id', models.CharField(max_length=256, verbose_name='app_id')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, verbose_name='regist datetime')),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messageflow.Bot')),
                ('current_message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='messageflow.Message')),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messageflow.Scenario')),
            ],
            options={
                'verbose_name': 'EndUserBotScenario',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(default='', null=True, verbose_name='response')),
                ('user_id', models.IntegerField(verbose_name='user_id')),
                ('owner_id', models.IntegerField(verbose_name='owner_id')),
                ('app_id', models.CharField(max_length=256, verbose_name='app_id')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('end_user_bot_scenario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='messageflow.EndUserBotScenario', verbose_name='end_user_bot_scenario')),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='messageflow.Message', verbose_name='message')),
            ],
            options={
                'verbose_name': 'Response',
                'permissions': (),
            },
        ),
    ]
