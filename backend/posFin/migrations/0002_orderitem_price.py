# Generated by Django 5.1.5 on 2025-03-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posFin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=2),
            preserve_default=False,
        ),
    ]
