# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0012_auto_20141113_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firewood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('firewood_status', models.IntegerField(verbose_name='firewood status')),
                ('koie', models.OneToOneField(verbose_name='koie', to='koie.Koie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
