# Generated by Django 5.1.5 on 2025-02-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_category_dish_delete_menu_category_dishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='extra_dish_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
