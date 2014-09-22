# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='T\xedtulo'),
            preserve_default=False,
        ),
    ]
