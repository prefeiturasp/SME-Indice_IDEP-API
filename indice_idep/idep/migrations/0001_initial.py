# Generated by Django 2.2.1 on 2019-06-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdepAnosFinaisV1',
            fields=[
                ('cod_esc', models.TextField(primary_key=True, serialize=False)),
                ('nse', models.IntegerField(blank=True, null=True)),
                ('icg', models.IntegerField(blank=True, null=True)),
                ('number_2018', models.TextField(blank=True, db_column='2018', null=True)),
                ('number_2019', models.TextField(blank=True, db_column='2019', null=True)),
                ('number_2020', models.TextField(blank=True, db_column='2020', null=True)),
                ('number_2021', models.TextField(blank=True, db_column='2021', null=True)),
                ('number_2022', models.TextField(blank=True, db_column='2022', null=True)),
                ('number_2023', models.TextField(blank=True, db_column='2023', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdepAnosIniciaisIndiceEscolas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_esc', models.TextField(blank=True, null=True)),
                ('cod_mec', models.TextField(blank=True, null=True)),
                ('idep_2018', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdepAnosIniciaisMetasEscolas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_esc', models.TextField(blank=True, null=True)),
                ('cod_mec', models.TextField(blank=True, null=True)),
                ('idep_2019', models.TextField(blank=True, null=True)),
                ('idep_2020', models.TextField(blank=True, null=True)),
                ('idep_2021', models.TextField(blank=True, null=True)),
                ('idep_2022', models.TextField(blank=True, null=True)),
                ('idep_2023', models.TextField(blank=True, null=True)),
                ('idep_2038', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdepAnosIniciaisV1',
            fields=[
                ('cod_esc', models.TextField(primary_key=True, serialize=False)),
                ('nse', models.IntegerField(blank=True, null=True)),
                ('icg', models.IntegerField(blank=True, null=True)),
                ('number_2018', models.TextField(blank=True, db_column='2018', null=True)),
                ('number_2019', models.TextField(blank=True, db_column='2019', null=True)),
                ('number_2020', models.TextField(blank=True, db_column='2020', null=True)),
                ('number_2021', models.TextField(blank=True, db_column='2021', null=True)),
                ('number_2022', models.TextField(blank=True, db_column='2022', null=True)),
                ('number_2023', models.TextField(blank=True, db_column='2023', null=True)),
            ],
        ),
    ]
