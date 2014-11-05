# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0006_auto_20141105_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='koier',
        ),
        migrations.AddField(
            model_name='koie',
            name='facilities',
            field=models.ManyToManyField(blank=True, to='koie.Facility', null=True, related_name='facilities'),
            preserve_default=True,
        ),
    ]
