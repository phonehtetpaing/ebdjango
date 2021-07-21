# Generated by Django 2.0.5 on 2019-03-12 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0123_auto_20190312_1736'),
        ('qa', '0005_auto_20190312_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='vendor_branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coupon_vendor_branch', to='core.VendorBranch', verbose_name='vendor_branch'),
        ),
    ]