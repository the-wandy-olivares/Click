# Generated by Django 5.0 on 2024-12-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0014_alter_sale_mount_box_movements'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='debit_mount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_choice',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha seleccionada'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='time',
            field=models.TimeField(blank=True, default='08:00', null=True, verbose_name='Hora seleccionada'),
        ),
    ]