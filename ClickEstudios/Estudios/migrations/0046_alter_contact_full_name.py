# Generated by Django 5.1.5 on 2025-02-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0045_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
