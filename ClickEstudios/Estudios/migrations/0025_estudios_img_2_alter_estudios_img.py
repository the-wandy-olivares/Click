# Generated by Django 5.0 on 2024-12-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0024_alter_estudios_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudios',
            name='img_2',
            field=models.ImageField(blank=True, null=True, upload_to='media/estudios', verbose_name='Imagen negra'),
        ),
        migrations.AlterField(
            model_name='estudios',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/estudios', verbose_name='Imagen blanca'),
        ),
    ]