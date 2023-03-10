# Generated by Django 4.0.4 on 2022-11-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0056_fiattransaccion_email_tkyccabecera_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiattransaccion',
            name='adjuntofiat',
            field=models.ImageField(blank=True, help_text='adjunto soporte de la venta o compra', null=True, upload_to='media/fiat'),
        ),
        migrations.AlterField(
            model_name='tkycdetalle',
            name='imagen',
            field=models.ImageField(help_text='Imagen KYC', null=True, upload_to='media/archivoskyc'),
        ),
        migrations.AlterField(
            model_name='tpais',
            name='imagen',
            field=models.ImageField(blank=True, help_text='Imagen asociado al pais', null=True, upload_to='media/paises'),
        ),
        migrations.AlterField(
            model_name='tpaisbanco',
            name='imagen',
            field=models.ImageField(blank=True, help_text='Logo asociado al banco', null=True, upload_to='media/bancos'),
        ),
    ]
