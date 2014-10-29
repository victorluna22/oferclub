# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20141029_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
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
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('category', models.ForeignKey(related_name=b'interests', to='offer.Category')),
            ],
            options={
                'verbose_name': 'Interesse',
                'verbose_name_plural': 'Interesses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('slug', models.SlugField(unique=True, max_length=255, blank=True)),
                ('image_grid', models.ImageField(upload_to=b'oferta/', verbose_name='Imagem do gride')),
                ('highlight', models.BooleanField(default=False, verbose_name='Destaque')),
                ('highlight_image', models.ImageField(upload_to=b'oferta/', verbose_name='Imagem Destaque')),
                ('bought', models.IntegerField(default=0, verbose_name='Comprados')),
                ('bought_virtual', models.IntegerField(verbose_name='Quantidade virtual')),
                ('max_by_user', models.IntegerField(null=True, verbose_name='M\xe1ximo por pessoa', blank=True)),
                ('percent_by_site', models.DecimalField(verbose_name='Percentual do site', max_digits=10, decimal_places=2)),
                ('percent_cashback', models.DecimalField(verbose_name='Percentual de CashBack', max_digits=10, decimal_places=2)),
                ('description', tinymce.models.HTMLField(verbose_name='Descri\xe7\xe3o')),
                ('when_to_use', tinymce.models.HTMLField()),
                ('how_to_use', tinymce.models.HTMLField()),
                ('good_to_know', tinymce.models.HTMLField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('affiliate', models.ForeignKey(verbose_name='Franqueado', blank=True, to='account.Affiliate', null=True)),
                ('city', models.ForeignKey(verbose_name='Cidade', to='account.City')),
                ('interests', models.ManyToManyField(to='offer.Interest', verbose_name='Interesses')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Sub T\xedtulo')),
                ('old_price', models.DecimalField(null=True, verbose_name='Pre\xe7o sem desconto', max_digits=10, decimal_places=2, blank=True)),
                ('new_price', models.DecimalField(verbose_name='Pre\xe7o com desconto', max_digits=10, decimal_places=2)),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('start_time', models.DateTimeField(verbose_name='Come\xe7a em')),
                ('end_time', models.DateTimeField(verbose_name='Termina em')),
                ('date_expiration', models.DateField(verbose_name='Expira em')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('filial', models.ForeignKey(related_name=b'offers', to='account.Filial')),
                ('offer', models.ForeignKey(related_name=b'options', to='offer.Offer')),
            ],
            options={
                'verbose_name': 'Op\xe7\xe3o',
                'verbose_name_plural': 'Op\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PromotionCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255, verbose_name='C\xf3digo')),
                ('discount', models.DecimalField(verbose_name='Desconto', max_digits=10, decimal_places=2)),
                ('start_time', models.DateTimeField(verbose_name='Come\xe7a em')),
                ('end_time', models.DateTimeField(verbose_name='Termina em')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, max_length=255, blank=True)),
                ('category', models.ForeignKey(related_name=b'subcategories', to='offer.Category')),
            ],
            options={
                'verbose_name': 'SubCategoria',
                'verbose_name_plural': 'SubCategorias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='offer',
            name='subcategory',
            field=models.ForeignKey(verbose_name='Sub Categoria', to='offer.SubCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='offer',
            field=models.ForeignKey(related_name=b'images', to='offer.Offer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(related_name=b'categories', to='offer.Type'),
            preserve_default=True,
        ),
    ]
