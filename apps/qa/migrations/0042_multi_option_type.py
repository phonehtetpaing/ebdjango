
from django.db import migrations, models


def generate_default_rows(apps, schema_editor):
    QuestionType = apps.get_model('qa', 'QuestionType')
    def_question_type = QuestionType()
    def_question_type.name = 'multioption'
    def_question_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0041_auto_20190619_1658'),
    ]

    operations = [
        migrations.RunPython(generate_default_rows),
    ]
