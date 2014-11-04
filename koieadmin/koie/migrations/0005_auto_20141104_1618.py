# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0004_damage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'get_latest_by': 'reported_date'},
        ),
        migrations.AddField(
            model_name='report',
            name='notification_date',
            field=models.DateField(default=datetime.date(2014, 11, 4), auto_now=True),
            preserve_default=False,
        ),
    ]
