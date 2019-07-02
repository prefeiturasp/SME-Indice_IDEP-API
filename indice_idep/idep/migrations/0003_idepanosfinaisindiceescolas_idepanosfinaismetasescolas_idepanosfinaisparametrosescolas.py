# Generated by Django 2.2.1 on 2019-06-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idep', '0002_idepanosiniciaisparametrosescolas'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdepAnosFinaisIndiceEscolas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_esc', models.TextField(blank=True, null=True)),
                ('cod_mec', models.TextField(blank=True, null=True)),
                ('idep_2018', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdepAnosFinaisMetasEscolas',
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
            name='IdepAnosFinaisParametrosEscolas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_esc', models.TextField(blank=True, null=True)),
                ('cod_mec', models.TextField(blank=True, null=True)),
                ('icg', models.TextField(blank=True, null=True)),
                ('nse', models.TextField(blank=True, null=True)),
                ('number_3_med_2017_ci', models.TextField(blank=True, db_column='3_med_2017_ci', null=True)),
                ('number_3_alun_2017_ci', models.TextField(blank=True, db_column='3_alun_2017_ci', null=True)),
                ('number_3_med_2018_ci', models.TextField(blank=True, db_column='3_med_2018_ci', null=True)),
                ('number_3_alun_2018_ci', models.TextField(blank=True, db_column='3_alun_2018_ci', null=True)),
                ('number_3_med_pond_17_18_ci', models.TextField(blank=True, db_column='3_med_pond_17_18_ci', null=True)),
                ('number_3_tot_alun_17_18_ci', models.TextField(blank=True, db_column='3_tot_alun_17_18_ci', null=True)),
                ('number_3_med_2017_lp', models.TextField(blank=True, db_column='3_med_2017_lp', null=True)),
                ('number_3_alun_2017_lp', models.TextField(blank=True, db_column='3_alun_2017_lp', null=True)),
                ('number_3_med_2018_lp', models.TextField(blank=True, db_column='3_med_2018_lp', null=True)),
                ('number_3_alun_2018_lp', models.TextField(blank=True, db_column='3_alun_2018_lp', null=True)),
                ('number_3_med_pond_17_18_lp', models.TextField(blank=True, db_column='3_med_pond_17_18_lp', null=True)),
                ('number_3_tot_alun_17_18_lp', models.TextField(blank=True, db_column='3_tot_alun_17_18_lp', null=True)),
                ('number_3_med_2017_mt', models.TextField(blank=True, db_column='3_med_2017_mt', null=True)),
                ('number_3_alun_2017_mt', models.TextField(blank=True, db_column='3_alun_2017_mt', null=True)),
                ('number_3_med_2018_mt', models.TextField(blank=True, db_column='3_med_2018_mt', null=True)),
                ('number_3_alun_2018_mt', models.TextField(blank=True, db_column='3_alun_2018_mt', null=True)),
                ('number_3_med_pond_17_18_mt', models.TextField(blank=True, db_column='3_med_pond_17_18_mt', null=True)),
                ('number_3_tot_alun_17_18_mt', models.TextField(blank=True, db_column='3_tot_alun_17_18_mt', null=True)),
                ('number_5_med_2017_ci', models.TextField(blank=True, db_column='5_med_2017_ci', null=True)),
                ('number_5_alun_2017_ci', models.TextField(blank=True, db_column='5_alun_2017_ci', null=True)),
                ('number_5_med_2018_ci', models.TextField(blank=True, db_column='5_med_2018_ci', null=True)),
                ('number_5_alun_2018_ci', models.TextField(blank=True, db_column='5_alun_2018_ci', null=True)),
                ('number_5_med_pond_17_18_ci', models.TextField(blank=True, db_column='5_med_pond_17_18_ci', null=True)),
                ('number_5_tot_alun_17_18_ci', models.TextField(blank=True, db_column='5_tot_alun_17_18_ci', null=True)),
                ('number_5_med_2017_lp', models.TextField(blank=True, db_column='5_med_2017_lp', null=True)),
                ('number_5_alun_2017_lp', models.TextField(blank=True, db_column='5_alun_2017_lp', null=True)),
                ('number_5_med_2018_lp', models.TextField(blank=True, db_column='5_med_2018_lp', null=True)),
                ('number_5_alun_2018_lp', models.TextField(blank=True, db_column='5_alun_2018_lp', null=True)),
                ('number_5_med_pond_17_18_lp', models.TextField(blank=True, db_column='5_med_pond_17_18_lp', null=True)),
                ('number_5_tot_alun_17_18_lp', models.TextField(blank=True, db_column='5_tot_alun_17_18_lp', null=True)),
                ('number_5_med_2017_mt', models.TextField(blank=True, db_column='5_med_2017_mt', null=True)),
                ('number_5_alun_2017_mt', models.TextField(blank=True, db_column='5_alun_2017_mt', null=True)),
                ('number_5_med_2018_mt', models.TextField(blank=True, db_column='5_med_2018_mt', null=True)),
                ('number_5_alun_2018_mt', models.TextField(blank=True, db_column='5_alun_2018_mt', null=True)),
                ('number_5_med_pond_17_18_mt', models.TextField(blank=True, db_column='5_med_pond_17_18_mt', null=True)),
                ('number_5_tot_alun_17_18_mt', models.TextField(blank=True, db_column='5_tot_alun_17_18_mt', null=True)),
                ('number_3cresc_5y_ci', models.TextField(blank=True, db_column='3cresc_5y_CI', null=True)),
                ('number_3cresc_5y_lp', models.TextField(blank=True, db_column='3cresc_5y_LP', null=True)),
                ('number_3cresc_5y_mt', models.TextField(blank=True, db_column='3cresc_5y_MT', null=True)),
                ('number_5cresc_5y_ci', models.TextField(blank=True, db_column='5cresc_5y_CI', null=True)),
                ('number_5cresc_5y_lp', models.TextField(blank=True, db_column='5cresc_5y_LP', null=True)),
                ('number_5cresc_5y_mt', models.TextField(blank=True, db_column='5cresc_5y_MT', null=True)),
                ('number_3cresc_1y_ci', models.TextField(blank=True, db_column='3cresc_1y_CI', null=True)),
                ('number_3cresc_1y_lp', models.TextField(blank=True, db_column='3cresc_1y_LP', null=True)),
                ('number_3cresc_1y_mt', models.TextField(blank=True, db_column='3cresc_1y_MT', null=True)),
                ('number_5cresc_1y_ci', models.TextField(blank=True, db_column='5cresc_1y_CI', null=True)),
                ('number_5cresc_1y_lp', models.TextField(blank=True, db_column='5cresc_1y_LP', null=True)),
                ('number_5cresc_1y_mt', models.TextField(blank=True, db_column='5cresc_1y_MT', null=True)),
                ('fluxo_med_17_18', models.TextField(blank=True, null=True)),
                ('c', models.TextField(blank=True, null=True)),
                ('b', models.TextField(blank=True, null=True)),
                ('a', models.TextField(blank=True, null=True)),
            ],
        ),
    ]