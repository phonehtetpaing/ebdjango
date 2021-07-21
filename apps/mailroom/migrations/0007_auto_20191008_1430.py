# Generated by Django 2.0.5 on 2019-10-08 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailroom', '0006_auto_20191003_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='message subject')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailroom_messagetemplate_message', to='mailroom.Message', verbose_name='message')),
            ],
            options={
                'verbose_name': 'MessageTemplate',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MessageTemplateCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='message subject')),
            ],
            options={
                'verbose_name': 'MessageTemplateCategory',
                'permissions': (),
            },
        ),
        migrations.AddField(
            model_name='messagetemplate',
            name='template_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailroom_messagetemplate_template_category', to='mailroom.MessageTemplateCategory', verbose_name='template_category'),
        ),
    ]