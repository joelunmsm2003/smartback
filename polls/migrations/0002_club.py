# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-31 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000, null=True)),
                ('razon_social', models.CharField(blank=True, max_length=1000, null=True)),
                ('ruc', models.CharField(blank=True, max_length=1000, null=True)),
                ('representante', models.CharField(blank=True, max_length=1000, null=True)),
                ('email_repre', models.CharField(blank=True, max_length=1000, null=True)),
                ('telefono', models.CharField(blank=True, max_length=1000, null=True)),
                ('direccion', models.CharField(blank=True, max_length=1000, null=True)),
                ('pagina_web', models.CharField(blank=True, max_length=1000, null=True)),
                ('pagina_red_social', models.CharField(blank=True, max_length=1000, null=True)),
                ('max_usuarios', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
