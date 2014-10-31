# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0003_auto_20141027_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('damage', models.TextField(null=True, blank=True, verbose_name='skade')),
                ('importance', models.IntegerField(null=True, blank=True)),
                ('fixed_date', models.DateTimeField(null=True, blank=True)),
                ('damaged_koie', models.ForeignKey(to='koie.Koie', null=True, blank=True, related_name='damaged_koie')),
                ('reporten', models.ForeignKey(to='koie.Report', null=True, blank=True, related_name='reporten')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
