# Generated by Django 5.1.5 on 2025-03-29 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_alter_financereport_total_sales_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financereport',
            old_name='total_serviceCharge',
            new_name='total_service_charge',
        ),
    ]
