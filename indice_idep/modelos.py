# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('PessoasServidoruser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EscolasEscolas(models.Model):
    dre = models.TextField(blank=True, null=True)
    codesc = models.CharField(primary_key=True, max_length=6)
    tipoesc = models.CharField(max_length=12, blank=True, null=True)
    nomesc = models.CharField(max_length=60, blank=True, null=True)
    ceu = models.TextField(blank=True, null=True)
    diretoria = models.CharField(max_length=60, blank=True, null=True)
    subpref = models.CharField(max_length=35, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    numero = models.CharField(max_length=6, blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cep = models.IntegerField(blank=True, null=True)
    tel1 = models.CharField(max_length=40, blank=True, null=True)
    tel2 = models.CharField(max_length=40, blank=True, null=True)
    fax = models.CharField(max_length=40, blank=True, null=True)
    situacao = models.CharField(max_length=10, blank=True, null=True)
    coddist = models.TextField(blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    setor = models.SmallIntegerField(blank=True, null=True)
    codinep = models.IntegerField(blank=True, null=True)
    cd_cie = models.TextField(blank=True, null=True)
    eh = models.CharField(max_length=15, blank=True, null=True)
    fx_etaria = models.CharField(max_length=100, blank=True, null=True)
    dt_criacao = models.DateTimeField(blank=True, null=True)
    ato_criacao = models.CharField(max_length=20, blank=True, null=True)
    dom_criacao = models.DateTimeField(blank=True, null=True)
    dt_ini_conv = models.DateTimeField(blank=True, null=True)
    dt_ini_func = models.DateTimeField(blank=True, null=True)
    dt_autoriza = models.DateTimeField(blank=True, null=True)
    dt_extintao = models.DateTimeField(blank=True, null=True)
    nome_ant = models.CharField(max_length=100, blank=True, null=True)
    rede = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    database = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escolas_escolas'


class IdepIdepanosfinaisv1(models.Model):
    cod_esc = models.TextField(primary_key=True)
    nse = models.IntegerField(blank=True, null=True)
    icg = models.IntegerField(blank=True, null=True)
    number_2018 = models.TextField(db_column='2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2019 = models.TextField(db_column='2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2020 = models.TextField(db_column='2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2021 = models.TextField(db_column='2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2022 = models.TextField(db_column='2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2023 = models.TextField(db_column='2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'idep_idepanosfinaisv1'


class IdepIdepanosiniciaisindiceescolas(models.Model):
    cod_esc = models.TextField(blank=True, null=True)
    cod_mec = models.TextField(blank=True, null=True)
    idep_2018 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idep_idepanosiniciaisindiceescolas'


class IdepIdepanosiniciaismetasescolas(models.Model):
    cod_esc = models.TextField(blank=True, null=True)
    cod_mec = models.TextField(blank=True, null=True)
    idep_2019 = models.TextField(blank=True, null=True)
    idep_2020 = models.TextField(blank=True, null=True)
    idep_2021 = models.TextField(blank=True, null=True)
    idep_2022 = models.TextField(blank=True, null=True)
    idep_2023 = models.TextField(blank=True, null=True)
    idep_2038 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idep_idepanosiniciaismetasescolas'


class IdepIdepanosiniciaisv1(models.Model):
    cod_esc = models.TextField(primary_key=True)
    nse = models.IntegerField(blank=True, null=True)
    icg = models.IntegerField(blank=True, null=True)
    number_2018 = models.TextField(db_column='2018', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2019 = models.TextField(db_column='2019', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2020 = models.TextField(db_column='2020', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2021 = models.TextField(db_column='2021', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2022 = models.TextField(db_column='2022', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2023 = models.TextField(db_column='2023', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'idep_idepanosiniciaisv1'


class IdepParametrosEscolasAi(models.Model):
    cod_esc = models.TextField(blank=True, null=True)
    cod_mec = models.TextField(blank=True, null=True)
    icg = models.TextField(blank=True, null=True)
    nse = models.TextField(blank=True, null=True)
    number_3_med_2017_ci = models.TextField(db_column='3_med_2017_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_alun_2017_ci = models.TextField(db_column='3_alun_2017_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_med_2018_ci = models.TextField(db_column='3_med_2018_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_alun_2018_ci = models.TextField(db_column='3_alun_2018_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_med_pond_17_18_ci = models.TextField(db_column='3_med_pond_17_18_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_tot_alun_17_18_ci = models.TextField(db_column='3_tot_alun_17_18_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_med_2017_lp = models.TextField(db_column='3_med_2017_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_alun_2017_lp = models.TextField(db_column='3_alun_2017_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_med_2018_lp = models.TextField(db_column='3_med_2018_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_alun_2018_lp = models.TextField(db_column='3_alun_2018_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_med_pond_17_18_lp = models.TextField(db_column='3_med_pond_17_18_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_tot_alun_17_18_lp = models.TextField(db_column='3_tot_alun_17_18_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_med_2017_mt = models.TextField(db_column='3_med_2017_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_alun_2017_mt = models.TextField(db_column='3_alun_2017_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_med_2018_mt = models.TextField(db_column='3_med_2018_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_alun_2018_mt = models.TextField(db_column='3_alun_2018_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_med_pond_17_18_mt = models.TextField(db_column='3_med_pond_17_18_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_tot_alun_17_18_mt = models.TextField(db_column='3_tot_alun_17_18_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_med_2017_ci = models.TextField(db_column='5_med_2017_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_alun_2017_ci = models.TextField(db_column='5_alun_2017_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_med_2018_ci = models.TextField(db_column='5_med_2018_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_alun_2018_ci = models.TextField(db_column='5_alun_2018_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_med_pond_17_18_ci = models.TextField(db_column='5_med_pond_17_18_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_tot_alun_17_18_ci = models.TextField(db_column='5_tot_alun_17_18_ci', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_med_2017_lp = models.TextField(db_column='5_med_2017_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_alun_2017_lp = models.TextField(db_column='5_alun_2017_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_med_2018_lp = models.TextField(db_column='5_med_2018_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_alun_2018_lp = models.TextField(db_column='5_alun_2018_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_med_pond_17_18_lp = models.TextField(db_column='5_med_pond_17_18_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_tot_alun_17_18_lp = models.TextField(db_column='5_tot_alun_17_18_lp', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_med_2017_mt = models.TextField(db_column='5_med_2017_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_alun_2017_mt = models.TextField(db_column='5_alun_2017_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_med_2018_mt = models.TextField(db_column='5_med_2018_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_alun_2018_mt = models.TextField(db_column='5_alun_2018_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_med_pond_17_18_mt = models.TextField(db_column='5_med_pond_17_18_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5_tot_alun_17_18_mt = models.TextField(db_column='5_tot_alun_17_18_mt', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3cresc_5y_ci = models.TextField(db_column='3cresc_5y_CI', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3cresc_5y_lp = models.TextField(db_column='3cresc_5y_LP', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3cresc_5y_mt = models.TextField(db_column='3cresc_5y_MT', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5cresc_5y_ci = models.TextField(db_column='5cresc_5y_CI', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5cresc_5y_lp = models.TextField(db_column='5cresc_5y_LP', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5cresc_5y_mt = models.TextField(db_column='5cresc_5y_MT', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3cresc_1y_ci = models.TextField(db_column='3cresc_1y_CI', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3cresc_1y_lp = models.TextField(db_column='3cresc_1y_LP', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3cresc_1y_mt = models.TextField(db_column='3cresc_1y_MT', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5cresc_1y_ci = models.TextField(db_column='5cresc_1y_CI', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5cresc_1y_lp = models.TextField(db_column='5cresc_1y_LP', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5cresc_1y_mt = models.TextField(db_column='5cresc_1y_MT', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    fluxo_med_17_18 = models.TextField(blank=True, null=True)
    c = models.TextField(blank=True, null=True)
    b = models.TextField(blank=True, null=True)
    a = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'idep_parametros_escolas_ai'


class MainTestmodel(models.Model):
    test = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'main_testmodel'


class PessoasServidores(models.Model):
    rf = models.IntegerField(blank=True, null=True)
    cd_cpf_pessoa = models.TextField(blank=True, null=True)
    nm_pessoa = models.TextField(blank=True, null=True)
    cd_serv_sme = models.IntegerField(blank=True, null=True)
    mes_nasc = models.IntegerField(blank=True, null=True)
    ano_nasc = models.IntegerField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    cd_sexo = models.TextField(blank=True, null=True)
    cd_municipio_nasc = models.IntegerField(blank=True, null=True)
    dc_municipio_nasc = models.TextField(blank=True, null=True)
    uf_municipio_nasc = models.TextField(blank=True, null=True)
    cd_pais_nasc = models.IntegerField(blank=True, null=True)
    dc_pais_nasc = models.TextField(blank=True, null=True)
    cd_municipio_res = models.IntegerField(blank=True, null=True)
    dc_municipio_res = models.TextField(blank=True, null=True)
    uf_municipio_res = models.TextField(blank=True, null=True)
    cd_raca_cor = models.IntegerField(blank=True, null=True)
    dc_raca_cor = models.TextField(blank=True, null=True)
    cd_def = models.IntegerField(blank=True, null=True)
    dc_def = models.TextField(blank=True, null=True)
    nivel_form = models.TextField(blank=True, null=True)
    dc_sit_func = models.TextField(blank=True, null=True)
    cd_cargo_base = models.IntegerField(blank=True, null=True)
    dc_cargo_base = models.TextField(blank=True, null=True)
    cd_area_atuacao_base = models.IntegerField(blank=True, null=True)
    dc_area_atuacao_base = models.TextField(blank=True, null=True)
    dt_inicio_cargo_base = models.TextField(blank=True, null=True)
    cd_unidade_base = models.TextField(blank=True, null=True)
    tp_unidade_base = models.TextField(blank=True, null=True)
    dc_unidade_base = models.TextField(blank=True, null=True)
    sigla_lotacao = models.TextField(blank=True, null=True)
    tp_lotacao = models.TextField(blank=True, null=True)
    cd_cargo_atual = models.IntegerField(blank=True, null=True)
    dc_cargo_atual = models.TextField(blank=True, null=True)
    cd_area_atuacao_cargo_atual = models.TextField(blank=True, null=True)
    dc_area_atuacao_cargo_atual = models.TextField(blank=True, null=True)
    cd_unidade_educacao_atual = models.TextField(blank=True, null=True)
    tp_unidade_educacao_atual = models.TextField(blank=True, null=True)
    dc_unidade_educacao_atual = models.TextField(blank=True, null=True)
    sigla_atual = models.TextField(blank=True, null=True)
    cd_unidade_funcao = models.IntegerField(blank=True, null=True)
    cd_funcao = models.IntegerField(blank=True, null=True)
    dc_funcao = models.TextField(blank=True, null=True)
    dt_inicio_funcao = models.TextField(blank=True, null=True)
    cd_unidade_sobreposto = models.TextField(blank=True, null=True)
    cd_sobreposto = models.IntegerField(blank=True, null=True)
    dc_sobreposto = models.TextField(blank=True, null=True)
    dt_inicio_sobreposto = models.TextField(blank=True, null=True)
    database = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoas_servidores'


class PessoasServidoruser(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    rf = models.IntegerField(unique=True)
    password = models.TextField(blank=True, null=True)
    ano_nasc = models.IntegerField(blank=True, null=True)
    mes_nasc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoas_servidoruser'


class PessoasServidoruserGroups(models.Model):
    servidoruser = models.ForeignKey(PessoasServidoruser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pessoas_servidoruser_groups'
        unique_together = (('servidoruser', 'group'),)


class PessoasServidoruserUserPermissions(models.Model):
    servidoruser = models.ForeignKey(PessoasServidoruser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pessoas_servidoruser_user_permissions'
        unique_together = (('servidoruser', 'permission'),)
