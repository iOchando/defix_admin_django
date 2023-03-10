# Generated by Django 4.0.4 on 2022-10-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_alter_tkycdetalle_imagen_alter_tkycdetalle_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tpais',
            name='kyccompra',
            field=models.BooleanField(default=True, help_text='valida KYC en compra?'),
        ),
        migrations.AlterField(
            model_name='tpais',
            name='kycventa',
            field=models.BooleanField(default=True, help_text='valida KYC en venta?'),
        ),
    ]
