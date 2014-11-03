# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0002_report_report_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='notificated_today',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
