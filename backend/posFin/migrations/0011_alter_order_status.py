# Generated by Django 5.1.5 on 2025-03-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posFin', '0010_alter_order_service_charge_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('paid', 'paid'), ('cancelled', 'cancelled')], default='pending', max_length=20),
        ),
    ]
