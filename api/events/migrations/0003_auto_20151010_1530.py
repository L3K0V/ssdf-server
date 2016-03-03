# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20151005_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTrack',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('C', 'Couples'), ('I', 'Individuals')], default='C', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='EventTrackLevel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('level', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('IA', 'Intermidiate-Advanced'), ('A', 'Advanced'), ('AP', 'Advanced Plus')], default='B', max_length=2)),
                ('track', models.ForeignKey(to='events.EventTrack', related_name='levels')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='eventperson',
            unique_together=set([('event', 'person')]),
        ),
        migrations.AddField(
            model_name='event',
            name='tracks',
            field=models.ManyToManyField(to='events.EventTrack', related_name='events'),
        ),
        migrations.AlterUniqueTogether(
            name='eventtracklevel',
            unique_together=set([('track', 'level')]),
        ),
    ]
