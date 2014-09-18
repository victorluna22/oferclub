# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliate',
            name='cellphone',
            field=models.CharField(max_length=20, null=True, verbose_name='Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='affiliate',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Telefone', blank=True),
        ),
        migrations.AlterField(
            model_name='filial',
            name='cellphone',
            field=models.CharField(max_length=20, null=True, verbose_name='Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='filial',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Telefone', blank=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='cellphone',
            field=models.CharField(max_length=20, null=True, verbose_name='Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Telefone', blank=True),
        ),
    ]
