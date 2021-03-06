# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aposta', '0003_aposta_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aposta2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aposta_identificacao', models.CharField(max_length=200)),
                ('valor', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Concurso2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concurso_edicao', models.CharField(max_length=20)),
                ('pub_data', models.DateTimeField(verbose_name='data de publicacao')),
            ],
        ),
        migrations.AlterField(
            model_name='aposta',
            name='dataAposta',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='aposta2',
            name='Concurso2_identificao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aposta.Concurso2'),
        ),
    ]
