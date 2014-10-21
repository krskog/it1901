# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0008_report_reported_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='koie',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='koie',
            name='latitude',
            field=models.DecimalField(default=1.1, max_digits=10, verbose_name='latitude', decimal_places=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='koie',
            name='longitude',
            field=models.DecimalField(default=1.1, max_digits=10, verbose_name='longitude', decimal_places=5),
            preserve_default=False,
        ),
    ]
