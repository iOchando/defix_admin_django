# Generated by Django 4.0.4 on 2022-11-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0055_delete_tpaisbancorango'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiattransaccion',
            name='email',
            field=models.TextField(blank=True, help_text='email del usuario', max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='tkyccabecera',
            name='email',
            field=models.TextField(blank=True, help_text='email del usuario', max_length=240, null=True),
        ),
    ]
