# Generated by Django 4.2.1 on 2024-10-04 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('longevity', '0037_service_servot'),
    ]

    operations = [
        migrations.CreateModel(
            name='drawbackproject',
            fields=[
                ('dp_id', models.AutoField(primary_key=True, serialize=False)),
                ('dprelation', models.IntegerField(blank=True, choices=[(1, 'Bottleneck - Drawback is slowing down the project'), (2, 'Barrier - Drawback has hold the project'), (3, 'Risk - Drawback is causing risk'), (4, 'Expense: Drawback is raising the expenses'), (5, 'Subject - Project is initiated to solve or alleviate the drawback problem')], db_column='dprelation', null=True)),
                ('drawback', models.ForeignKey(blank=True, db_column='drawback_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='longevity.drawback')),
                ('project', models.ForeignKey(blank=True, db_column='Project_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='longevity.project')),
            ],
            options={
                'db_table': 'drawbackproject',
            },
        ),
    ]
