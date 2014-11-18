# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0013_firewood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firewood',
            name='firewood_status',
            field=models.IntegerField(null=True, verbose_name='firewood status', blank=True),
        ),
    ]
