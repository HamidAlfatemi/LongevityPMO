# Generated by Django 4.2.1 on 2023-11-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('longevity', '0014_concept_openproblem_relation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='ctitle',
            field=models.CharField(blank=True, db_column='ctitle', max_length=200, null=True),
        ),
    ]
