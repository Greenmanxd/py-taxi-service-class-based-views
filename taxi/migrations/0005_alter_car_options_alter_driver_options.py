# Generated by Django 4.1 on 2023-01-25 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_alter_manufacturer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'default_related_name': 'cars'},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'default_related_name': 'drivers', 'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
    ]