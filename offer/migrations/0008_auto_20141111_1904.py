# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='slug',
            field=models.SlugField(default='', max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='good_to_know',
            field=tinymce.models.HTMLField(verbose_name='Bom saber'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='how_to_use',
            field=tinymce.models.HTMLField(verbose_name='Como usar'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='max_by_user',
            field=models.IntegerField(help_text='Deixar vazio para n\xe3o ter limite', null=True, verbose_name='M\xe1ximo por pessoa', blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='when_to_use',
            field=tinymce.models.HTMLField(verbose_name='Quando usar'),
        ),
    ]
