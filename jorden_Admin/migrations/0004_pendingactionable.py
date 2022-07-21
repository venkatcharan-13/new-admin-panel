# Generated by Django 4.0.6 on 2022-07-21 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jorden_Admin', '0003_channel_rule_remove_orderitem_order_delete_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingActionable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=100)),
                ('clientRemarks', models.CharField(blank=True, max_length=500)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PendingActions', to='jorden_Admin.listofcompanies')),
            ],
        ),
    ]
