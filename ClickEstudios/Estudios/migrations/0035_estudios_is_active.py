# Generated by Django 5.0 on 2025-01-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0034_facturacion_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudios',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]