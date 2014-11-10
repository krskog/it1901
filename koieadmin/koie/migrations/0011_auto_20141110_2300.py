# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0010_auto_20141110_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='koie_ordered',
            field=models.ForeignKey(verbose_name='koie', to='koie.Koie'),
        ),
    ]
