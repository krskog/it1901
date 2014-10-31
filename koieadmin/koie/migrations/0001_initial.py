# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('damage', models.TextField(verbose_name='skade', blank=True, null=True)),
                ('importance', models.IntegerField(blank=True, null=True)),
                ('fixed_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Koie',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='koie name')),
                ('address', models.CharField(max_length=200, verbose_name='koie address')),
                ('location', models.CharField(max_length=50, verbose_name='location')),
                ('latitude', models.DecimalField(max_digits=10, decimal_places=5, verbose_name='latitude')),
                ('longitude', models.DecimalField(max_digits=10, decimal_places=5, verbose_name='longitude')),
                ('num_beds', models.IntegerField(default=0, verbose_name='beds')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('report', models.TextField(verbose_name='end of stay report')),
                ('reported_date', models.DateTimeField(blank=True, null=True)),
                ('read_date', models.DateTimeField(blank=True, null=True)),
                ('firewood_status', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('rent_date', models.DateField(verbose_name='rent date')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, verbose_name='timestamp for order')),
                ('beds', models.IntegerField(verbose_name='number of beds')),
                ('koie_ordered', models.ForeignKey(to='koie.Koie', related_name='ordered koie')),
                ('ordered_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='ordered by')),
            ],
            options={
                'get_latest_by': 'id',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='report',
            name='reservation',
            field=models.ForeignKey(to='koie.Reservation', related_name='reservation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='damage',
            name='damaged_koie',
            field=models.ForeignKey(to='koie.Koie', blank=True, null=True, related_name='damaged_koie'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='damage',
            name='reporten',
            field=models.ForeignKey(to='koie.Report', blank=True, null=True, related_name='reporten'),
            preserve_default=True,
        ),
    ]
