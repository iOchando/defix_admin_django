# Generated by Django 4.0.4 on 2022-11-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0026_alter_fiattransaccion_accion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tkyccuenta',
            name='tipocuenta',
            field=models.TextField(blank=True, help_text='tipo  de cuenta del titular', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fiattransaccion',
            name='estatus',
            field=models.CharField(choices=[('1', 'Creado'), ('2', 'Asignado'), ('3', 'Procesado'), ('4', 'Completado'), ('5', 'Anulado')], default='C', max_length=1),
        ),
    ]