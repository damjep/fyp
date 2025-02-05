# Generated by Django 5.1.5 on 2025-02-05 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dish_type', models.CharField(choices=[('Starters', 'Starters'), ('Mains', 'Mains'), ('Desserts', 'Desserts'), ('Drinks', 'Drinks')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
