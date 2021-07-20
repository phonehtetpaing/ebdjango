# Generated by Django 2.0.5 on 2018-11-15 07:36
import ast
from django.db import migrations


def migrate_todo_message(apps, schema_editor):
    MessageBlock = apps.get_model('core', 'MessageBlock')
    for block in MessageBlock.objects.all():
        dict_list = ast.literal_eval(block.messaging_api_param_json)
        for count, message in enumerate(dict_list):
            if message['type'] == 'todosendmessage' and message['version'] == '1.0':
                template = {
                    "type": "formsendmessage",
                    "version": "2.0",
                    "title": "",
                    "memo": "",
                    "todo": False,
                    "payload": []
                }
                template['title'] = message['payload']['title']
                template['memo'] = message['payload']['memo']
                template['todo'] = True
                template['payload'] = [{"question": message['payload']['question'],"attribute": "answer"}]
                dict_list[count] = template
        block.messaging_api_param_json = dict_list
        block.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0097_auto_20181115_1733'),
    ]

    operations = [
        migrations.RunPython(migrate_todo_message),
    ]