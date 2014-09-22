# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_remove_offer_percent_by_affiliate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Imagem', 'verbose_name_plural': 'Imagens'},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'verbose_name': 'Op\xe7\xe3o', 'verbose_name_plural': 'Op\xe7\xf5es'},
        ),
    ]
