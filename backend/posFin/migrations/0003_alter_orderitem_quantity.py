# Generated by Django 5.1.5 on 2025-03-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posFin', '0002_orderitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
