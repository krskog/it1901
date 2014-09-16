# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0006_auto_20140916_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report',
            field=models.TextField(verbose_name='end of stay report', default=0),
            preserve_default=False,
        ),
    ]
