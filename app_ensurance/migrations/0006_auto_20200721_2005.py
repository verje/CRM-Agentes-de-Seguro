# Generated by Django 2.2.10 on 2020-07-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ensurance', '0005_auto_20200721_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilla',
            name='tipodoc',
            field=models.CharField(choices=[(1, 'DNI'), (2, 'Pasaporte'), (3, 'Cedula de Extranjeria')], max_length=20),
        ),
    ]