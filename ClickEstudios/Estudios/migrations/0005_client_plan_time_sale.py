# Generated by Django 5.0 on 2024-12-18 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0004_alter_plan_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='time',
            field=models.TimeField(blank=True, default='08:00', null=True, verbose_name='Hora de inicio'),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_plan', models.CharField(blank=True, max_length=100, null=True)),
                ('description_plane', models.TextField(blank=True, null=True)),
                ('price_plan', models.IntegerField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, default='08:00', null=True, verbose_name='Hora de inicio')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('mont_reserv', models.IntegerField(blank=True, null=True)),
                ('is_reserve', models.BooleanField(default=False)),
                ('sale_payment', models.IntegerField(null=True)),
                ('proces_end', models.BooleanField(default=False)),
                ('start_date', models.DateField(verbose_name='Fecha de inicio')),
                ('end_date', models.DateField(verbose_name='Fecha final')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_sale', to='Estudios.client')),
            ],
        ),
    ]
