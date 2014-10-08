# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0007_report_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reported_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2014, 9, 16)),
            preserve_default=False,
        ),
    ]
