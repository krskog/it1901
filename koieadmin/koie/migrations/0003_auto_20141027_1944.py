# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0002_report_read'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='read',
        ),
        migrations.AddField(
            model_name='report',
            name='read_date',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='reported_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
