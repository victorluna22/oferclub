# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0008_auto_20140922_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='slug',
            field=models.SlugField(default='', unique=True, max_length=255, blank=True),
            preserve_default=False,
        ),
    ]
