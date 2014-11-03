# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_notification',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
