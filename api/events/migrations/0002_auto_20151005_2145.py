# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPerson',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(default='S', max_length=1, choices=[('T', 'Teacher'), ('S', 'Student'), ('D', 'DJ'), ('G', 'Guest')])),
                ('event', models.ForeignKey(related_name='person', to='events.Event')),
                ('person', models.ForeignKey(related_name='event', to='members.Person')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='people',
            field=models.ManyToManyField(related_name='events', to='members.Person', through='events.EventPerson'),
        ),
    ]
