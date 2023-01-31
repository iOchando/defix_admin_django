# Generated by Django 4.0.4 on 2022-10-26 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_alter_tpais_kyccompra_alter_tpais_kycventa'),
    ]

    operations = [
        migrations.CreateModel(
            name='tTipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, help_text='Nombre del Banco', max_length=120, null=True)),
                ('habilitado', models.BooleanField(default=True, help_text='Esta activo?')),
            ],
        ),
        migrations.CreateModel(
            name='tPaisBanco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, help_text='Nombre del Banco', max_length=120, null=True)),
                ('codigo', models.TextField(blank=True, help_text='Codigo del Banco 4 digitos', max_length=4, null=True)),
                ('logo', models.ImageField(blank=True, help_text='Logo asociado al banco', null=True, upload_to='paises')),
                ('habilitado', models.BooleanField(default=True, help_text='Esta activo?')),
                ('pais', models.ForeignKey(help_text='Pais asociado', on_delete=django.db.models.deletion.CASCADE, to='backend.tpais')),
            ],
        ),
        migrations.CreateModel(
            name='tkycCuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.TextField(blank=True, help_text='Nombre del Titular', max_length=150, null=True)),
                ('cedula', models.TextField(blank=True, help_text='Numero de Identificacion', max_length=20, null=True)),
                ('telefono', models.TextField(blank=True, help_text='Numero de telefono', max_length=50, null=True)),
                ('numerocuenta', models.TextField(blank=True, help_text='numero de cuenta del titular', max_length=20, null=True)),
                ('habilitado', models.BooleanField(default=True, help_text='Esta activo?')),
                ('banco', models.ForeignKey(blank=True, help_text='Id de Banco Pais', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backend.tpaisbanco')),
                ('kyccabecera', models.ForeignKey(blank=True, help_text='Id de KYC asociado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backend.tkyccabecera')),
                ('tipopago', models.ForeignKey(blank=True, help_text='Id de tipo de pago', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backend.ttipopago')),
            ],
        ),
    ]