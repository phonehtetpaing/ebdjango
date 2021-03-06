# Generated by Django 2.0.5 on 2019-03-25 01:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


def generate_default_rows(apps, schema_editor):
    QuestionType = apps.get_model('qa', 'QuestionType')
    def_question_type = QuestionType()
    def_question_type.name = 'text'
    def_question_type.save()

    def_question_type = QuestionType()
    def_question_type.name = 'option'
    def_question_type.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0126_auto_20190325_1059'),
        ('qa', '0008_auto_20190325_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='question name')),
                ('question_text', models.CharField(default='', max_length=2048, verbose_name='question text')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
            ],
            options={
                'verbose_name': 'Question',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='questionnaire name')),
                ('intro', models.CharField(default='', max_length=2048, verbose_name='intro')),
                ('outro', models.CharField(default='', max_length=2048, verbose_name='outro')),
                ('valid_from', models.DateTimeField(default=django.utils.timezone.now, verbose_name='valid from datetime')),
                ('valid_until', models.DateTimeField(null=True, verbose_name='valid until datetime')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('vendor_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qa_questionnaire_vendor_branch', to='core.VendorBranch', verbose_name='vendor_branch')),
            ],
            options={
                'verbose_name': 'Questionnaire',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='QuestionnaireQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_order', models.IntegerField(default=0, verbose_name='display order')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa_questionnairequestion_question', to='qa.Question', verbose_name='question')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa_questionnairequestion_questionnaire', to='qa.Questionnaire', verbose_name='questionnaire')),
            ],
            options={
                'verbose_name': 'Questionnaire Question',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='question type name')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
            ],
            options={
                'verbose_name': 'QuestionType',
                'permissions': (),
            },
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa_question_type', to='qa.QuestionType', verbose_name='type'),
        ),
        migrations.AddField(
            model_name='question',
            name='vendor_branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qa_question_vendor_branch', to='core.VendorBranch', verbose_name='vendor_branch'),
        ),
        migrations.RunPython(generate_default_rows),
    ]
