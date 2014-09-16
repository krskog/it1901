# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0003_auto_20140916_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='rent_date',
        ),
        migrations.AddField(
            model_name='reservation',
            name='rent_end',
            field=models.DateField(verbose_name='rent end', default=datetime.date(2014, 9, 16)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='rent_start',
            field=models.DateField(verbose_name='rent start', default=datetime.date(2014, 9, 16)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='koie',
            name='location',
            field=models.CharField(verbose_name='location', max_length=50),
        ),
        migrations.AlterField(
            model_name='koie',
            name='num_beds',
            field=models.IntegerField(verbose_name='beds', default=0),
        ),
        migrations.AlterField(
            model_name='koie',
            name='zip_code',
            field=models.IntegerField(verbose_name='zip code', max_length=4),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='timestamp for order'),
        ),
    ]
