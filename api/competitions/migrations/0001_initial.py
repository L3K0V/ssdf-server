# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20151021_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=1, default='C', choices=[('C', 'Couples'), ('I', 'Individuals')])),
                ('description', models.TextField()),
                ('event', models.ForeignKey(to='events.Event', related_name='competitions')),
            ],
        ),
    ]
