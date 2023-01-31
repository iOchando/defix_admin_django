# Generated by Django 4.0.4 on 2022-10-09 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tPaisServicioDefix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(help_text='Servicio Defix x Pais', max_length=120)),
                ('habilitado', models.BooleanField(default=True, help_text='Esta activo?')),
                ('pais', models.ForeignKey(help_text='Pais asociado', on_delete=django.db.models.deletion.CASCADE, to='backend.tpais')),
            ],
        ),
    ]