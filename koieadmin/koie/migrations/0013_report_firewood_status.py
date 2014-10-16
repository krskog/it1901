# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0012_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='firewood_status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
