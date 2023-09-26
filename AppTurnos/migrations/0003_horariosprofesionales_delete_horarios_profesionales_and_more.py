# Generated by Django 4.2.5 on 2023-09-26 14:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppTurnos', '0002_horarios_profesionales_meses_pacientes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorariosProfesionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(default='', max_length=10)),
                ('hora_inicio', models.CharField(default='', max_length=10)),
                ('hora_fin', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Horarios_profesionales',
        ),
        migrations.RenameField(
            model_name='pacientes',
            old_name='id_pacientes',
            new_name='id_paciente',
        ),
        migrations.AddField(
            model_name='meses',
            name='id_profesional',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AppTurnos.datosprofesionales'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meses',
            name='fecha',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.RenameModel(
            old_name='Datos_profesionales',
            new_name='DatosProfesionales',
        ),
        migrations.AddField(
            model_name='horariosprofesionales',
            name='id_profesional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTurnos.datosprofesionales'),
        ),
    ]