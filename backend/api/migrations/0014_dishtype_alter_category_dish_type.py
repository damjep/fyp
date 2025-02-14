# Generated by Django 5.1.5 on 2025-02-14 04:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_category_extra_dish_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='dish_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dishtype'),
        ),
    ]
