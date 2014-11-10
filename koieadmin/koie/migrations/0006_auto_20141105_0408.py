# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0005_auto_20141103_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='koien',
        ),
        migrations.AddField(
            model_name='facility',
            name='koier',
            field=models.ManyToManyField(null=True, related_name='koier', blank=True, to='koie.Koie'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='facility',
            name='facility',
            field=models.CharField(max_length=50, verbose_name='facility_name'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='info',
            field=models.TextField(null=True, blank=True, verbose_name='facility_info'),
        ),
    ]
