# Generated by Django 5.0.2 on 2024-02-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0002_alter_cuenta_impuesto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='importeAdeudado',
        ),
        migrations.AddField(
            model_name='cuenta',
            name='importeAdeudado_db',
            field=models.FloatField(default=0),
        ),
    ]
