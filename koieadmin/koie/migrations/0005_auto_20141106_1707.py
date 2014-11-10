# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0004_damage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firewood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('firewood_status', models.IntegerField()),
                ('firewood_capacity', models.IntegerField()),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('koie', models.ForeignKey(to='koie.Koie', related_name='koie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'get_latest_by': 'reported_date'},
        ),
        migrations.AddField(
            model_name='koie',
            name='next_user_message',
            field=models.TextField(verbose_name='Utstyrsmelding', blank=True, null=True),
            preserve_default=True,
        ),
    ]
