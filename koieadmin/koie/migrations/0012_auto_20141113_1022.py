# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0011_auto_20141110_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='firewood_status',
            field=models.IntegerField(verbose_name='firewood status', null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='report',
            field=models.TextField(verbose_name='comments about your stay', null=True),
        ),
    ]
