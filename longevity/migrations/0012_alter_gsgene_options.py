# Generated by Django 4.2.1 on 2023-11-08 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('longevity', '0011_remove_gene_protein'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gsgene',
            options={'ordering': ['gs__gstitle', 'gene__gsymbol']},
        ),
    ]
