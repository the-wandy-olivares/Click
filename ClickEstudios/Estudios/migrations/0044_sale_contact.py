# Generated by Django 5.1.5 on 2025-02-10 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0043_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_contact', to='Estudios.contact'),
        ),
    ]
