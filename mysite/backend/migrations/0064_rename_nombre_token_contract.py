# Generated by Django 4.0.4 on 2023-02-07 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0063_alter_token_coin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='nombre',
            new_name='contract',
        ),
    ]
