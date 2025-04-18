# Generated by Django 5.0 on 2024-12-17 21:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/empleados')),
                ('role', models.CharField(choices=[('admin', 'Administrador'), ('supervisor', 'Supervisor'), ('customer_service', 'Servicio al Cliente'), ('photographer', 'Fotografo'), ('editor', 'Editor'), ('estandard', 'Estandar')], default='estandard', max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
            },
        ),
        migrations.CreateModel(
            name='Moment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/momentos')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'momento',
                'verbose_name_plural': 'momentos',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/servicios')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
            },
        ),
        migrations.CreateModel(
            name='Estudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/estudios')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados_estudio', to='Estudios.empleado')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_estudio', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'estudio',
                'verbose_name_plural': 'estudios',
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='estudio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='Estudios.estudios'),
        ),
        migrations.CreateModel(
            name='ImgMoment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/imagenes')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('moment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='img_moments', to='Estudios.moment')),
            ],
            options={
                'verbose_name': 'imagen',
                'verbose_name_plural': 'imagenes',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='media/planes')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planes', to='Estudios.service')),
            ],
            options={
                'verbose_name': 'plan',
                'verbose_name_plural': 'planes',
            },
        ),
        migrations.AddField(
            model_name='moment',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='momentos', to='Estudios.service'),
        ),
    ]
