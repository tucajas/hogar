# Generated by Django 5.0.2 on 2024-02-14 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
        ('impuesto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='impuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impuesto', to='impuesto.impuesto'),
        ),
    ]