# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('oferclubabstractuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('cellphone', models.CharField(max_length=20, verbose_name='Celular')),
                ('owner_name', models.CharField(help_text='Nome do titular', max_length=200, verbose_name='Nome do Titular')),
                ('bank_name', models.CharField(help_text='Nome do banco', max_length=100, verbose_name='Banco')),
                ('agency', models.CharField(help_text='C\xf3digo da ag\xeancia', max_length=100, verbose_name='Ag\xeancia')),
                ('number', models.CharField(help_text='N\xfamero da conta', max_length=100, verbose_name='Conta')),
                ('cpf', models.CharField(help_text='CPF do propriet\xe1rio da conta', max_length=14, verbose_name='CPF')),
                ('city', models.ForeignKey(blank=True, to='account.City', null=True)),
            ],
            options={
                'verbose_name': 'Filial do OferClub',
                'verbose_name_plural': 'filiais do OferClub',
            },
            bases=('account.oferclubabstractuser',),
        ),
    ]
