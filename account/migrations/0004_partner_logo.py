# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_affiliate_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='logo',
            field=models.ImageField(upload_to=b'parceiro/', null=True, verbose_name='Logomarca', blank=True),
            preserve_default=True,
        ),
    ]
