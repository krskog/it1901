# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0002_auto_20140916_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('reservation', models.ForeignKey(related_name='reservation', to='koie.Reservation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='koie',
            name='house_no',
        ),
        migrations.AlterField(
            model_name='koie',
            name='address',
            field=models.CharField(max_length=200, verbose_name='koie address'),
        ),
        migrations.AlterField(
            model_name='koie',
            name='name',
            field=models.CharField(max_length=50, verbose_name='koie name'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='koie_ordered',
            field=models.ForeignKey(related_name='ordered koie', to='koie.Koie'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='ordered_by',
            field=models.ForeignKey(related_name='ordered by', to=settings.AUTH_USER_MODEL),
        ),
    ]
