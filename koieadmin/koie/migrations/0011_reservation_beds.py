# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0010_auto_20141012_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='beds',
            field=models.IntegerField(verbose_name='number of beds', default=1),
            preserve_default=False,
        ),
    ]
