# Generated by Django 4.0.5 on 2022-10-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=11)),
                ('nombre_completo', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=12)),
            ],
        ),
    ]
