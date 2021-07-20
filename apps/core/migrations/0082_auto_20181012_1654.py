# Generated by Django 2.0.5 on 2018-10-12 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_auto_20180919_1448'),
    ]

    operations = [
#         migrations.CreateModel(
#             name='EndUserContactChat',
#             fields=[
#                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
#                 ('user_id', models.CharField(max_length=64, null=True, verbose_name='user_id')),
#                 ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
#                 ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
#                 ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
#                 ('end_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endusercontactchat_end_user', to='core.EndUser', verbose_name='end_user')),
#             ],
#             options={
#                 'verbose_name': 'EndUserContactChat',
#                 'permissions': (),
#             },
#         ),
#         migrations.AddField(
#             model_name='vendor',
#             name='contactchat_access_token',
#             field=models.CharField(max_length=2048, null=True, verbose_name='ContactChat Access Token'),
#         ),
#         migrations.AddField(
#             model_name='vendor',
#             name='contactchat_access_url_part',
#             field=models.CharField(max_length=2048, null=True, verbose_name='ContactChat Access URL'),
#         ),
#         migrations.AddField(
#             model_name='vendor',
#             name='contactchat_public_url',
#             field=models.CharField(max_length=1024, null=True, verbose_name='ContactChat Public URL'),
#         ),
#         migrations.AddField(
#             model_name='vendor',
#             name='contactchat_verify_token',
#             field=models.CharField(max_length=256, null=True, verbose_name='ContactChat Verify Token'),
#         ),
#         migrations.AlterField(
#             model_name='automessagecontroller',
#             name='auto_message_trigger',
#             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagecontroller_auto_message_trigger', to='core.AutoMessageTrigger', verbose_name='auto_message_trigger'),
#         ),
#         migrations.AlterField(
#             model_name='automessagehistory',
#             name='auto_message_condition',
#             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagehistory_auto_message_condition', to='core.AutoMessageCondition', verbose_name='auto_message_condition'),
#         ),
#         migrations.AlterField(
#             model_name='automessagehistory',
#             name='auto_message_trigger',
#             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagehistory_auto_message_trigger', to='core.AutoMessageTrigger', verbose_name='auto_message_trigger'),
#         ),
#         migrations.AlterField(
#             model_name='automessagetrigger',
#             name='auto_message_condition',
#             field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='automessagetrigger_auto_message_condition', to='core.AutoMessageCondition', verbose_name='auto_message_condition'),
#         ),
    ]
