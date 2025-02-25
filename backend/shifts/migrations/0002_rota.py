# Generated by Django 5.1.5 on 2025-02-24 10:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shifts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.shift')),
                ('users', models.ManyToManyField(related_name='Users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
