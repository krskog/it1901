# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0004_auto_20140916_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='reservation',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='koie_ordered',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='ordered_by',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
