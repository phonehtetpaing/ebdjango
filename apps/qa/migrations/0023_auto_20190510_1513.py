# Generated by Django 2.0.5 on 2019-05-10 06:13

from django.db import migrations, models
import django.db.models.deletion


def generate_default_rows(apps, schema_editor):
    MaTriggerType = apps.get_model('qa', 'MaTriggerType')
    def_matriggertype = MaTriggerType()
    def_matriggertype.name = "after joining"
    def_matriggertype.save()

    def_matriggertype = MaTriggerType()
    def_matriggertype.name = "after taking survey"
    def_matriggertype.save()

    def_matriggertype = MaTriggerType()
    def_matriggertype.name = "after using coupon"
    def_matriggertype.save()

    def_matriggertype = MaTriggerType()
    def_matriggertype.name = "after no activity"
    def_matriggertype.save()

    def_matriggertype = MaTriggerType()
    def_matriggertype.name = "after new survey goes live"
    def_matriggertype.save()

    def_matriggertype = MaTriggerType()
    def_matriggertype.name = "after new coupon goes live"
    def_matriggertype.save()

    def_matriggertype = MaTriggerType()
    def_matriggertype.name = "before coupon expires"
    def_matriggertype.save()

    def_matriggertype = MaTriggerType()
    def_matriggertype.name = "before survey expires"
    def_matriggertype.save()

    def_matriggertype = MaTriggerType()
    def_matriggertype.name = "before birthday"
    def_matriggertype.save()


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0022_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaTrigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa_matrigger_message', to='qa.Message', verbose_name='message')),
            ],
            options={
                'verbose_name': 'MaTrigger',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MaTriggerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='ma trigger type name')),
            ],
            options={
                'verbose_name': 'MaTriggerType',
                'permissions': (),
            },
        ),
        migrations.AddField(
            model_name='matrigger',
            name='trigger_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa_matrigger_trigger_type', to='qa.MaTriggerType', verbose_name='trigger_type'),
        ),
        migrations.RunPython(generate_default_rows),
    ]
