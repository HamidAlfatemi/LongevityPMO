# Generated by Django 4.2.1 on 2023-11-06 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('longevity', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acperson',
            name='ac',
        ),
    ]
