# Generated by Django 4.2.5 on 2023-09-25 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTurnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horarios_profesionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(default='', max_length=10)),
                ('hora_inicio', models.CharField(default='', max_length=10)),
                ('hora_fin', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='meses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(default='202301', max_length=10)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('hora', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='pacientes',
            fields=[
                ('id_pacientes', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=60)),
                ('apellido', models.CharField(default='', max_length=60)),
                ('obra_social', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='datos_profesionales',
            name='id',
        ),
        migrations.AddField(
            model_name='datos_profesionales',
            name='apellido',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='datos_profesionales',
            name='cuit',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='datos_profesionales',
            name='especialidad',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='datos_profesionales',
            name='id_profesional',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datos_profesionales',
            name='mail',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='datos_profesionales',
            name='nombre',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='datos_profesionales',
            name='razon_social',
            field=models.CharField(default='', max_length=60),
        ),
    ]