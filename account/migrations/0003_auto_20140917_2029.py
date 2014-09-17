# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_affiliate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='affiliate',
            options={'verbose_name': 'Afiliado', 'verbose_name_plural': 'Afiliados'},
        ),
        migrations.AlterModelOptions(
            name='filial',
            options={'verbose_name': 'Filial', 'verbose_name_plural': 'Filiais'},
        ),
        migrations.AlterModelOptions(
            name='oferclubuser',
            options={'verbose_name': 'Usu\xe1rio', 'verbose_name_plural': 'Usu\xe1rios'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name': 'Parceiro', 'verbose_name_plural': 'Parceiros'},
        ),
        migrations.AlterField(
            model_name='affiliate',
            name='agency',
            field=models.CharField(help_text='C\xf3digo da ag\xeancia', max_length=100, null=True, verbose_name='Ag\xeancia', blank=True),
        ),
        migrations.AlterField(
            model_name='affiliate',
            name='bank_name',
            field=models.CharField(help_text='Nome do banco', max_length=100, null=True, verbose_name='Banco', blank=True),
        ),
        migrations.AlterField(
            model_name='affiliate',
            name='cpf',
            field=models.CharField(help_text='CPF do propriet\xe1rio da conta', max_length=14, null=True, verbose_name='CPF', blank=True),
        ),
        migrations.AlterField(
            model_name='affiliate',
            name='number',
            field=models.CharField(help_text='N\xfamero da conta', max_length=100, null=True, verbose_name='Conta', blank=True),
        ),
        migrations.AlterField(
            model_name='affiliate',
            name='owner_name',
            field=models.CharField(help_text='Nome do titular', max_length=200, null=True, verbose_name='Nome do Titular', blank=True),
        ),
        migrations.AlterField(
            model_name='filial',
            name='agency',
            field=models.CharField(help_text='C\xf3digo da ag\xeancia', max_length=100, null=True, verbose_name='Ag\xeancia', blank=True),
        ),
        migrations.AlterField(
            model_name='filial',
            name='bank_name',
            field=models.CharField(help_text='Nome do banco', max_length=100, null=True, verbose_name='Banco', blank=True),
        ),
        migrations.AlterField(
            model_name='filial',
            name='cpf',
            field=models.CharField(help_text='CPF do propriet\xe1rio da conta', max_length=14, null=True, verbose_name='CPF', blank=True),
        ),
        migrations.AlterField(
            model_name='filial',
            name='number',
            field=models.CharField(help_text='N\xfamero da conta', max_length=100, null=True, verbose_name='Conta', blank=True),
        ),
        migrations.AlterField(
            model_name='filial',
            name='owner_name',
            field=models.CharField(help_text='Nome do titular', max_length=200, null=True, verbose_name='Nome do Titular', blank=True),
        ),
    ]
