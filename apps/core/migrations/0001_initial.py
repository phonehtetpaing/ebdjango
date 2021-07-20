# Generated by Django 2.0.5 on 2018-06-02 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EndUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('django_pass_cd', models.CharField(max_length=2048, null=True, verbose_name='django user login password')),
                ('last_name', models.CharField(max_length=64, null=True, verbose_name='last name')),
                ('first_name', models.CharField(max_length=64, null=True, verbose_name='first name')),
                ('last_name_kana', models.CharField(max_length=64, null=True, verbose_name='last name kana')),
                ('first_name_kana', models.CharField(max_length=64, null=True, verbose_name='first name kana')),
                ('gender', models.CharField(max_length=25, null=True, verbose_name='gender')),
                ('age', models.CharField(max_length=25, null=True, verbose_name='age')),
                ('birth_date', models.DateField(null=True, verbose_name='birth day')),
                ('email', models.CharField(max_length=2048, null=True, verbose_name='email')),
                ('zip_code', models.CharField(max_length=20, null=True, verbose_name='zip code')),
                ('prefecture', models.CharField(max_length=32, null=True, verbose_name='prefecture / state')),
                ('address1', models.CharField(max_length=256, null=True, verbose_name='address1')),
                ('address2', models.CharField(max_length=256, null=True, verbose_name='address2')),
                ('tel1', models.CharField(max_length=32, null=True, verbose_name='tel1')),
                ('tel2', models.CharField(max_length=32, null=True, verbose_name='tel2')),
                ('admin_text', models.TextField(null=True, verbose_name='memo for admin')),
                ('last_login_dt', models.DateTimeField(null=True, verbose_name='login datetime')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enduser_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'EndUser',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='EndUserFacebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.CharField(max_length=256, null=True, verbose_name='sender id')),
                ('last_name', models.CharField(max_length=64, null=True, verbose_name='last name')),
                ('first_name', models.CharField(max_length=64, null=True, verbose_name='first name')),
                ('gender', models.CharField(max_length=25, null=True, verbose_name='gender')),
                ('locale', models.CharField(max_length=25, null=True, verbose_name='locale')),
                ('profile_pic_url', models.CharField(max_length=2024, null=True, verbose_name='profile picture url')),
                ('timezone', models.IntegerField(null=True, verbose_name='timezone')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('end_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enduserfacebook_end_user', to='core.EndUser', verbose_name='end_user')),
            ],
            options={
                'verbose_name': 'EndUserFacebook',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='EndUserLINE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=256, null=True, verbose_name='display_name')),
                ('user_id', models.CharField(max_length=64, null=True, verbose_name='user_id')),
                ('picture_url', models.CharField(max_length=2048, null=True, verbose_name='picture_url')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('end_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enduserline_end_user', to='core.EndUser', verbose_name='end_user')),
            ],
            options={
                'verbose_name': 'EndUserLINE',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd', models.CharField(max_length=64, null=True, verbose_name='service code')),
                ('name', models.CharField(max_length=256, null=True, verbose_name='service name')),
                ('fbms_access_url_part', models.CharField(max_length=2048, null=True, verbose_name='FB Messaneger Access URL')),
                ('fbms_access_token', models.CharField(max_length=2048, null=True, verbose_name='FB Access Token')),
                ('fbms_verify_token', models.CharField(max_length=256, null=True, verbose_name='FB Verify Token')),
                ('line_access_url_part', models.CharField(max_length=2048, null=True, verbose_name='LINE Access URL')),
                ('line_access_token', models.CharField(max_length=2048, null=True, verbose_name='LINE Access Token')),
                ('line_verify_token', models.CharField(max_length=256, null=True, verbose_name='LINE Verify Token')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
            ],
            options={
                'verbose_name': 'Service',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd', models.CharField(max_length=64, null=True, verbose_name='contract code')),
                ('company_name', models.CharField(max_length=256, null=True, verbose_name='company name')),
                ('company_name_kana', models.CharField(max_length=256, null=True, verbose_name='company name kana')),
                ('company_url', models.CharField(max_length=2048, null=True, verbose_name='company web site url')),
                ('fbms_access_url_part', models.CharField(max_length=2048, null=True, verbose_name='FB Messaneger Access URL')),
                ('fbms_access_token', models.CharField(max_length=2048, null=True, verbose_name='FB Access Token')),
                ('fbms_verify_token', models.CharField(max_length=256, null=True, verbose_name='FB Verify Token')),
                ('line_access_url_part', models.CharField(max_length=2048, null=True, verbose_name='LINE Access URL')),
                ('line_access_token', models.CharField(max_length=2048, null=True, verbose_name='LINE Access Token')),
                ('line_verify_token', models.CharField(max_length=256, null=True, verbose_name='LINE Verify Token')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_service', to='core.Service', verbose_name='Service')),
            ],
            options={
                'verbose_name': 'Vendor',
                'permissions': (),
            },
        ),
        migrations.CreateModel(
            name='VendorBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd', models.CharField(max_length=128, null=True, verbose_name='branch code')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='branch name')),
                ('cd_path', models.CharField(max_length=2024, null=True, verbose_name='branch code path')),
                ('join_cd', models.CharField(max_length=64, null=True, verbose_name='Client Join Code')),
                ('regist_dt', models.DateTimeField(auto_now_add=True, null=True, verbose_name='regist datetime')),
                ('update_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='update datetime')),
                ('is_delete', models.BooleanField(default=0, verbose_name='delete flg')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendorbranch_vendor', to='core.Vendor', verbose_name='Vendor')),
            ],
            options={
                'verbose_name': 'VendorBranch',
                'permissions': (),
            },
        ),
        migrations.AddField(
            model_name='enduser',
            name='vendor_branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enduser_vendor_branch', to='core.VendorBranch', verbose_name='vendor_branch'),
        ),
    ]