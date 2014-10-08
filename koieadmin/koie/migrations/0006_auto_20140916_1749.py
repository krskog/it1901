# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('koie', '0005_auto_20140916_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rent_start', models.DateField(verbose_name='rent start')),
                ('rent_end', models.DateField(verbose_name='rent end')),
                ('ordered_date', models.DateTimeField(auto_now_add=True, verbose_name='timestamp for order')),
                ('koie_ordered', models.ForeignKey(related_name='ordered koie', to='koie.Koie')),
                ('ordered_by', models.ForeignKey(related_name='ordered by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
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
