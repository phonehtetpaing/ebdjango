# Generated by Django 2.0.5 on 2018-07-02 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_auto_20180702_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndUserStoryTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload', models.CharField(max_length=256, null=True, verbose_name='payload value')),
                ('next_end_user_state', models.CharField(max_length=256, null=True, verbose_name='payload value')),
                ('messaging_api_type', models.CharField(max_length=256, null=True, verbose_name='payload value')),
                ('messaging_api_param_json', models.TextField(null=True, verbose_name='api parameter')),
                ('run_order_num', models.IntegerField(null=True, verbose_name='run order')),
                ('is_todo', models.BooleanField(default=0, verbose_name='todo flg')),
                ('todo_title', models.CharField(max_length=128, null=True, verbose_name='todo title')),
                ('admin_text', models.TextField(null=True, verbose_name='memo for admin')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
            ],
            options={
                'verbose_name': 'EndUserStoryTemplate',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='EndUserStoryTemplateCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True, verbose_name='payload value')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enduserstorytemplatecategory_service', to='core.Service', verbose_name='service')),
            ],
            options={
                'verbose_name': 'EndUserStoryTemplateCategory',
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
        migrations.AddField(
            model_name='enduserstorytemplate',
            name='end_user_story_template_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enduserstorytemplate_end_user_story_template_category', to='core.EndUserStoryTemplateCategory', verbose_name='end_user_story_template_category'),
        ),
    ]