# Generated by Django 4.0.4 on 2022-10-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_tkycdetalle_documento_alter_tkycdetalle_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='tkycdetalle',
            name='tipo',
            field=models.CharField(default='I', help_text='Tipo de documento', max_length=1, null=True),
        ),
    ]
