# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20140918_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.ImageField(upload_to=b'oferta/', verbose_name='Imagem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('highlight', models.BooleanField(default=False, verbose_name='Destaque')),
                ('highlight_image', models.ImageField(upload_to=b'oferta/', verbose_name='Imagem Destaque')),
                ('bought', models.IntegerField(verbose_name='Comprados')),
                ('bought_virtual', models.IntegerField(verbose_name='Quantidade virtual')),
                ('max_by_user', models.IntegerField(null=True, verbose_name='M\xe1ximo por pessoa', blank=True)),
                ('percent_by_site', models.DecimalField(verbose_name='Percentual do site', max_digits=10, decimal_places=2)),
                ('percent_by_affiliate', models.DecimalField(null=True, verbose_name='Percentual do site', max_digits=10, decimal_places=2, blank=True)),
                ('description', models.TextField(verbose_name='Descri\xe7\xe3o')),
                ('regulation', models.TextField(verbose_name='Regulamento')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('affiliate', models.ForeignKey(blank=True, to='account.Affiliate', null=True)),
                ('city', models.ManyToManyField(to='account.City', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('old_price', models.DecimalField(null=True, verbose_name='Pre\xe7o sem desconto', max_digits=10, decimal_places=2, blank=True)),
                ('new_price', models.DecimalField(verbose_name='Pre\xe7o com desconto', max_digits=10, decimal_places=2)),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('start_time', models.DateTimeField(verbose_name='Come\xe7a em')),
                ('end_time', models.DateTimeField(verbose_name='Termina em')),
                ('date_expiration', models.DateField(verbose_name='Expira em')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('filial', models.ForeignKey(to='account.Filial')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='offer',
            field=models.ForeignKey(to='offer.Offer'),
            preserve_default=True,
        ),
    ]
