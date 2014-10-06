# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_oferclubuser_inviter'),
        ('offer', '0012_remove_offer_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='city',
            field=models.ForeignKey(default=2, verbose_name='Cidade', to='account.City'),
            preserve_default=False,
        ),
    ]
