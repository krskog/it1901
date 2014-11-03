# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0004_damage'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='notificated_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
