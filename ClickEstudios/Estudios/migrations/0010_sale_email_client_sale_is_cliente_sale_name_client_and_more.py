# Generated by Django 5.0 on 2024-12-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0009_remove_plan_likes_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='email_client',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='is_cliente',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sale',
            name='name_client',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='phone_client',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
