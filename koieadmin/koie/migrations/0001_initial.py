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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('num_beds', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('rent_date', models.DateField()),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('koie_ordered', models.ForeignKey(to='koie.Koie', related_name='Ordered koie')),
                ('ordered_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='Ordered by')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
