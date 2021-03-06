# Generated by Django 2.2.1 on 2019-05-28 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escolas',
            fields=[
                ('dre', models.TextField(blank=True, null=True)),
                ('codesc', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('tipoesc', models.CharField(blank=True, max_length=12, null=True)),
                ('nomesc', models.CharField(blank=True, max_length=60, null=True)),
                ('ceu', models.TextField(blank=True, null=True)),
                ('diretoria', models.CharField(blank=True, max_length=60, null=True)),
                ('subpref', models.CharField(blank=True, max_length=35, null=True)),
                ('endereco', models.TextField(blank=True, null=True)),
                ('numero', models.CharField(blank=True, max_length=6, null=True)),
                ('bairro', models.CharField(blank=True, max_length=40, null=True)),
                ('cep', models.IntegerField(blank=True, null=True)),
                ('tel1', models.CharField(blank=True, max_length=40, null=True)),
                ('tel2', models.CharField(blank=True, max_length=40, null=True)),
                ('fax', models.CharField(blank=True, max_length=40, null=True)),
                ('situacao', models.CharField(blank=True, max_length=10, null=True)),
                ('coddist', models.TextField(blank=True, null=True)),
                ('distrito', models.TextField(blank=True, null=True)),
                ('setor', models.SmallIntegerField(blank=True, null=True)),
                ('codinep', models.IntegerField(blank=True, null=True)),
                ('cd_cie', models.TextField(blank=True, null=True)),
                ('eh', models.CharField(blank=True, max_length=15, null=True)),
                ('fx_etaria', models.CharField(blank=True, max_length=100, null=True)),
                ('dt_criacao', models.DateTimeField(blank=True, null=True)),
                ('ato_criacao', models.CharField(blank=True, max_length=20, null=True)),
                ('dom_criacao', models.DateTimeField(blank=True, null=True)),
                ('dt_ini_conv', models.DateTimeField(blank=True, null=True)),
                ('dt_ini_func', models.DateTimeField(blank=True, null=True)),
                ('dt_autoriza', models.DateTimeField(blank=True, null=True)),
                ('dt_extintao', models.DateTimeField(blank=True, null=True)),
                ('nome_ant', models.CharField(blank=True, max_length=100, null=True)),
                ('rede', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('database', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
