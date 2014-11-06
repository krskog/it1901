# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0004_damage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('facility', models.CharField(verbose_name='facility name', max_length=50)),
                ('info', models.TextField(verbose_name='facility name', blank=True, null=True)),
                ('koien', models.ManyToManyField(related_name='koien', to='koie.Koie', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'get_latest_by': 'reported_date'},
        ),
    ]
