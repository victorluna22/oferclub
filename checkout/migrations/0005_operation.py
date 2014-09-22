# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_partner_logo'),
        ('checkout', '0004_auto_20140922_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_operation', models.BooleanField(default=0, verbose_name='Tipo', choices=[(0, b'D\xc3\xa9bito'), (1, b'Cr\xc3\xa9dito')])),
                ('value', models.DecimalField(verbose_name='valor', max_digits=10, decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Gerado em')),
                ('user', models.ForeignKey(related_name=b'operations', verbose_name='usu\xe1rio', to='account.OferClubUser')),
            ],
            options={
                'verbose_name': 'Opera\xe7\xe3o',
                'verbose_name_plural': 'Opera\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
    ]
