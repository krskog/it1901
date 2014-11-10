# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0005_auto_20141106_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('facility', models.CharField(verbose_name='facility_name', max_length=50)),
                ('info', models.TextField(verbose_name='facility_info', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='firewood',
            name='koie',
        ),
        migrations.DeleteModel(
            name='Firewood',
        ),
        migrations.RemoveField(
            model_name='koie',
            name='next_user_message',
        ),
        migrations.AddField(
            model_name='koie',
            name='facilities',
            field=models.ManyToManyField(to='koie.Facility', blank=True, related_name='facilities', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='notification_date',
            field=models.DateField(auto_now=True, null=True),
            preserve_default=True,
        ),
    ]
