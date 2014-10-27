# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '__first__'),
        ('offer', '0004_subcategory_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=255, verbose_name='C\xf3digo')),
                ('price', models.DecimalField(verbose_name='valor pago', max_digits=10, decimal_places=2)),
                ('is_consumed', models.BooleanField(default=0, verbose_name='Foi consumido?', choices=[(1, 'Consumido'), (0, 'N\xe3o Consumido')])),
                ('date_expiration', models.DateField(verbose_name='Expira em')),
                ('date_consumed', models.DateTimeField(null=True, verbose_name='Consumido em', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Gerado em')),
                ('address', models.ForeignKey(verbose_name='endere\xe7o', blank=True, to='account.Address', null=True)),
            ],
            options={
                'ordering': ['date_created'],
                'verbose_name': 'Cupom',
                'verbose_name_plural': 'Cupons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255, verbose_name='Descri\xe7\xe3o')),
                ('type_operation', models.BooleanField(default=0, verbose_name='Tipo', choices=[(0, b'D\xc3\xa9bito'), (1, b'Cr\xc3\xa9dito')])),
                ('value', models.DecimalField(verbose_name='valor', max_digits=10, decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Gerado em')),
                ('user', models.ForeignKey(related_name=b'operations', verbose_name='usu\xe1rio', to='account.OferClubUser')),
            ],
            options={
                'verbose_name': 'Opera\xe7\xe3o',
                'verbose_name_plural': 'Opera\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_consumer', models.CharField(max_length=200, null=True, verbose_name='nome completo', blank=True)),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantidade')),
                ('total', models.DecimalField(verbose_name='valor pago', max_digits=10, decimal_places=2)),
                ('code_pagseguro', models.CharField(max_length=255, null=True, verbose_name='C\xf3digo PagSeguro', blank=True)),
                ('status', models.PositiveSmallIntegerField(default=2, null=True, verbose_name='situa\xe7\xe3o', blank=True, choices=[(0, 'Aprovada'), (1, 'Negada'), (2, 'Em An\xe1lise')])),
                ('purchase_time', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('date_approved', models.DateTimeField(null=True, verbose_name='Aprovado em', blank=True)),
                ('option', models.ForeignKey(related_name=b'orders', to='offer.Option')),
                ('user', models.ForeignKey(related_name=b'orders', verbose_name='usu\xe1rio', to='account.OferClubUser')),
            ],
            options={
                'ordering': ['purchase_time'],
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coupon',
            name='order',
            field=models.ForeignKey(related_name=b'get_coupons', to='checkout.Order'),
            preserve_default=True,
        ),
    ]
