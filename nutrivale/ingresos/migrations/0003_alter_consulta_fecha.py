# Generated by Django 4.0.4 on 2023-01-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingresos', '0002_alter_consulta_fecha_alter_consulta_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='fecha',
            field=models.DateField(verbose_name='Fecha consulta'),
        ),
    ]
