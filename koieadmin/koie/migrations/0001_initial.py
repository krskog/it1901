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
            name='Koie',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='koie name', max_length=50)),
                ('address', models.CharField(verbose_name='koie address', max_length=200)),
                ('location', models.CharField(verbose_name='location', max_length=50)),
                ('latitude', models.DecimalField(verbose_name='latitude', decimal_places=5, max_digits=10)),
                ('longitude', models.DecimalField(verbose_name='longitude', decimal_places=5, max_digits=10)),
                ('num_beds', models.IntegerField(default=0, verbose_name='beds')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('report', models.TextField(verbose_name='end of stay report')),
                ('reported_date', models.DateTimeField(auto_now_add=True)),
                ('firewood_status', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('rent_date', models.DateField(verbose_name='rent date')),
                ('ordered_date', models.DateTimeField(verbose_name='timestamp for order', auto_now_add=True)),
                ('beds', models.IntegerField(verbose_name='number of beds')),
                ('koie_ordered', models.ForeignKey(related_name='ordered koie', to='koie.Koie')),
                ('ordered_by', models.ForeignKey(related_name='ordered by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'id',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='report',
            name='reservation',
            field=models.ForeignKey(related_name='reservation', to='koie.Reservation'),
            preserve_default=True,
        ),
    ]
