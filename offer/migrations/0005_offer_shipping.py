# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0004_auto_20141031_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='shipping',
            field=models.BooleanField(default=0, verbose_name='Cobra Frete?'),
            preserve_default=True,
        ),
    ]
