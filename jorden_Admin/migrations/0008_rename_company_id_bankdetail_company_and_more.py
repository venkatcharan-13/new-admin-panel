# Generated by Django 4.0.6 on 2022-07-21 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jorden_Admin', '0007_rename_company_property_bankdetail_company_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankdetail',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='companyaddress',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='companycontext',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='pendingactionable',
            old_name='company_property',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='watchoutpoint',
            old_name='company_id',
            new_name='company',
        ),
    ]