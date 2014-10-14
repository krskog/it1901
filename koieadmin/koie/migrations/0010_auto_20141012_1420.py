# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0009_auto_20140923_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koie',
            name='zip_code',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(0)]),
        ),
    ]
