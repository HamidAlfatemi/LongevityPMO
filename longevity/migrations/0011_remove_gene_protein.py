# Generated by Django 4.2.1 on 2023-11-08 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('longevity', '0010_alter_gsgene_generole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gene',
            name='protein',
        ),
    ]
