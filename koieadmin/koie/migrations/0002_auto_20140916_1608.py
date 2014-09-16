# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='koie',
            name='house_no',
            field=models.CharField(default='1', max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='koie',
            name='location',
            field=models.CharField(default='place', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='koie',
            name='zip_code',
            field=models.IntegerField(default=1324, max_length=4),
            preserve_default=False,
        ),
    ]
