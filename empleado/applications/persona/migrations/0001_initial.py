# Generated by Django 3.2.5 on 2021-07-27 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleado',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=60, verbose_name='apellidos')),
                ('full_name', models.CharField(blank=True, max_length=120, verbose_name='Nombres completos')),
                ('job', models.CharField(choices=[('0', ' CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO')], max_length=1, verbose_name='Trabajo')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='empleado')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
                ('habilidades', models.ManyToManyField(to='persona.Habilidades')),
            ],
            options={
                'verbose_name': 'Trabajadores',
                'verbose_name_plural': 'Empleados',
                'ordering': ['first_name'],
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
