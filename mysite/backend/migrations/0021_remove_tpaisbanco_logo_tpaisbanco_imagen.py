# Generated by Django 4.0.4 on 2022-11-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_alter_tpaisbanco_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tpaisbanco',
            name='logo',
        ),
        migrations.AddField(
            model_name='tpaisbanco',
            name='imagen',
            field=models.ImageField(blank=True, help_text='Logo asociado al banco', null=True, upload_to='bancos'),
        ),
    ]
