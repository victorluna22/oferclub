# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferclubuser',
            name='inviter',
            field=models.ForeignKey(blank=True, to='account.OferClubUser', null=True),
            preserve_default=True,
        ),
    ]
