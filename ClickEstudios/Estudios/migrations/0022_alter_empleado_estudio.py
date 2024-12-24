# Generated by Django 5.0 on 2024-12-24 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0021_alter_empleado_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='estudio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='Estudios.estudios'),
        ),
    ]
