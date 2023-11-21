from django.db import models

class AcPerson(models.Model):
    acp_id = models.AutoField(db_column='ACP_id', primary_key=True, serialize=True)  # Field name made lowercase.
    ac = models.ForeignKey('Agingclock', models.DO_NOTHING, db_column='AC_id', blank=True, null=True)  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_id', blank=True, null=True)  # Field name made lowercase.
    acdate = models.DateField(db_column='ACDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ac_person'


class Agingclock(models.Model):
    ac_id = models.AutoField(db_column='AC_id', primary_key=True, serialize=True)  # Field name made lowercase.
    actitle = models.CharField(db_column='ACTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    acdesc = models.TextField(db_column='ACDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'agingclock'


class Author(models.Model):
    author_id = models.AutoField(db_column='Author_id', primary_key=True, serialize=True)  # Field name made lowercase.
    role = models.IntegerField(db_column='Role', blank=True, null=True)  # Field name made lowercase.
    affiliation_id = models.BigIntegerField(db_column='Affiliation_id', blank=True, null=True)  # Field name made lowercase.
    authordesc = models.TextField(db_column='AuthorDesc', blank=True, null=True)  # Field name made lowercase.
    lit = models.ForeignKey('Literature', models.DO_NOTHING, db_column='Lit_id', blank=True, null=True)  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'author'


class Biomarker(models.Model):
    bm_id = models.AutoField(db_column='BM_id', primary_key=True, serialize=True)  # Field name made lowercase.
    unit = models.ForeignKey('Unit', models.DO_NOTHING, blank=True, null=True)
    bmtitle = models.CharField(db_column='BMTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    upper_limit = models.DecimalField(db_column='Upper_limit', max_digits=9, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lower_limit = models.DecimalField(db_column='Lower_limit', max_digits=9, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bmdesc = models.TextField(db_column='BMDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'biomarker'


class Cellage(models.Model):
    ceag_id = models.AutoField(db_column='CeAg_id', primary_key=True, serialize=True)  # Field name made lowercase.
    hagrid = models.BigIntegerField(blank=True, null=True)
    genesymbol = models.CharField(db_column='GeneSymbol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hgncid = models.BigIntegerField(blank=True, null=True)
    entrezid = models.BigIntegerField(db_column='entrezID', blank=True, null=True)  # Field name made lowercase.
    organism = models.CharField(max_length=10, blank=True, null=True)
    cancer_type = models.CharField(max_length=3, blank=True, null=True)
    senescence_effect = models.CharField(max_length=10, blank=True, null=True)
    cadescription = models.TextField(db_column='CADescription', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(blank=True, null=True)
    gene = models.ForeignKey('Gene', models.DO_NOTHING, db_column='gene_id', blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=25, blank=True, null=True)  # Field name made lowercase.
    celltypes = models.CharField(db_column='CellTypes', max_length=140, blank=True, null=True)  # Field name made lowercase.
    celllines = models.CharField(db_column='CellLines', max_length=140, blank=True, null=True)  # Field name made lowercase.
    senescencetype = models.CharField(db_column='SenescenceType', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'cellage'
        db_table_comment = 'Genes associated with cellular senescence based on genetic m'


class Cellenteragent(models.Model):
    agent_id = models.AutoField(db_column='Agent_id', primary_key=True, serialize=True)  # Field name made lowercase.
    agenttitle = models.TextField(db_column='AgentTitle', blank=True, null=True)  # Field name made lowercase.
    agentdesc = models.TextField(db_column='AgentDesc', blank=True, null=True)  # Field name made lowercase.
    entrancetype = models.IntegerField(db_column='EntranceType', blank=True, null=True)  # Field name made lowercase.
    receptor = models.TextField(db_column='Receptor', blank=True, null=True)  # Field name made lowercase.
    class Meta:

        db_table = 'cellenteragent'


class Contactinfo(models.Model):
    ci_id = models.AutoField(db_column='CI_id', primary_key=True, serialize=True)  # Field name made lowercase.
    conttype = models.IntegerField(db_column='ContType', blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_id', blank=True, null=True)  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_id', blank=True, null=True)  # Field name made lowercase.
    lit = models.ForeignKey('Literature', models.DO_NOTHING, db_column='Lit_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'contactinfo'


class ConvDiagt(models.Model):
    cdt_id = models.AutoField(primary_key=True, serialize=True)
    diagnose = models.ForeignKey('Diagnostictest', models.DO_NOTHING, db_column='Diagnose_id')  # Field name made lowercase.
    conv = models.ForeignKey('Convenience', models.DO_NOTHING, db_column='Conv_id')  # Field name made lowercase.

    class Meta:
        db_table = 'conv_diagt'


class ConvTre(models.Model):
    ct_id = models.AutoField(primary_key=True, serialize=True)
    treatment = models.ForeignKey('Treatment', models.DO_NOTHING, db_column='Treatment_id')  # Field name made lowercase.
    conv = models.ForeignKey('Convenience', models.DO_NOTHING, db_column='Conv_id')  # Field name made lowercase.
    def __str__(self):
        return  f"{self.treatment.treattitle} - {self.conv.convtitle}"

    class Meta:
        db_table = 'conv_tre'


class Convenience(models.Model):
    conv_id = models.AutoField(db_column='Conv_id', primary_key=True, serialize=True)  # Field name made lowercase.
    convtitle = models.CharField(db_column='ConvTitle', max_length=60, blank=True, null=True)  # Field name made lowercase.
    convdesc = models.TextField(db_column='ConvDesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.convtitle

    class Meta:
        db_table = 'convenience'


class Costanalysis(models.Model):
    cost_id = models.AutoField(db_column='Cost_id', primary_key=True, serialize=True)  # Field name made lowercase.
    costitem = models.TextField(db_column='CostItem', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ni = models.ForeignKey('NodeIntervention', models.DO_NOTHING, db_column='NI_id', blank=True, null=True)  # Field name made lowercase.
    np = models.ForeignKey('Nanoparticle', models.DO_NOTHING, db_column='NP_id', blank=True, null=True)  # Field name made lowercase.
    parent_c = models.ForeignKey('self', models.DO_NOTHING, db_column='Parent_c_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'costanalysis'


class Country(models.Model):
    country_id = models.AutoField(db_column='Country_id', primary_key=True, serialize=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'country'


class Ddstep(models.Model):
    step_id = models.AutoField(db_column='Step_id', primary_key=True, serialize=True)  # Field name made lowercase.
    ddstitle = models.CharField(db_column='DDSTitle', max_length=60, blank=True, null=True)  # Field name made lowercase.
    p_step = models.ForeignKey('self', models.DO_NOTHING, db_column='P_Step_id', blank=True, null=True)  # Field name made lowercase.
    step = models.IntegerField(db_column='Step', blank=True, null=True)
    medication = models.IntegerField(db_column='Medication', blank=True, null=True)  # Field name made lowercase.
    nonmedication = models.IntegerField(db_column='NonMedication', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return f"{self.step} - {self.ddstitle}"

    class Meta:
        db_table = 'ddstep'
        ordering = ['step']


class DiagnoseDt(models.Model):
    ddt_id = models.AutoField(primary_key=True, serialize=True)
    diagnosis = models.ForeignKey('Diagnosis', models.DO_NOTHING, db_column='diagnosis_id')  # Field name made lowercase.
    diagnose = models.ForeignKey('Diagnostictest', models.DO_NOTHING, db_column='Diagnose_id')  # Field name made lowercase.

    class Meta:
        db_table = 'diagnose_dt'


class Diagnosis(models.Model):
    diagnosis_id = models.AutoField(db_column='diagnosis_id', primary_key=True, serialize=True)  # Field name made lowercase.
#    node = models.ForeignKey('Node', models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.
    diagnosis = models.CharField(db_column='diagnosis', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nddesc = models.TextField(db_column='NDDesc', blank=True, null=True)  # Field name made lowercase.
    goldstandard = models.IntegerField(db_column='GoldStandard', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.diagnosis

    class Meta:
        db_table = 'diagnosis'


class DiagnosisBm(models.Model):
    dbm_id = models.AutoField(db_column='DBM_id', primary_key=True, serialize=True)  # Field name made lowercase.
    dbmdesc = models.TextField(db_column='DBMDesc', blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.ForeignKey(Diagnosis, models.DO_NOTHING, db_column='diagnosis_id', blank=True, null=True)  # Field name made lowercase.
    bm = models.ForeignKey(Biomarker, models.DO_NOTHING, db_column='BM_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'diagnosis_bm'


class Diagnostictest(models.Model):
    diagnose_id = models.AutoField(db_column='Diagnose_id', primary_key=True, serialize=True)  # Field name made lowercase.
    diagtitle = models.CharField(db_column='DiagTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diagdesc = models.TextField(db_column='DiagDesc', blank=True, null=True)  # Field name made lowercase.
    sensitivity = models.DecimalField(db_column='Sensitivity', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dtspecificity = models.DecimalField(db_column='DTSpecificity', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'diagnostictest'


class Drawbacktype(models.Model):
    dbt_id = models.AutoField(db_column='DBT_id', primary_key=True, serialize=True)  # Field name made lowercase.
    dbttitle = models.CharField(db_column='DBTTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbtdesc = models.TextField(db_column='DBTDesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.dbtitle

    class Meta:
        db_table = 'drawbacktype'


class Drawback(models.Model):
    drawback_id = models.AutoField(db_column='DrawBack_id', primary_key=True, serialize=True)  # Field name made lowercase.
    #intervention = models.ForeignKey('Intervention', models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.
    #diagnose = models.ForeignKey(Diagnostictest, models.DO_NOTHING, db_column='Diagnose_id')  # Field name made lowercase.
    dbtitle = models.CharField(db_column='DBTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dbdesc = models.TextField(db_column='DBDesc', blank=True, null=True)  # Field name made lowercase.
    #project = models.ForeignKey(Project, models.DO_NOTHING, db_column='Project_id')  # Field name made lowercase.
    dbt = models.ForeignKey(Drawbacktype, models.DO_NOTHING, db_column='DBT_id', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.dbtitle

    class Meta:
        db_table = 'drawback'


class DiagnoseDrawback(models.Model):
    ddb_id = models.AutoField(db_column='ddb_id', primary_key=True, serialize=True)  # Field name made lowercase.
    diagnose = models.ForeignKey(Diagnostictest, models.DO_NOTHING, db_column='Diagnose_id')  # Field name made lowercase.
    drawback = models.ForeignKey(Drawback, models.DO_NOTHING, db_column='Drawback_id')  # Field name made lowercase.
    def __str__(self):
        return  f"{self.diagnose.diagtitle} - {self.drawback.dbtitle}"

    class Meta:
        db_table = 'diagnose_drawback'


class Drug(models.Model):
    drug_id = models.AutoField(db_column='Drug_id', primary_key=True, serialize=True)  # Field name made lowercase.
    drugname = models.TextField(db_column='DrugName', blank=True, null=True)  # Field name made lowercase.
    genericname = models.TextField(db_column='GenericName', blank=True, null=True)  # Field name made lowercase.
    drugdesc = models.TextField(db_column='DrugDesc', blank=True, null=True)  # Field name made lowercase.
    drugtype = models.IntegerField(db_column='DrugType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'drug'


class DrugNp(models.Model):
    dnp_id = models.AutoField(primary_key=True, serialize=True)
    np = models.ForeignKey('Nanoparticle', models.DO_NOTHING, db_column='NP_id')  # Field name made lowercase.
    drug = models.ForeignKey(Drug, models.DO_NOTHING, db_column='Drug_id')  # Field name made lowercase.

    class Meta:
        db_table = 'drug_np'


class Drugage(models.Model):
    da_id = models.AutoField(primary_key=True, serialize=True)
    drag_id = models.BigIntegerField(db_column='DrAg_id')  # Field name made lowercase.
    drug = models.ForeignKey(Drug, models.DO_NOTHING, db_column='Drug_id', blank=True, null=True)  # Field name made lowercase.
    formulation = models.TextField(db_column='Formulation', blank=True, null=True)  # Field name made lowercase.
    species = models.TextField(db_column='Species', blank=True, null=True)  # Field name made lowercase.
    lifespanc = models.TextField(db_column='LifespanC', blank=True, null=True)  # Field name made lowercase.
    maxlifspan = models.TextField(db_column='MaxLifspan', blank=True, null=True)  # Field name made lowercase.
    strain = models.TextField(db_column='Strain', blank=True, null=True)  # Field name made lowercase.
    dosage = models.TextField(db_column='Dosage', blank=True, null=True)  # Field name made lowercase.
    significant = models.IntegerField(db_column='Significant', blank=True, null=True)  # Field name made lowercase.
    reference = models.TextField(db_column='Reference', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'drugage'


class Drugbank(models.Model):
    dbd_id = models.AutoField(primary_key=True, serialize=True)
    drba_id = models.BigIntegerField(db_column='DrBa_id')  # Field name made lowercase.
    drug = models.ForeignKey(Drug, models.DO_NOTHING, db_column='Drug_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'drugbank'


# class DtypeDrawback(models.Model):
    # dtdb_id = models.AutoField(primary_key=True, serialize=True)
    # drawback = models.ForeignKey(Drawback, models.DO_NOTHING, db_column='DrawBack_id')  # Field name made lowercase.
    # dbt = models.ForeignKey(Drawbacktype, models.DO_NOTHING, db_column='DBT_id')  # Field name made lowercase.

    # class Meta:
        # db_table = 'dtype_drawback'


class Dye(models.Model):
    dye_id = models.AutoField(db_column='Dye_id', primary_key=True, serialize=True)  # Field name made lowercase.
    dyetitle = models.TextField(db_column='DyeTitle', blank=True, null=True)  # Field name made lowercase.
    dyedesc = models.TextField(db_column='DyeDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'dye'


class DyeNp(models.Model):
    dnp_id = models.AutoField(primary_key=True, serialize=True)
    np = models.ForeignKey('Nanoparticle', models.DO_NOTHING, db_column='NP_id')  # Field name made lowercase.
    dye = models.ForeignKey(Dye, models.DO_NOTHING, db_column='Dye_id')  # Field name made lowercase.

    class Meta:
        db_table = 'dye_np'

class Edge(models.Model):
    edge_id = models.AutoField(db_column='Edge_id', primary_key=True, serialize=True)  # Field name made lowercase.
    begin = models.ForeignKey('Node', models.DO_NOTHING, db_column='Begin_id')  # Field name made lowercase.
    end = models.ForeignKey('Node', models.DO_NOTHING, db_column='End_id', related_name='edge_end_set')  # Field name made lowercase.
    edgeshape = models.IntegerField(db_column='EdgeShape', blank=True, null=True)  # Field name made lowercase.
    # 1- Causal Sequence of Events or Enhancement
    # 2- Very Important Pathway
    # 3- Movement, Transport, or Flow of things
    color = models.IntegerField(db_column='Color', blank=True, null=True)  # Field name made lowercase.
    # Color integer codes are the same as in Node
    edgetype = models.IntegerField(db_column='EdgeType', blank=True, null=True)  # Field name made lowercase.
    # 0- Enhancement of Pathway or Process
    # 1- Beneficial Inhibition of Pathway or Process
    # 2- Harmful Inhibition of Pathway or Process
    # 3- Inhibition of Pathway or Process, benefit or harm depends on situation
    edgedesc = models.TextField(db_column='EdgeDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'edge'

class EdgeLiterature(models.Model):
    el_id = models.AutoField(primary_key=True, serialize=True)
    lit = models.ForeignKey('Literature', models.DO_NOTHING, db_column='Lit_id')  # Field name made lowercase.
    edge = models.ForeignKey(Edge, models.DO_NOTHING, db_column='Edge_id')  # Field name made lowercase.

    class Meta:
        db_table = 'edge_literature'


class EdgeSbpathway(models.Model):
    es_id = models.AutoField(primary_key=True, serialize=True)
    sbp = models.ForeignKey('Sbpathway', models.DO_NOTHING, db_column='SBP_id')  # Field name made lowercase.
    edge = models.ForeignKey(Edge, models.DO_NOTHING, db_column='Edge_id')  # Field name made lowercase.

    class Meta:
        db_table = 'edge_sbpathway'


class Education(models.Model):
    edu_id = models.AutoField(db_column='Edu_id', primary_key=True, serialize=True)  # Field name made lowercase.
    edudegree = models.IntegerField(db_column='EduDegree', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'education'


class Externalfactor(models.Model):
    ef_id = models.AutoField(db_column='EF_id', primary_key=True, serialize=True)  # Field name made lowercase.
    eftype = models.IntegerField(db_column='EFType', blank=True, null=True)  # Field name made lowercase.
    efdesc = models.TextField(db_column='EFDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'externalfactor'


class ExtfactNp(models.Model):
    efnp_id = models.AutoField(primary_key=True, serialize=True)
    np = models.ForeignKey('Nanoparticle', models.DO_NOTHING, db_column='NP_id')  # Field name made lowercase.
    ef = models.ForeignKey(Externalfactor, models.DO_NOTHING, db_column='EF_id')  # Field name made lowercase.

    class Meta:
        db_table = 'extfact_np'


class Facility(models.Model):
    facil_id = models.AutoField(db_column='Facil_id', primary_key=True, serialize=True)  # Field name made lowercase.
    facilitytitle = models.CharField(db_column='FacilityTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    facilitydesc = models.TextField(db_column='FacilityDesc', blank=True, null=True)  # Field name made lowercase.
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'facility'


class Field(models.Model):
    field_id = models.AutoField(db_column='Field_id', primary_key=True, serialize=True)  # Field name made lowercase.
    fieldtitle = models.CharField(db_column='FieldTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    engagement = models.IntegerField(db_column='Engagement', blank=True, null=True)  # Field name made lowercase.
    fielddesc = models.TextField(db_column='FieldDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'field'


class FieldEducation(models.Model):
    fe_id = models.AutoField(primary_key=True, serialize=True)
    edu = models.ForeignKey(Education, models.DO_NOTHING, db_column='Edu_id')  # Field name made lowercase.
    field = models.ForeignKey(Field, models.DO_NOTHING, db_column='Field_id')  # Field name made lowercase.

    class Meta:
        db_table = 'field_education'


class FieldOrganization(models.Model):
    fo_id = models.AutoField(primary_key=True, serialize=True)
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_id')  # Field name made lowercase.
    field = models.ForeignKey(Field, models.DO_NOTHING, db_column='Field_id')  # Field name made lowercase.

    class Meta:
        db_table = 'field_organization'


class Genage(models.Model):
    geag_id = models.AutoField(db_column='GeAg_id', primary_key=True, serialize=True)  # Field name made lowercase.
    genageid = models.BigIntegerField(db_column='GenAgeID', blank=True, null=True)  # Field name made lowercase.
    gagenename = models.CharField(db_column='GAGeneName', max_length=130, blank=True, null=True)  # Field name made lowercase.
    gaentrezid = models.BigIntegerField(db_column='GAEntrezID', blank=True, null=True)  # Field name made lowercase.
    gagenesymbol = models.TextField(db_column='GAGeneSymbol', blank=True, null=True)  # Field name made lowercase.
    uniport = models.CharField(db_column='Uniport', max_length=20, blank=True, null=True)  # Field name made lowercase.
    why = models.CharField(db_column='Why', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gene = models.ForeignKey('Gene', models.DO_NOTHING, db_column='gene_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'genage'


class Gene(models.Model):
    gene_id = models.AutoField(db_column='gene_id', primary_key=True, serialize=True)  # Field name made lowercase.
    gsymbol = models.CharField(db_column='Gsymbol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genename = models.CharField(db_column='GeneName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    #protein = models.CharField(db_column='protein', max_length=60, blank=True, null=True)  # Field name made lowercase.
    gsignificant = models.IntegerField(db_column='GSignificant', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.gsymbol

    class Meta:
        db_table = 'gene'
        ordering = ['gsymbol']


class IcfParameter(models.Model):
    icfp_id = models.AutoField(primary_key=True, serialize=True)
    parameter = models.ForeignKey('Parameter', models.DO_NOTHING, db_column='Parameter_id')  # Field name made lowercase.
    icf = models.ForeignKey('InterventionCf', models.DO_NOTHING, db_column='ICF_id')  # Field name made lowercase.

    class Meta:
        db_table = 'icf_parameter'


class Image(models.Model):
    imag_id = models.AutoField(db_column='Imag_id', primary_key=True, serialize=True)  # Field name made lowercase.
    pdt = models.ForeignKey('PersDiagtest', models.DO_NOTHING, db_column='PDT_id', blank=True, null=True)  # Field name made lowercase.
    mr = models.ForeignKey('Medicalrecord', models.DO_NOTHING, db_column='MR_id', blank=True, null=True)  # Field name made lowercase.
    dimage = models.CharField(db_column='DImage', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dfile = models.CharField(db_column='DFile', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'image'


class Improvement(models.Model):
    impr_id = models.AutoField(db_column='Impr_id', primary_key=True, serialize=True)  # Field name made lowercase.
    avgchange = models.DecimalField(db_column='AvgChange', max_digits=9, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ni = models.ForeignKey('NodeIntervention', models.DO_NOTHING, db_column='NI_id', blank=True, null=True)  # Field name made lowercase.
    bm = models.ForeignKey(Biomarker, models.DO_NOTHING, db_column='BM_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'improvement'


class Intellectualproperty(models.Model):
    ip_id = models.AutoField(db_column='IP_id', primary_key=True, serialize=True)  # Field name made lowercase.
    iptitle = models.CharField(db_column='IPTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    patentnumber = models.IntegerField(db_column='PatentNumber', blank=True, null=True)  # Field name made lowercase.
    ipdate = models.DateField(db_column='IPDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'intellectualproperty'


class Intervention(models.Model):
    intervention_id = models.AutoField(db_column='Intervention_id', primary_key=True, serialize=True)  # Field name made lowercase.
    step = models.ForeignKey(Ddstep, models.DO_NOTHING, db_column='Step_id', blank=True, null=True)  # Field name made lowercase.
    interventiontitle = models.CharField(db_column='InterventionTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    interventiondesc = models.TextField(db_column='InterventionDesc', blank=True, null=True)  # Field name made lowercase.
    materialcosts = models.FloatField(db_column='MaterialCosts', blank=True, null=True)  # Field name made lowercase.
    processcosts = models.FloatField(db_column='ProcessCosts', blank=True, null=True)  # Field name made lowercase.
    costeffectiveness = models.IntegerField(db_column='CostEffectiveness', blank=True, null=True)  # Field name made lowercase.
    compare_factor = models.FloatField(db_column='Compare_Factor', blank=True, null=True)  # Field name made lowercase.
    intoutput = models.IntegerField(db_column='IntOutput', blank=True, null=True)  # Field name made lowercase.
    # 1- Alleviation of Symptoms
    # 2- Slow down
    # 3- Stop progress
    # 4- Cure and control
    # 5- Rejuvenation
    # 6- Prevention
    # 7- Life Style
    comb_n = models.ForeignKey('self', models.DO_NOTHING, db_column='Comb_N_id', blank=True, null=True)  # Field name made lowercase.
    ichi = models.CharField(db_column='ICHI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.interventiontitle
    class Meta:

        db_table = 'intervention'


class InterventionCf(models.Model):
    icf_id = models.AutoField(db_column='ICF_id', primary_key=True, serialize=True)  # Field name made lowercase.
    f_min = models.FloatField(db_column='F_min', blank=True, null=True)  # Field name made lowercase.
    f_max = models.FloatField(db_column='F_max', blank=True, null=True)  # Field name made lowercase.
    f_weight = models.FloatField(db_column='F_weight', blank=True, null=True)  # Field name made lowercase.
    f_unit = models.CharField(db_column='F_unit', max_length=20, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.

    class Meta:
        db_table = 'intervention_cf'


class InterventionDrawback(models.Model):
    idb_id = models.AutoField(db_column='idb_id', primary_key=True, serialize=True)  # Field name made lowercase.
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.
    drawback = models.ForeignKey(Drawback, models.DO_NOTHING, db_column='Drawback_id')  # Field name made lowercase.
    def __str__(self):
        return  f"{self.intervention.interventiontitle} - {self.drawback.dbtitle}"

    class Meta:
        db_table = 'intervention_drawback'


class InterventionGene(models.Model):
    ig_id = models.AutoField(primary_key=True, serialize=True)
    gene = models.ForeignKey(Gene, models.DO_NOTHING, db_column='gene_id')  # Field name made lowercase.
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.

    class Meta:
        db_table = 'intervention_gene'


class InterventionLiterature(models.Model):
    il_id = models.AutoField(primary_key=True, serialize=True)
    lit = models.ForeignKey('Literature', models.DO_NOTHING, db_column='Lit_id')  # Field name made lowercase.
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.
    def __str__(self):
        return  f"{self.intervention.interventiontitle} - {self.lit.littitle}"

    class Meta:
        db_table = 'intervention_literature'


class InterventionSbp(models.Model):
    is_id = models.AutoField(primary_key=True, serialize=True)
    sbp = models.ForeignKey('Sbpathway', models.DO_NOTHING, db_column='SBP_id')  # Field name made lowercase.
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.

    class Meta:
        db_table = 'intervention_sbp'


class InterventionTarget(models.Model):
    it_id = models.AutoField(primary_key=True, serialize=True)
    target = models.ForeignKey('Target', on_delete=models.CASCADE, db_column='Target_id')  # Add on_delete parameter
    intervention = models.ForeignKey('Intervention', on_delete=models.CASCADE, db_column='Intervention_id')  # Add on_delete parameter
    def __str__(self):
        return f"{self.target.targettitle} - {self.intervention.interventiontitle}"

    class Meta:
        db_table = 'intervention_target'


class Treatment(models.Model):
    treatment_id = models.AutoField(db_column='Treatment_id', primary_key=True, serialize=True)  # Field name made lowercase.
    treattitle = models.CharField(db_column='TreatTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    treatdesc = models.TextField(db_column='TreatDesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return  self.treattitle

    class Meta:
        db_table = 'treatment'


class InterventionTreatment(models.Model):
    it_id = models.AutoField(primary_key=True, serialize=True)
    treatment = models.ForeignKey('Treatment', models.DO_NOTHING, db_column='Treatment_id')  # Field name made lowercase.
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.
    def __str__(self):
        return f"{self.intervention.interventiontitle} - {self.treatment.treattitle}"

    class Meta:
        db_table = 'intervention_treatment'


class InterventionStrategy(models.Model):
    strategy_id = models.AutoField(db_column='Strategy_id', primary_key=True, serialize=True)  # Field name made lowercase.
    strategyname = models.CharField(db_column='StrategyName', max_length=100, blank=True, null=True, db_comment='Gene Therapy\n             Tissue Regeneration\n             Nanotherapy\n             Epigenome Modification')  # Field name made lowercase.
    strtegydesc = models.TextField(db_column='StrtegyDesc', blank=True, null=True)  # Field name made lowercase.
    strategylevel = models.IntegerField(db_column='StrategyLevel', blank=True, null=True)  # Field name made lowercase.
    parent_s = models.ForeignKey('self', models.DO_NOTHING, db_column='Parent_S_id', blank=True, null=True)  # Field name made lowercase.
    medication = models.IntegerField(db_column='Medication', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.strategyname

    class Meta:
        db_table = 'interventionstrategy'


class StrategyDrawback(models.Model):
    sdb_id = models.AutoField(db_column='sdb_id', primary_key=True, serialize=True)  # Field name made lowercase.
    strategy = models.ForeignKey(InterventionStrategy, models.DO_NOTHING, db_column='Strategy_id')  # Field name made lowercase.
    drawback = models.ForeignKey(Drawback, models.DO_NOTHING, db_column='Drawback_id')  # Field name made lowercase.
    def __str__(self):
        return  f"{self.strategy.strategyname} - {self.drawback.dbtitle}"

    class Meta:
        db_table = 'strategy_drawback'


class Journal(models.Model):
    journal_id = models.AutoField(db_column='Journal_id', primary_key=True, serialize=True)  # Field name made lowercase.
    journalname = models.CharField(db_column='JournalName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    impactf = models.DecimalField(db_column='ImpactF', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'journal'


class Keyword(models.Model):
    keyword_id = models.AutoField(db_column='Keyword_id', primary_key=True, serialize=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='Keyword', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'keyword'


class Ligandtype(models.Model):
    lt_id = models.AutoField(db_column='LT_id', primary_key=True, serialize=True)  # Field name made lowercase.
    lttitle = models.TextField(db_column='LTTitle', blank=True, null=True)  # Field name made lowercase.
    ltdesc = models.TextField(db_column='LTDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ligandtype'
#        db_table_comment = 'Peptide chain\nAntibody\nChemical\n...'


class Linker(models.Model):
    linker_id = models.AutoField(db_column='Linker_id', primary_key=True, serialize=True)  # Field name made lowercase.
    linkertitle = models.TextField(db_column='LinkerTitle', blank=True, null=True)  # Field name made lowercase.
    linkerdesc = models.TextField(db_column='LinkerDesc')  # Field name made lowercase.

    class Meta:
        db_table = 'linker'


class Literature(models.Model):
    lit_id = models.AutoField(db_column='Lit_id', primary_key=True, serialize=True)  # Field name made lowercase.
    doi = models.CharField(db_column='DOI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    littitle = models.TextField(db_column='LitTitle', blank=True, null=True)  # Field name made lowercase.
    relevance = models.DecimalField(db_column='Relevance', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    publishyear = models.DecimalField(db_column='PublishYear', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    publishmonth = models.DecimalField(db_column='PublishMonth', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    citation = models.TextField(db_column='Citation', blank=True, null=True)  # Field name made lowercase.
    isbn = models.TextField(db_column='ISBN', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.littitle

    class Meta:
        db_table = 'literature'


class LiteratureJournal(models.Model):
    lj_id = models.AutoField(primary_key=True, serialize=True)
    journal = models.ForeignKey(Journal, models.DO_NOTHING, db_column='Journal_id')  # Field name made lowercase.
    lit = models.ForeignKey(Literature, models.DO_NOTHING, db_column='Lit_id')  # Field name made lowercase.

    class Meta:
        db_table = 'literature_journal'


class LitType(models.Model):
    lt_id = models.AutoField(primary_key=True, serialize=True)
    ltype = models.ForeignKey('Literaturetype', models.DO_NOTHING, db_column='LType_id')  # Field name made lowercase.
    lit = models.ForeignKey(Literature, models.DO_NOTHING, db_column='Lit_id')  # Field name made lowercase.

    class Meta:
        db_table = 'lit_type'


class Literaturetype(models.Model):
    ltype_id = models.AutoField(db_column='LType_id', primary_key=True, serialize=True)  # Field name made lowercase.
    ltype = models.TextField(db_column='LType', blank=True, null=True) # , db_comment='Theory\n             Approval/Disapproval of a theory\n             Hallmark of Aging\n             Intervention\n             Clinical Trial\n             Meta Analysis\n             Intervention Discovery\n             Review\n             Philosophy')  # Field name made lowercase.
    classdesc = models.TextField(db_column='ClassDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'literaturetype'
#        db_table_comment = 'An Article may be of one type or combination of types\n'


class MatPro(models.Model):
    quantity = models.DecimalField(db_column='Quantity', max_digits=7, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    minquality = models.IntegerField(db_column='MinQuality', blank=True, null=True, db_comment='Minimum quality required')  # Field name made lowercase.
    mp_id = models.AutoField(db_column='MP_id', primary_key=True, serialize=True)  # Field name made lowercase.
    mat = models.ForeignKey('Material', models.DO_NOTHING, db_column='Mat_id', blank=True, null=True)  # Field name made lowercase.
    prot = models.ForeignKey('Protocol', models.DO_NOTHING, db_column='Prot_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'mat_pro'


class Material(models.Model):
    mat_id = models.AutoField(db_column='Mat_id', primary_key=True, serialize=True)  # Field name made lowercase.
    mattitle = models.TextField(db_column='MatTitle', blank=True, null=True)  # Field name made lowercase.
    matdesc = models.TextField(db_column='MatDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'material'


class Medicalrecord(models.Model):
    mr_id = models.AutoField(db_column='MR_id', primary_key=True, serialize=True)  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.
    mrtitle = models.CharField(db_column='MRTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mrtype = models.IntegerField(db_column='MRType', blank=True, null=True)  # Field name made lowercase.
    mrdate = models.DateField(db_column='MRDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'medicalrecord'


class Nanocarrier(models.Model):
    nc_id = models.AutoField(db_column='NC_id', primary_key=True, serialize=True)  # Field name made lowercase.
    nctitle = models.TextField(db_column='NCTitle', blank=True, null=True)  # Field name made lowercase.
    ncdesc = models.TextField(db_column='NCDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'nanocarrier'


class Nanoparticle(models.Model):
    np_id = models.AutoField(db_column='NP_id', primary_key=True, serialize=True)  # Field name made lowercase.
    nc = models.ForeignKey(Nanocarrier, models.DO_NOTHING, db_column='NC_id', blank=True, null=True)  # Field name made lowercase.
    tl = models.ForeignKey('Targetingligand', models.DO_NOTHING, db_column='TL_id', blank=True, null=True)  # Field name made lowercase.
    agent = models.ForeignKey(Cellenteragent, models.DO_NOTHING, db_column='Agent_id', blank=True, null=True)  # Field name made lowercase.
    linker = models.ForeignKey(Linker, models.DO_NOTHING, db_column='Linker_id', blank=True, null=True)  # Field name made lowercase.
    linkerdesc = models.TextField(db_column='LinkerDesc', blank=True, null=True)  # Field name made lowercase.
    nptitle = models.TextField(db_column='NPTitle', blank=True, null=True)  # Field name made lowercase.
    npdesc = models.TextField(db_column='NPDesc', blank=True, null=True)  # Field name made lowercase.
    shape = models.TextField(db_column='Shape', blank=True, null=True)  # Field name made lowercase.
    dimx = models.DecimalField(db_column='Dimx', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dimy = models.DecimalField(db_column='Dimy', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dimz = models.DecimalField(db_column='Dimz', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    echarge = models.DecimalField(db_column='ECharge', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ecdist = models.TextField(db_column='ECDist', blank=True, null=True)  # Field name made lowercase.
    hydrophobicity = models.TextField(db_column='Hydrophobicity', blank=True, null=True)  # Field name made lowercase.
    immuneresist = models.TextField(db_column='ImmuneResist', blank=True, null=True)  # Field name made lowercase.
    specificity = models.DecimalField(db_column='Specificity', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    efficiency = models.DecimalField(db_column='Efficiency', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    effectspeed = models.TextField(db_column='EffectSpeed', blank=True, null=True)  # Field name made lowercase.
    halflife = models.DecimalField(db_column='HalfLife', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    excretion = models.TextField(db_column='Excretion', blank=True, null=True)  # Field name made lowercase.
    tracked = models.IntegerField(db_column='Tracked', blank=True, null=True)  # Field name made lowercase.
    peg = models.TextField(db_column='PEG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'nanoparticle'

class Node(models.Model):
    node_id = models.IntegerField(db_column='Node_id', primary_key=True, serialize=True)  # Field name made lowercase.
    ref_num = models.CharField(db_column='Ref_num', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nodecaption = models.CharField(db_column='NodeCaption', max_length=254, blank=True, null=True)  # Field name made lowercase.
    nodeshape = models.IntegerField(db_column='NodeShape', blank=True, null=True) # , db_comment='1\tThings: Quantities or Pools of Molecules, Cells, Substances, etc.\n             2\tProcess, Action, Change, or Reaction\n             3\tOrganelle or compartment\n             4\tGradual Accumulation or Increase in Quantity or Mass with Aging\n             5\tGradual Loss or Decrease in Quantity or Mass with Aging\n             6\tExternal Intervention, or Environmental Factors\n             7\tPhysiological Condition (Senescence)')  # Field name made lowercase.
    # 1- Rectangles - Things: Quantities or Pools of Molecules, Cells, Substances, etc.  Or Process, Action, Change, or Reaction  
    # 2- Gradual Accumulation or Increase in Quantity or Mass with Aging  
    # 3- Gradual Loss or Decrease in Quantity or Mass with Aging  
    # 4- Environmental Factors  
    # 5- External Intervention  
    # 6- Physiological Condition (Senescence)  
    # 7- Container   
    dash = models.IntegerField(db_column='Dash', blank=True, null=True)  # Field name made lowercase.
    # 0- continuous
    # 1- dashed
    nodecolor = models.IntegerField(db_column='NodeColor', blank=True, null=True)  # Field name made lowercase.
    # 1- Blue: Genetics, Nucleus, Endoplasmic Reticulum
    # 2- Light Brown (Dark Yellow): Cytoplasmic molecules
    # 3- Light Blue (Cyan): Mitochondria
    # 4- Brown: Extracellular Substances & Structures
    # 5- Pink (Magenta): Controlled Degradation & Turnover
    # 6- Green: Beneficial process or intervention
    # 7- Purple (Violet): Signaling Pathway
    # 8- Red: Damaging Substance or Process
    # 9- Black: Senescence Physiology
    container = models.IntegerField(db_column='Container', blank=True, null=True)  # Field name made lowercase.
    # 1- Tissue, Organ, & Whole Body Physiology & Pathology
    # 2- Whole Cells or Tissues
    # 3- Extracellular Spaces: ECM, Blood Plasma, Lymph, CSF
    # 4- Cytosolic Compartment of the Cell
    # 5- Lysosome – Hydrolysis - for recycling. Accumulation in nonmitotic cells.
    # 6- Macroautophagy
    # 7- Mitochondria in nonmitotic cell
    # 8- Cell Nucleus – Genetics
    # 9- Endoplasmic Reticulum
    # 10- Membrane
    # 11- Secretion
    # 12- External Environment
    # 13- Endoplasmic Reticulum Membrane
    # 14- Cell Nucleus Membrane
    # 15- Mitochondria Membrane
    # 16- Lysosome Membrane
    nodedesc = models.TextField(db_column='NodeDesc', blank=True, null=True)  # Field name made lowercase.
    severity_q = models.DecimalField(db_column='Severity_Q', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    frequency_q = models.DecimalField(db_column='Frequency_Q', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    speed_q = models.DecimalField(db_column='Speed_Q', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    adsens = models.DecimalField(db_column='ADSens', max_digits=6, decimal_places=2, blank=True, null=True, db_comment='Acceptable Diagnosis Sensitivity\n             ')  # Field name made lowercase.
    adspec = models.DecimalField(db_column='ADSpec', max_digits=6, decimal_places=2, blank=True, null=True, db_comment='Acceptable Diagnosis Specificity')  # Field name made lowercase.
    hallmark = models.IntegerField(db_column='Hallmark', blank=True, null=True)  # Field name made lowercase.
    icd11 = models.CharField(db_column='ICD11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return f"{self.ref_num} - {self.nodecaption}"

    class Meta:
        db_table = 'node'
        ordering = ['ref_num']


# class NodeGene(models.Model):
    # ng_id = models.AutoField(primary_key=True, serialize=True)
    # gene = models.ForeignKey(Gene, models.DO_NOTHING, db_column='Gene_id')  # Field name made lowercase.
    # node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.
    # generole = models.IntegerField(db_column='GeneRole', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # db_table = 'node_gene'


class NodeDiagnosis(models.Model):
    nd_id = models.AutoField(primary_key=True, serialize=True)
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.
    diagnosis = models.ForeignKey(Diagnosis, models.DO_NOTHING, db_column='diagnosis_id')  # Field name made lowercase.
    nddesc = models.TextField(db_column='nddesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return f"{self.node.ref_num} - {self.diagnosis.diagnosis}"

    class Meta:
        db_table = 'nodediagnosis'


class GeneSet(models.Model):
    gs_id = models.AutoField(primary_key=True, serialize=True)
    gstitle = models.CharField(db_column='gstitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gsdesc = models.TextField(db_column='gsdesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.gstitle

    class Meta:
        db_table = 'geneset'



class gsgene(models.Model):
    gsg_id = models.AutoField(primary_key=True, serialize=True)
    gs = models.ForeignKey(GeneSet, models.DO_NOTHING, db_column='gs_id')  # Field name made lowercase.
    gene = models.ForeignKey(Gene, models.DO_NOTHING, db_column='gene_id')  # Field name made lowercase.
    generole = models.TextField(db_column='generole', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return f"{self.gs.gstitle} - {self.gene.gsymbol}"

    class Meta:
        db_table = 'gsgene'
        ordering = ['gs__gstitle', 'gene__gsymbol']


class nodegs(models.Model):
    ngs_id = models.AutoField(primary_key=True, serialize=True)
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.
    gs = models.ForeignKey(GeneSet, models.DO_NOTHING, db_column='gs_id')  # Field name made lowercase.
    def __str__(self):
        return f"{self.node.ref_num} - {self.gs.gstitle}"

    class Meta:
        db_table = 'nodegs'


class InteractionType(models.Model):
    it_id = models.AutoField(primary_key=True, serialize=True)
    interaction = models.CharField(db_column='interaction', max_length=30, blank=True, null=True)  # Field name made lowercase.
    typedesc = models.TextField(db_column='typedesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.interaction

    class Meta:
        db_table = 'interactiontype'
    
    
class geneinteraction(models.Model):
    gi_id = models.AutoField(primary_key=True, serialize=True)
    gene1 = models.ForeignKey(Gene, models.DO_NOTHING, db_column='gene1_id', blank=True, null=True)  # Field name made lowercase.
    gene2 = models.ForeignKey(Gene, models.DO_NOTHING, db_column='gene2_id', related_name='geneinteraction_gene2_set', blank=True, null=True)  # Field name made lowercase.
    it = models.ForeignKey(InteractionType, models.DO_NOTHING, db_column='it_id')  # Field name made lowercase.
    def __str__(self):
        return f"{self.gene1.gsymbol} - {self.it.interaction} - {self.gene2.gsymbol}"

    class Meta:
        db_table = 'geneinteraction'


class SAE(models.Model):
    ae_id = models.AutoField(db_column='AE_id', primary_key=True, serialize=True)  # Field name made lowercase.
    aetitle = models.CharField(db_column='AETitle', max_length=40, blank=True, null=True)  # Field name made lowercase.
    aedesc = models.TextField(db_column='AEDesc', blank=True, null=True)  # Field name made lowercase.
    sae = models.IntegerField(db_column='SAE', blank=True, null=True, db_comment='Serious Adverse Event')  # Field name made lowercase.
    SAE_LEVELS = {
        1: 'Results in Death',
        2: 'Is life-threatening',
        3: 'Requires Inpatient Hospitalization or Prolongation of Existing Hospitalization',
        4: 'Results in Persistent or Significant Disability/Incapacity',
        5: 'Impacts Mental Health',
        6: 'Causes Congenital Anomaly/Birth Defect',
        7: 'Requires Medical Intervention but Not Hospitalization',
        8: 'Causes Temporary and Annoying Effects',
        # Add more levels as needed
    }
    def __str__(self):
        sae_category = self.SAE_LEVELS.get(self.sae, '')
        return f"{self.aetitle} - {sae_category}"

    class Meta:
        db_table = 'sae'


class DoseUnit(models.Model):
    unit_id = models.AutoField(db_column='unit_id', primary_key=True, serialize=True)  # Field name made lowercase.
    doseunit = models.CharField(db_column='doseunit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='abbreviation', max_length=20, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.doseunit

    class Meta:
        db_table = 'doseunit'


class InterventionSAE(models.Model):
    isae_id = models.AutoField(primary_key=True, serialize=True)
    intervention = models.ForeignKey('Intervention', models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.
    ae = models.ForeignKey('SAE', models.DO_NOTHING, db_column='AE_id')  # Field name made lowercase.
    isaedesc = models.TextField(db_column='isaedesc', blank=True, null=True)  # Field name made lowercase.
    doselimit = models.DecimalField(db_column='doselimit', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unit = models.ForeignKey(DoseUnit, models.DO_NOTHING, db_column='unit_id', blank=True, null=True)  # Field name made lowercase.
    doseduration = models.IntegerField(db_column='doseduration', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return  f"{self.intervention.interventiontitle} - {self.ae.aetitle}"

    class Meta:
        db_table = 'intervention_sae'


# class SAELiterature(models.Model):
    # sael_id = models.AutoField(primary_key=True, serialize=True)
    # ae = models.ForeignKey('SAE', models.DO_NOTHING, db_column='AE_id')  # Field name made lowercase.
    # lit = models.ForeignKey('Literature', models.DO_NOTHING, db_column='Lit_id')  # Field name made lowercase.
    # def __str__(self):
        # return  f"{self.sae.sae} - self.lit.littitle"

    # class Meta:
        # db_table = 'sae_literature'


class ISAELiterature(models.Model):
    sael_id = models.AutoField(primary_key=True, serialize=True)
    isae = models.ForeignKey('InterventionSAE', models.DO_NOTHING, db_column='isae_id')  # Field name made lowercase.
    lit = models.ForeignKey('Literature', models.DO_NOTHING, db_column='Lit_id')  # Field name made lowercase.
    def __str__(self):
        return  f"{self.isae.intervention.interventiontitle} - {self.isae.ae.aetitle} - {self.lit.littitle}"

    class Meta:
        db_table = 'isae_literature'


class Condition(models.Model):
    cond_id = models.AutoField(primary_key=True, serialize=True)  # Field name made lowercase.
    condtitle = models.CharField(db_column='condtitle', max_length=30, blank=True, null=True)  # Field name made lowercase.
    conddesc = models.TextField(db_column='conddesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.condtitle

    class Meta:
        db_table = 'condition'


class isaecond(models.Model):
    isaec_id = models.AutoField(primary_key=True, serialize=True)
    isae = models.ForeignKey('InterventionSAE', models.DO_NOTHING, db_column='isae_id')  # Field name made lowercase.
    cond = models.ForeignKey('Condition', models.DO_NOTHING, db_column='cond_id')  # Field name made lowercase.
    conditionset = models.IntegerField(db_column='conditionset', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return  f"{self.isae.intervention.interventiontitle} - {self.isae.ae.aetitle} - {self.cond.condtitle}"

    class Meta:
        db_table = 'isae_cond'


class NodeIntervention(models.Model):
    ni_id = models.AutoField(db_column='NI_id', primary_key=True, serialize=True)  # Field name made lowercase.
    node = models.ForeignKey(Node, on_delete=models.CASCADE, db_column='Node_id', blank=True, null=True)  # Field name made lowercase.
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE, db_column='Intervention_id', blank=True, null=True)  # Field name made lowercase.
#    ae = models.ForeignKey(SAE, models.DO_NOTHING, db_column='AE_id', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return f"{self.node.ref_num} - {self.intervention.interventiontitle}"

    class Meta:
        db_table = 'node_intervention'


class NodeKeyword(models.Model):
    nk_id = models.AutoField(primary_key=True, serialize=True)
    keyword = models.ForeignKey(Keyword, models.DO_NOTHING, db_column='Keyword_id')  # Field name made lowercase.
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.

    class Meta:
        db_table = 'node_keyword'


class NodeLiterature(models.Model):
    nl_id = models.AutoField(primary_key=True, serialize=True)
    lit = models.ForeignKey(Literature, models.DO_NOTHING, db_column='Lit_id')  # Field name made lowercase.
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.
    def __str__(self):
        return f"{self.node.ref_num} - {self.lit.littitle}"

    class Meta:
        db_table = 'node_literature'


class NodeSbpathway(models.Model):
    ns_id = models.AutoField(primary_key=True, serialize=True)
    sbp = models.ForeignKey('Sbpathway', models.DO_NOTHING, db_column='SBP_id')  # Field name made lowercase.
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.

    class Meta:
        db_table = 'node_sbpathway'


class NodeSymptom(models.Model):
    ns_id = models.AutoField(db_column='NS_id', primary_key=True, serialize=True)  # Field name made lowercase.
    nsdesc = models.TextField(db_column='NSDesc', blank=True, null=True)  # Field name made lowercase.
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.
    symptom = models.ForeignKey('Symptom', models.DO_NOTHING, db_column='Symptom_id')  # Field name made lowercase.

    class Meta:
        db_table = 'node_symptom'

class NodeTheory(models.Model):
    nt_id = models.AutoField(primary_key=True, serialize=True)
    theory = models.ForeignKey('Theory', models.DO_NOTHING, db_column='Theory_id')  # Field name made lowercase.
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.
    ntdesc = models.TextField(db_column='NTDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'node_theory'

class NpInt(models.Model):
    npi_id = models.AutoField(primary_key=True, serialize=True)
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.
    np = models.ForeignKey(Nanoparticle, models.DO_NOTHING, db_column='NP_id')  # Field name made lowercase.

    class Meta:
        db_table = 'np_int'


class OrgIp(models.Model):
    oi_id = models.AutoField(primary_key=True, serialize=True)
    ip = models.ForeignKey(Intellectualproperty, models.DO_NOTHING, db_column='IP_id')  # Field name made lowercase.
    organization = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Organization_id')  # Field name made lowercase.

    class Meta:
        db_table = 'org_ip'


class OrgOrg(models.Model):
    oo_id = models.AutoField(db_column='OO_id', primary_key=True, serialize=True)  # Field name made lowercase.
    orgrelation = models.TextField(db_column='OrgRelation', blank=True, null=True)  # Field name made lowercase.
    org_id1 = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Org_id1')  # Field name made lowercase.
    org_id2 = models.ForeignKey('Organization', models.DO_NOTHING, db_column='Org_id2', related_name='orgorg_org_id2_set')  # Field name made lowercase.

    class Meta:
        db_table = 'org_org'


class Organization(models.Model):
    organization_id = models.AutoField(db_column='Organization_id', primary_key=True, serialize=True)  # Field name made lowercase.
    ot = models.ForeignKey('Orgtype', models.DO_NOTHING, db_column='OT_id', blank=True, null=True)  # Field name made lowercase.
    orgtitle = models.CharField(db_column='OrgTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    parent_org_id = models.BigIntegerField(db_column='Parent_org_id', blank=True, null=True)  # Field name made lowercase.
    olrole = models.IntegerField(db_column='OLRole', blank=True, null=True)  # Field name made lowercase.
    orgdesc = models.TextField(db_column='OrgDesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.orgtitle

    class Meta:
        db_table = 'organization'


class OrganizationCountry(models.Model):
    oc_id = models.AutoField(primary_key=True, serialize=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_id')  # Field name made lowercase.
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Organization_id')  # Field name made lowercase.

    class Meta:
        db_table = 'organization_country'


class OrganizationPerson(models.Model):
    op_id = models.AutoField(primary_key=True, serialize=True)
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Organization_id')  # Field name made lowercase.

    class Meta:
        db_table = 'organization_person'


class Orgtype(models.Model):
    ot_id = models.AutoField(db_column='OT_id', primary_key=True, serialize=True)  # Field name made lowercase.
    typetitle = models.TextField(db_column='TypeTitle', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'orgtype'
        db_table_comment = '1- Univerity\n2- Faculty - A department of University.\n'


class Parameter(models.Model):
    parameter_id = models.AutoField(db_column='Parameter_id', primary_key=True, serialize=True)  # Field name made lowercase.
    paratitle = models.CharField(db_column='ParaTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paraunit = models.CharField(db_column='ParaUnit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    p_weight = models.FloatField(db_column='P_Weight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'parameter'


class PcBm(models.Model):
    pcbm_id = models.AutoField(db_column='PCBM_id', primary_key=True, serialize=True)  # Field name made lowercase.
    pc = models.ForeignKey('Perscondition', models.DO_NOTHING, db_column='PC_id', blank=True, null=True)  # Field name made lowercase.
    pdt = models.ForeignKey('PersDiagtest', models.DO_NOTHING, db_column='PDT_id', blank=True, null=True)  # Field name made lowercase.
    bm = models.ForeignKey(Biomarker, models.DO_NOTHING, db_column='BM_id', blank=True, null=True)  # Field name made lowercase.
    pcbmvalue = models.DecimalField(db_column='PCBMValue', max_digits=9, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pc_bm'


class PcSymp(models.Model):
    pcs_id = models.AutoField(db_column='PCS_id', primary_key=True, serialize=True)  # Field name made lowercase.
    symptom = models.ForeignKey('Symptom', models.DO_NOTHING, db_column='Symptom_id', blank=True, null=True)  # Field name made lowercase.
    pc = models.ForeignKey('Perscondition', models.DO_NOTHING, db_column='PC_id')  # Field name made lowercase.
    symptomobs = models.TextField(db_column='SymptomObs', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pc_symp'


class PdtDt(models.Model):
    pdtdt_id = models.AutoField(primary_key=True, serialize=True)
    diagnose = models.ForeignKey(Diagnostictest, models.DO_NOTHING, db_column='Diagnose_id')  # Field name made lowercase.
    pdt = models.ForeignKey('PersDiagtest', models.DO_NOTHING, db_column='PDT_id')  # Field name made lowercase.

    class Meta:
        db_table = 'pdt_dt'


class PersDiagtest(models.Model):
    pdt_id = models.AutoField(db_column='PDT_id', primary_key=True, serialize=True)  # Field name made lowercase.
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Organization_id', blank=True, null=True)  # Field name made lowercase.
    visit = models.ForeignKey('Visit', models.DO_NOTHING, db_column='Visit_id', blank=True, null=True)  # Field name made lowercase.
    pdtdate = models.DateField(db_column='PDTDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pers_diagtest'


class PersInt(models.Model):
    pi_id = models.AutoField(db_column='PI_id', primary_key=True, serialize=True)  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.
    visit = models.ForeignKey('Visit', models.DO_NOTHING, db_column='Visit_id', blank=True, null=True)  # Field name made lowercase.
    pidate = models.DateField(db_column='PIDate', blank=True, null=True)  # Field name made lowercase.
    pitime = models.TimeField(db_column='PITime', blank=True, null=True)  # Field name made lowercase.
    pidesc = models.TextField(db_column='PIDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pers_int'
#        db_table_comment = 'A record can be added for every time the drug is consumed.'


class PersPerscond(models.Model):
    ppc_id = models.AutoField(primary_key=True, serialize=True)
    pc = models.ForeignKey('Perscondition', models.DO_NOTHING, db_column='PC_id')  # Field name made lowercase.
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.

    class Meta:
        db_table = 'pers_perscond'


class PersPerstyp(models.Model):
    pp_id = models.AutoField(primary_key=True, serialize=True)
    pt = models.ForeignKey('Perstype', models.DO_NOTHING, db_column='PT_id')  # Field name made lowercase.
    person = models.OneToOneField('Person', models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.

    class Meta:
        db_table = 'pers_perstyp'


class Perscondition(models.Model):
    pc_id = models.AutoField(db_column='PC_id', primary_key=True, serialize=True)  # Field name made lowercase.
    pcdate = models.DateField(db_column='PCDate', blank=True, null=True)  # Field name made lowercase.
    pctime = models.TimeField(db_column='PCTime', blank=True, null=True)  # Field name made lowercase.
    pcondition = models.TextField(db_column='PCondition', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'perscondition'


class PersintInt(models.Model):
    pii_id = models.AutoField(primary_key=True, serialize=True)
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.
    pi = models.ForeignKey(PersInt, models.DO_NOTHING, db_column='PI_id')  # Field name made lowercase.

    class Meta:
        db_table = 'persint_int'


class Person(models.Model):
    person_id = models.AutoField(db_column='Person_id', primary_key=True, serialize=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    persondesc = models.TextField(db_column='PersonDesc', blank=True, null=True)  # Field name made lowercase.
    plrole = models.IntegerField(db_column='PLRole', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'person'
##########################################################################
#########################  Temporarily added   ###########################
##########################################################################

# class Stakeholder(models.Model):
    # sh_id = models.IntegerField(db_column='SH_id', primary_key=True)  # Field name made lowercase.
    # shrole = models.CharField(db_column='SHRole', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # shroledesc = models.TextField(db_column='SHRoleDesc', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'stakeholder'

       
# class PersonStakeholder(models.Model):
    # ps_id = models.IntegerField(db_column='ps_id', primary_key=True)  # Field name made lowercase.
    # sh = models.ForeignKey(Stakeholder, models.DO_NOTHING, db_column='SH_id')  # Field name made lowercase. The composite primary key (SH_id, Person_id) found, that is not supported. The first column is selected.
    # person = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.

    # class Meta:
        # managed = False
        # db_table = 'person_stakeholder'
        # #unique_together = (('sh', 'person'),)

###########################################################################

class PersonCountry(models.Model):
    pc_id = models.AutoField(primary_key=True, serialize=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_id')  # Field name made lowercase.
    person = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.

    class Meta:
        db_table = 'person_country'


class PersonEducation(models.Model):
    pe_id = models.AutoField(primary_key=True, serialize=True)
    edu = models.ForeignKey(Education, models.DO_NOTHING, db_column='Edu_id')  # Field name made lowercase.
    person = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.

    class Meta:
        db_table = 'person_education'


class PersonField(models.Model):
    pf_id = models.AutoField(primary_key=True, serialize=True)
    field = models.OneToOneField(Field, models.DO_NOTHING, db_column='Field_id')  # Field name made lowercase.
    person = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.

    class Meta:
        db_table = 'person_field'


class PersonIp(models.Model):
    pip_id = models.AutoField(primary_key=True, serialize=True)
    ip = models.ForeignKey(Intellectualproperty, models.DO_NOTHING, db_column='IP_id')  # Field name made lowercase.
    person = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.

    class Meta:
        db_table = 'person_ip'


class Perstype(models.Model):
    pt_id = models.AutoField(db_column='PT_id', primary_key=True, serialize=True)  # Field name made lowercase.
    pttitle = models.TextField(db_column='PTTitle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'perstype'
#        db_table_comment = 'Researcher\nMedical Doctor\nSenior\nPatient\n                             '


class Pricelist(models.Model):
    pl_id = models.AutoField(db_column='PL_id', primary_key=True, serialize=True)  # Field name made lowercase.
    mat = models.ForeignKey(Material, models.DO_NOTHING, db_column='Mat_id', blank=True, null=True)  # Field name made lowercase.
    supl = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='Supl_id', blank=True, null=True)  # Field name made lowercase.
    priceitem = models.TextField(db_column='PriceItem', blank=True, null=True)  # Field name made lowercase.
    plquant = models.DecimalField(db_column='PLQuant', max_digits=9, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    plquality = models.IntegerField(db_column='PLQuality', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pricelist'


class ProNp(models.Model):
    pnp_id = models.AutoField(primary_key=True, serialize=True)
    np = models.ForeignKey(Nanoparticle, models.DO_NOTHING, db_column='NP_id')  # Field name made lowercase.
    prot = models.ForeignKey('Protocol', models.DO_NOTHING, db_column='Prot_id')  # Field name made lowercase.

    class Meta:
        db_table = 'pro_np'


class Project(models.Model):
    project_id = models.AutoField(db_column='Project_id', primary_key=True, serialize=True)  # Field name made lowercase.
    #research = models.ForeignKey('Requiredresearch', models.DO_NOTHING, db_column='Research_id', blank=True, null=True)  # Field name made lowercase.
    projtitle = models.CharField(db_column='ProjTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    overallgoal = models.TextField(db_column='overallgoal', blank=True, null=True)  # Field name made lowercase.
    keyobjectives = models.TextField(db_column='keyobjectives', blank=True, null=True)  # Field name made lowercase.
    projectsource = models.IntegerField(db_column='ProjectSource', blank=True, null=True)  # Field name made lowercase.
    program = models.ForeignKey('self', models.DO_NOTHING, db_column='Program_id', blank=True, null=True)  # Field name made lowercase.
    projdesc = models.TextField(db_column='ProjDesc', blank=True, null=True)  # Field name made lowercase.
    #proj_subj = models.IntegerField(db_column='Proj_Subj', blank=True, null=True)  # Field name made lowercase.
    projstatus = models.IntegerField(db_column='ProjStatus', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.projtitle

    class Meta:
        db_table = 'project'


class Subject(models.Model):
    subject_id = models.AutoField(db_column='Subject_id', primary_key=True, serialize=True)  # Field name made lowercase.
    subjecttitle = models.CharField(db_column='SubjectTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subjdesc = models.TextField(db_column='SubjDesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.subjecttitle

    class Meta:
        db_table = 'subject'


class ProjectSubject(models.Model):
    ps_id = models.AutoField(primary_key=True, serialize=True)
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='Project_id', blank=True, null=True)  # Field name made lowercase.
    Subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column='Subject_id', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return  f"{self.project.projtitle} - {self.Subject.subjecttitle}"

    class Meta:
        db_table = 'project_subject'


class ProjectIntervention(models.Model):
    pi_id = models.AutoField(primary_key=True, serialize=True)
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id', blank=True, null=True)  # Field name made lowercase.
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='Project_id', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return  f"{self.project.projtitle} - {self.intervention.interventiontitle}"

    class Meta:
        db_table = 'project_intervention'

class ProjectDiagnosis(models.Model):
    pd_id = models.AutoField(primary_key=True, serialize=True)
    diagnosis = models.ForeignKey(Diagnosis, models.DO_NOTHING, db_column='diagnosis_id', blank=True, null=True)  # Field name made lowercase.
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='Project_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'project_diagnosis'

class ProjectTheory(models.Model):
    pt_id = models.AutoField(primary_key=True, serialize=True)
    theory = models.ForeignKey('Theory', models.DO_NOTHING, db_column='Theory_id', blank=True, null=True)  # Field name made lowercase.
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='Project_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'project_theory'


class ProtRequ(models.Model):
    pr_id = models.AutoField(primary_key=True, serialize=True)
    requ = models.ForeignKey('Requirement', models.DO_NOTHING, db_column='Requ_id')  # Field name made lowercase.
    prot = models.ForeignKey('Protocol', models.DO_NOTHING, db_column='Prot_id')  # Field name made lowercase.

    class Meta:
        db_table = 'prot_requ'


class Protocol(models.Model):
    prot_id = models.AutoField(db_column='Prot_id', primary_key=True, serialize=True)  # Field name made lowercase.
    prottitle = models.TextField(db_column='ProtTitle', blank=True, null=True)  # Field name made lowercase.
    protdesc = models.TextField(db_column='ProtDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'protocol'


class ReqProj(models.Model):
    pr_id = models.AutoField(primary_key=True, serialize=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, db_column='Project_id')  # Field name made lowercase.
    requ = models.ForeignKey('Requirement', models.DO_NOTHING, db_column='Requ_id')  # Field name made lowercase.

    class Meta:
        db_table = 'req_proj'


class Requieddata(models.Model):
    rd_id = models.AutoField(db_column='RD_id', primary_key=True, serialize=True)  # Field name made lowercase.
    rdsubject = models.IntegerField(db_column='RDSubject', blank=True, null=True)  # Field name made lowercase.
    rdsituation = models.IntegerField(db_column='RDSituation', blank=True, null=True)  # Field name made lowercase.
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id', blank=True, null=True)  # Field name made lowercase.
    gene = models.ForeignKey(Gene, models.DO_NOTHING, db_column='gene_id', blank=True, null=True)  # Field name made lowercase.
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id', blank=True, null=True)  # Field name made lowercase.
    step = models.ForeignKey(Ddstep, models.DO_NOTHING, db_column='Step_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'requieddata'


# class Requiredresearch(models.Model):
    # research_id = models.AutoField(db_column='Research_id', primary_key=True, serialize=True)  # Field name made lowercase.
    # researchsubj = models.IntegerField(db_column='ResearchSubj', blank=True, null=True)  # Field name made lowercase.
    # gene = models.ForeignKey(Gene, models.DO_NOTHING, db_column='Gene_id', blank=True, null=True)  # Field name made lowercase.
    # req_research = models.ForeignKey('self', models.DO_NOTHING, db_column='Req_Research_id', blank=True, null=True)  # Field name made lowercase.
    # researchtitle = models.TextField(db_column='ResearchTitle', blank=True, null=True)  # Field name made lowercase.
    # researchdesc = models.TextField(db_column='ResearchDesc', blank=True, null=True)  # Field name made lowercase.

    # class Meta:
        # db_table = 'requiredresearch'


class Requirement(models.Model):
    requ_id = models.AutoField(db_column='Requ_id', primary_key=True, serialize=True)  # Field name made lowercase.
    reqtitle = models.CharField(db_column='ReqTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reqdesc = models.TextField(db_column='ReqDesc', blank=True, null=True)  # Field name made lowercase.
    req_type = models.IntegerField(db_column='Req_type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'requirement'


class Species(models.Model):
    species_id = models.AutoField(db_column='species_id', primary_key=True, serialize=True)
    speciestitle = models.CharField(db_column='SpeciesTitle', max_length=40, blank=True, null=True)

    def __str__(self):
        return self.speciestitle

    class Meta:
        db_table = 'species'


class GeneSpecies(models.Model):
    gs_id = models.AutoField(primary_key=True, serialize=True)
    gene = models.ForeignKey(Gene, models.DO_NOTHING, db_column='gene_id')  # Field name made lowercase.
    species = models.ForeignKey(Species, models.DO_NOTHING, db_column='species_id')  # Field name made lowercase.
    def __str__(self):
        return  f"{self.gene.gsymbol} - {self.species.speciestitle}"

    class Meta:
        db_table = 'gene_species'
        ordering = ['gene__gsymbol']


class Sbpathway(models.Model):
    sbp_id = models.AutoField(db_column='SBP_id', primary_key=True, serialize=True)
    sbtitle = models.CharField(db_column='SBTitle', max_length=40, blank=True, null=True)
    sourcecode = models.CharField(db_column='Sourcecode', max_length=10, blank=True, null=True)
    filelocation = models.TextField(db_column='FileLocation', blank=True, null=True)
    source = models.CharField(db_column='Source', max_length=20, blank=True, null=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, db_column='Species_id', null=True, blank=True)
    sblink = models.TextField(db_column='SBLink', blank=True, null=True)

    def __str__(self):
        return self.sbtitle

    class Meta:
        db_table = 'sbpathway'


class SbpathwayTarget(models.Model):
    st_id = models.AutoField(primary_key=True, serialize=True)
    target = models.ForeignKey('Target', models.DO_NOTHING, db_column='Target_id')  # Field name made lowercase.
    sbp = models.ForeignKey(Sbpathway, models.DO_NOTHING, db_column='SBP_id')  # Field name made lowercase.

    class Meta:

        db_table = 'sbpathway_target'


class Signature(models.Model):
    sig_id = models.AutoField(db_column='Sig_id', primary_key=True, serialize=True)  # Field name made lowercase.
    gene = models.ForeignKey(Gene, models.DO_NOTHING, db_column='gene_id', blank=True, null=True)  # Field name made lowercase.
    sigsymbol = models.CharField(db_column='SigSymbol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=130, blank=True, null=True)  # Field name made lowercase.
    expression = models.CharField(db_column='Expression', max_length=15, blank=True, null=True)  # Field name made lowercase.
    otherdatabases = models.CharField(db_column='OtherDatabases', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cellage_id = models.BigIntegerField(db_column='CellAge_ID', blank=True, null=True)  # Field name made lowercase.
    sig_entrez_id = models.BigIntegerField(db_column='Sig_Entrez_id', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    p_value = models.DecimalField(db_column='P_Value', max_digits=12, decimal_places=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'signature'
        db_table_comment = 'Genes that are either over-expressed or under-expressed duri'


class StakeholderRole(models.Model):
    role_id = models.AutoField(db_column='Role_id', primary_key=True, serialize=True)  # Field name made lowercase.
    shrole = models.CharField(db_column='SHRole', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shroledesc = models.TextField(db_column='SHRoleDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'stakeholderrole'


class StakeholderOrg(models.Model):
    so_id = models.AutoField(primary_key=True, serialize=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Organization_id')  # Field name made lowercase.
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='Project_id')  # Field name made lowercase.
    role = models.ForeignKey('StakeholderRole', models.DO_NOTHING, db_column='Role_id')  # Field name made lowercase.

    class Meta:
        db_table = 'stakeholderorg'


class StakeholderPers(models.Model):
    sp_id = models.AutoField(primary_key=True, serialize=True)
    person = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.
    project = models.ForeignKey(Project, models.DO_NOTHING, db_column='Project_id')  # Field name made lowercase.
    #role = models.ForeignKey(StakeholderRole, models.DO_NOTHING, db_column='Role_id')  # Field name made lowercase.

    
    class Meta:
        db_table = 'stakeholderpers'
        #db_table = 'person_stakeholder'

class StrategyIntervention(models.Model):
    si_id = models.AutoField(primary_key=True, serialize=True)
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING, db_column='Intervention_id')  # Field name made lowercase.
    strategy = models.ForeignKey(InterventionStrategy, models.DO_NOTHING, db_column='Strategy_id')  # Field name made lowercase.
    def __str__(self):
        return f"{self.intervention.interventiontitle} - {self.strategy.strategyname}"

    class Meta:
        db_table = 'strategy_intervention'


class Supplier(models.Model):
    supl_id = models.AutoField(db_column='Supl_id', primary_key=True, serialize=True)  # Field name made lowercase.
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Organization_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'supplier'


class Sympimprove(models.Model):
    si_id = models.AutoField(db_column='SI_id', primary_key=True, serialize=True)  # Field name made lowercase.
    improvedesc = models.TextField(db_column='ImproveDesc', blank=True, null=True)  # Field name made lowercase.
    ni = models.ForeignKey(NodeIntervention, models.DO_NOTHING, db_column='NI_id', blank=True, null=True)  # Field name made lowercase.
    symptom = models.ForeignKey('Symptom', models.DO_NOTHING, db_column='Symptom_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sympimprove'


class Symptom(models.Model):
    symptom_id = models.AutoField(db_column='Symptom_id', primary_key=True, serialize=True)  # Field name made lowercase.
    symptitle = models.CharField(db_column='SympTitle', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sympdesc = models.TextField(db_column='SympDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'symptom'


class Target(models.Model):
    target_id = models.AutoField(db_column='Target_id', primary_key=True, serialize=True)  # Field name made lowercase.
    targettitle = models.CharField(db_column='TargetTitle', max_length=200, blank=True, null=True)  # Field name made lowercase.
    targetdesc = models.TextField(db_column='TargetDesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.targettitle

    class Meta:
        db_table = 'target'


class TargetArticle(models.Model):
    ta_id = models.AutoField(primary_key=True, serialize=True)
    lit = models.ForeignKey(Literature, models.DO_NOTHING, db_column='Lit_id')  # Field name made lowercase.
    target = models.ForeignKey(Target, models.DO_NOTHING, db_column='Target_id')  # Field name made lowercase.
    def __str__(self):
        return  f"{self.target.targettitle} - {self.lit.littitle}"

    class Meta:
        db_table = 'target_article'


class Targetingligand(models.Model):
    tl_id = models.AutoField(db_column='TL_id', primary_key=True, serialize=True)  # Field name made lowercase.
    lt = models.ForeignKey(Ligandtype, models.DO_NOTHING, db_column='LT_id', blank=True, null=True)  # Field name made lowercase.
    tltitle = models.TextField(db_column='TLTitle', blank=True, null=True)  # Field name made lowercase.
    tldesc = models.TextField(db_column='TLDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'targetingligand'

class Theory(models.Model):
    theory_id = models.AutoField(db_column='Theory_id', primary_key=True, serialize=True)
    #theory_id = models.BigIntegerField(db_column='Theory_id', primary_key=True, serialize=True)  # Field name made lowercase.
    theorytitle = models.CharField(db_column='TheoryTitle', max_length=40, blank=True, null=True)  # Field name made lowercase.
    theorydesc = models.TextField(db_column='TheoryDesc', blank=True, null=True)  # Field name made lowercase.
    parent_t = models.ForeignKey('self', models.DO_NOTHING, db_column='Parent_T_id', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.theorytitle

    class Meta:
        db_table = 'theory'

class TheoryLiterature(models.Model):
    tl_id = models.AutoField(primary_key=True, serialize=True)
    lit = models.ForeignKey(Literature, models.DO_NOTHING, db_column='Lit_id')  # Field name made lowercase.
    theory = models.ForeignKey(Theory, models.DO_NOTHING, db_column='Theory_id')  # Field name made lowercase.

    class Meta:
        db_table = 'theory_literature'


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True, serialize=True)
    unitname = models.CharField(db_column='UnitName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'unit'


class Visit(models.Model):
    visit_id = models.AutoField(db_column='Visit_id', primary_key=True, serialize=True)  # Field name made lowercase.
    patient = models.ForeignKey(Person, models.DO_NOTHING, db_column='Patient_id')  # Field name made lowercase.
    md = models.ForeignKey(Person, models.DO_NOTHING, db_column='MD_id', related_name='visit_md_set')  # Field name made lowercase.
    visitdate = models.DateField(db_column='VisitDate', blank=True, null=True)  # Field name made lowercase.
    visittime = models.TimeField(db_column='VisitTime', blank=True, null=True)  # Field name made lowercase.
    visitdesc = models.TextField(db_column='VisitDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'visit'
        
class Hallmark(models.Model):
    hallmark_id = models.AutoField(db_column='Hallmark_id', primary_key=True, serialize=True)
    hallmarktitle = models.CharField(db_column='HallmarkTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hallmarkdesc = models.TextField(db_column='HallmarkDesc', blank=True, null=True)  # Field name made lowercase.
    p_hm = models.ForeignKey('self', models.DO_NOTHING, db_column='P_hm_id', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.hallmarktitle

    class Meta:
        db_table = 'hallmark'

class NodeHallmark(models.Model):
    nh_id = models.AutoField(primary_key=True, serialize=True)
    hallmark = models.ForeignKey('Hallmark', models.DO_NOTHING, db_column='Hallmark_id')  # Field name made lowercase.
    node = models.ForeignKey(Node, models.DO_NOTHING, db_column='Node_id')  # Field name made lowercase.
    nhdesc = models.TextField(db_column='NHDesc', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return  f"{self.node.ref_num} - {self.hallmark.hallmarktitle}"

    class Meta:

        db_table = 'node_hallmark'
