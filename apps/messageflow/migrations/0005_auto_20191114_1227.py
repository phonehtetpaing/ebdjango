# Generated by Django 2.0.5 on 2019-11-14 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messageflow', '0004_enduserbotscenario_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='enduserbotscenario',
            name='state',
            field=models.CharField(default='INITIAL', max_length=256, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='messageblock',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_block_set', to='messageflow.Scenario', verbose_name='scenario'),
        ),
    ]