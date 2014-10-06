# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0010_auto_20140925_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='category',
            field=models.ForeignKey(default='', verbose_name='Categoria', to='offer.Category'),
            preserve_default=False,
        ),
    ]
