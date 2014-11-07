# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0006_auto_20141107_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='koie',
            name='firewood',
            field=models.IntegerField(verbose_name='firewood', default=0),
            preserve_default=True,
        ),
    ]
