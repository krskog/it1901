# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0008_report_reported_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koie',
            name='zip_code',
            field=models.DecimalField(verbose_name='zip code', max_digits=4, decimal_places=0),
        ),
    ]
