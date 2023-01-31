# Generated by Django 4.0.4 on 2022-10-09 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('coin', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('blockchain', models.CharField(max_length=255)),
                ('transfer', models.FloatField()),
                ('swap', models.FloatField()),
                ('fiat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('nombre', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, help_text='esta el usuario activo?')),
                ('tipo', models.CharField(choices=[('S', 'Super'), ('A', 'Admin'), ('U', 'Usuario'), ('B', 'Banco')], default='U', help_text='Tipo de usuario', max_length=1, null=True)),
                ('usuario', models.OneToOneField(help_text='usuario asociado', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tPais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(help_text='Nombre Pais', max_length=120)),
                ('imagen', models.ImageField(blank=True, help_text='Imagen asociado al pais', null=True, upload_to='paises')),
                ('habilitado', models.BooleanField(default=True, help_text='Esta activo?')),
            ],
        ),
        migrations.CreateModel(
            name='tPaisDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(help_text='Nombre Documento x Pais', max_length=120)),
                ('tipo', models.CharField(choices=[('I', 'Imagen'), ('A', 'Archivo'), ('T', 'Texto')], default='I', help_text='Tipo de documento', max_length=1, null=True)),
                ('habilitado', models.BooleanField(default=True, help_text='Esta activo?')),
                ('pais', models.ForeignKey(help_text='Pais asociado', on_delete=django.db.models.deletion.CASCADE, to='backend.tpais')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leer', models.BooleanField(default=False, help_text='Tiene opcion de leer?')),
                ('escribir', models.BooleanField(default=False, help_text='Tiene opcion de escribir?')),
                ('borrar', models.BooleanField(default=False, help_text='Tiene opcion de borrar?')),
                ('actualizar', models.BooleanField(default=False, help_text='Tiene opcion de actualizar?')),
                ('modulo', models.ForeignKey(help_text='Opcion de menu asociada', on_delete=django.db.models.deletion.CASCADE, to='backend.modulo')),
                ('perfil', models.ForeignKey(help_text='Usuario asociado', on_delete=django.db.models.deletion.CASCADE, to='backend.perfil')),
            ],
        ),
    ]
