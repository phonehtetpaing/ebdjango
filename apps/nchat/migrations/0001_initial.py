# Generated by Django 2.0.5 on 2019-09-03 06:45

import apps.nchat.models.business
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=255, unique=True, verbose_name='business name')),
                ('service_name', models.CharField(max_length=255, verbose_name='service name')),
                ('logo', models.ImageField(max_length=2024, null=True, upload_to=apps.nchat.models.business.business_directory_path, verbose_name='logo')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_super_oem', models.BooleanField(default=False, verbose_name='super oem flg')),
                ('is_delete', models.BooleanField(default=False, verbose_name='delete flg')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent_business', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_businesses', to='nchat.Business')),
            ],
            options={
                'verbose_name': 'Business',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='BusinessPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='business plan name')),
                ('price', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='business plan price')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=False, verbose_name='delete flg')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nchat.Business', verbose_name='Business')),
            ],
            options={
                'verbose_name': 'BusinessPlan',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='VendorUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=64, verbose_name='last name')),
                ('first_name', models.CharField(max_length=64, verbose_name='first name')),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='email')),
                ('tel', models.CharField(max_length=32, null=True, verbose_name='tel')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_oem_admin', models.BooleanField(default=False, verbose_name='oem admin flg')),
                ('is_active', models.BooleanField(default=False, verbose_name='active flg')),
                ('is_delete', models.BooleanField(default=False, verbose_name='delete flg')),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nchat_vendoruser_user', to=settings.AUTH_USER_MODEL)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nchat_vendoruser_parent_business', to='nchat.Business', verbose_name='parent_business')),
            ],
            options={
                'verbose_name': 'VendorUser',
                'permissions': (),
            },
        ),
    ]
