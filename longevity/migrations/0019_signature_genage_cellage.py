# Generated by Django 4.2.1 on 2023-11-29 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('longevity', '0018_remove_genage_gene_remove_signature_gene_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('sig_id', models.AutoField(db_column='Sig_id', primary_key=True, serialize=False)),
                ('sigsymbol', models.CharField(blank=True, db_column='SigSymbol', max_length=10, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=130, null=True)),
                ('expression', models.CharField(blank=True, db_column='Expression', max_length=15, null=True)),
                ('otherdatabases', models.CharField(blank=True, db_column='OtherDatabases', max_length=30, null=True)),
                ('cellage_id', models.BigIntegerField(blank=True, db_column='CellAge_ID', null=True)),
                ('sig_entrez_id', models.BigIntegerField(blank=True, db_column='Sig_Entrez_id', null=True)),
                ('total', models.IntegerField(blank=True, db_column='Total', null=True)),
                ('p_value', models.DecimalField(blank=True, db_column='P_Value', decimal_places=10, max_digits=12, null=True)),
                ('gene', models.ForeignKey(blank=True, db_column='gene_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='longevity.gene')),
            ],
            options={
                'db_table': 'signature',
                'db_table_comment': 'Genes that are either over-expressed or under-expressed duri',
            },
        ),
        migrations.CreateModel(
            name='Genage',
            fields=[
                ('geag_id', models.AutoField(db_column='GeAg_id', primary_key=True, serialize=False)),
                ('genageid', models.BigIntegerField(blank=True, db_column='GenAgeID', null=True)),
                ('gagenename', models.CharField(blank=True, db_column='GAGeneName', max_length=130, null=True)),
                ('gaentrezid', models.BigIntegerField(blank=True, db_column='GAEntrezID', null=True)),
                ('gagenesymbol', models.TextField(blank=True, db_column='GAGeneSymbol', null=True)),
                ('uniport', models.CharField(blank=True, db_column='Uniport', max_length=20, null=True)),
                ('why', models.CharField(blank=True, db_column='Why', max_length=50, null=True)),
                ('gene', models.ForeignKey(blank=True, db_column='gene_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='longevity.gene')),
            ],
            options={
                'db_table': 'genage',
            },
        ),
        migrations.CreateModel(
            name='Cellage',
            fields=[
                ('ceag_id', models.AutoField(db_column='CeAg_id', primary_key=True, serialize=False)),
                ('hagrid', models.BigIntegerField(blank=True, null=True)),
                ('genesymbol', models.CharField(blank=True, db_column='GeneSymbol', max_length=10, null=True)),
                ('hgncid', models.BigIntegerField(blank=True, null=True)),
                ('entrezid', models.BigIntegerField(blank=True, db_column='entrezID', null=True)),
                ('organism', models.CharField(blank=True, max_length=10, null=True)),
                ('cancer_type', models.CharField(blank=True, max_length=3, null=True)),
                ('senescence_effect', models.CharField(blank=True, max_length=10, null=True)),
                ('cadescription', models.TextField(blank=True, db_column='CADescription', null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('method', models.CharField(blank=True, db_column='Method', max_length=25, null=True)),
                ('celltypes', models.CharField(blank=True, db_column='CellTypes', max_length=140, null=True)),
                ('celllines', models.CharField(blank=True, db_column='CellLines', max_length=140, null=True)),
                ('senescencetype', models.CharField(blank=True, db_column='SenescenceType', max_length=30, null=True)),
                ('gene', models.ForeignKey(blank=True, db_column='gene_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='longevity.gene')),
            ],
            options={
                'db_table': 'cellage',
                'db_table_comment': 'Genes associated with cellular senescence based on genetic m',
            },
        ),
    ]
