# Generated by Django 4.2.1 on 2023-11-22 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('longevity', '0012_alter_gsgene_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='hallmark',
        ),
    ]
