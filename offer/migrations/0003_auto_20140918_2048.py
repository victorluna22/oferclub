# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_offer_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='offer',
            options={'verbose_name': 'Oferta', 'verbose_name_plural': 'Ofertas'},
        ),
        migrations.AddField(
            model_name='option',
            name='offer',
            field=models.ForeignKey(default='', to='offer.Offer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='bought',
            field=models.IntegerField(default=0, verbose_name='Comprados'),
        ),
    ]
