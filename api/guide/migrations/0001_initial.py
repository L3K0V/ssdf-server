# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20151021_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=48)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('event', models.ForeignKey(to='events.Event', related_name='items')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.TextField()),
                ('from_datetime', models.DateTimeField()),
                ('to_datetime', models.DateTimeField()),
                ('guide_item', models.ForeignKey(to='guide.GuideItem', related_name='hours')),
            ],
        ),
    ]
