# Generated by Django 4.2.1 on 2024-02-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('longevity', '0028_node_adsens_node_adspec'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='posnx',
            field=models.DecimalField(blank=True, db_column='posnx', decimal_places=4, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='posny',
            field=models.DecimalField(blank=True, db_column='posny', decimal_places=4, max_digits=6, null=True),
        ),
    ]
