# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0009_notification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='damage',
            options={'verbose_name': 'damage', 'verbose_name_plural': 'damages'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name': 'facility', 'verbose_name_plural': 'facilities'},
        ),
        migrations.AlterModelOptions(
            name='koie',
            options={'verbose_name': 'koie', 'verbose_name_plural': 'koies'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'notification', 'verbose_name_plural': 'notifications'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'report', 'verbose_name_plural': 'reports', 'get_latest_by': 'reported_date'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'reservation', 'verbose_name_plural': 'reservations', 'get_latest_by': 'id'},
        ),
        migrations.RemoveField(
            model_name='damage',
            name='reporten',
        ),
        migrations.AddField(
            model_name='damage',
            name='report',
            field=models.ForeignKey(blank=True, verbose_name='report', null=True, to='koie.Report'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='damage',
            name='damage',
            field=models.TextField(verbose_name='damage', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='damage',
            name='damaged_koie',
            field=models.ForeignKey(blank=True, verbose_name='damaged koie', null=True, to='koie.Koie'),
        ),
        migrations.AlterField(
            model_name='damage',
            name='fixed_date',
            field=models.DateTimeField(verbose_name='fixed date', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='damage',
            name='importance',
            field=models.IntegerField(verbose_name='importance', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='facility',
            field=models.CharField(verbose_name='facility', max_length=50),
        ),
        migrations.AlterField(
            model_name='facility',
            name='info',
            field=models.TextField(verbose_name='description', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='koie',
            name='facilities',
            field=models.ManyToManyField(verbose_name='facilities', blank=True, null=True, to='koie.Facility'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='koie',
            field=models.ForeignKey(verbose_name='koie', to='koie.Koie'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='reservation',
            field=models.ForeignKey(blank=True, verbose_name='reservation', null=True, to='koie.Reservation'),
        ),
        migrations.AlterField(
            model_name='report',
            name='firewood_status',
            field=models.IntegerField(verbose_name='firewood status'),
        ),
        migrations.AlterField(
            model_name='report',
            name='notification_date',
            field=models.DateField(verbose_name='notification sent date', auto_now=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='read_date',
            field=models.DateTimeField(verbose_name='report read date', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='reported_date',
            field=models.DateTimeField(verbose_name='reported date', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='reservation',
            field=models.ForeignKey(verbose_name='reservation', to='koie.Reservation'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='koie_ordered',
            field=models.ForeignKey(verbose_name='koie ordered', to='koie.Koie'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='ordered_by',
            field=models.ForeignKey(verbose_name='ordered by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='ordered_date',
            field=models.DateTimeField(verbose_name='reservation registered', auto_now_add=True),
        ),
    ]
