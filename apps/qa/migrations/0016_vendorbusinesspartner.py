# Generated by Django 2.0.5 on 2019-05-01 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0134_auto_20190501_1138'),
        ('qa', '0015_merge_20190501_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorBusinessPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True, verbose_name='company name')),
                ('short_name', models.CharField(max_length=256, null=True, verbose_name='company short name')),
                ('name_kana', models.CharField(max_length=256, null=True, verbose_name='company name kana')),
                ('email', models.CharField(max_length=2048, null=True, verbose_name='email')),
                ('zip_code', models.CharField(max_length=20, null=True, verbose_name='zip code')),
                ('prefecture', models.CharField(max_length=32, null=True, verbose_name='prefecture / state')),
                ('address1', models.CharField(max_length=256, null=True, verbose_name='address1')),
                ('address2', models.CharField(max_length=256, null=True, verbose_name='address2')),
                ('tel1', models.CharField(max_length=32, null=True, verbose_name='tel1')),
                ('tel2', models.CharField(max_length=32, null=True, verbose_name='tel2')),
                ('fax', models.CharField(max_length=32, null=True, verbose_name='fax')),
                ('memo', models.TextField(null=True, verbose_name='memo')),
                ('attribute_json', models.TextField(null=True, verbose_name='Attribute')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendorbusinesspartner_vendor_business_partner', to='core.Vendor', verbose_name='Vendor_BusinessPartner')),
            ],
            options={
                'verbose_name': 'VendorBusinessPartner',
                'permissions': (),
            },
        ),
    ]
