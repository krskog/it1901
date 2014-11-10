# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koie', '0008_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateField(verbose_name='due date')),
                ('message', models.TextField(verbose_name='message', max_length=3000)),
                ('koie', models.ForeignKey(related_name='koie', to='koie.Koie')),
                ('reservation', models.ForeignKey(null=True, to='koie.Reservation', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
