# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0005_auto_20140919_1552'),
        ('account', '0002_auto_20140918_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_consumer', models.CharField(max_length=200, verbose_name='nome completo')),
                ('code', models.CharField(unique=True, max_length=255, verbose_name='C\xf3digo')),
                ('price', models.DecimalField(verbose_name='valor pago', max_digits=10, decimal_places=2)),
                ('is_consumed', models.BooleanField(default=0, verbose_name='Foi consumido?', choices=[(1, 'Consumido'), (0, 'N\xe3o Consumido')])),
                ('date_expiration', models.DateField(verbose_name='Expira em')),
                ('date_consumed', models.DateTimeField(auto_now_add=True, verbose_name='Consumido em')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Gerado em')),
                ('address', models.ForeignKey(verbose_name='endere\xe7o', to='account.Address')),
                ('option', models.ForeignKey(related_name=b'coupons', to='offer.Option')),
            ],
            options={
                'ordering': ['date_created'],
                'verbose_name': 'Cupom',
                'verbose_name_plural': 'Cupons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.DecimalField(verbose_name='valor pago', max_digits=10, decimal_places=2)),
                ('status', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='situa\xe7\xe3o', choices=[(0, 'Aprovada'), (1, 'Negada'), (2, 'Negada por Fraude'), (5, 'Em Revis\xe3o (An\xe1lise Manual de Fraude)'), (1022, 'Erro na operadora de cart\xe3o'), (1024, 'Erro nos par\xe2metros enviados'), (1025, 'Erro nas credenciais'), (2048, 'Erro interno na maxiPago!'), (4097, 'Timeout com a adquirente')])),
                ('purchase_time', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('user', models.ForeignKey(related_name=b'orders', verbose_name='usu\xe1rio', to='account.OferClubUser')),
            ],
            options={
                'ordering': ['purchase_time'],
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
            bases=(models.Model,),
        ),
    ]
