# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20151010_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventtracklevel',
            name='name',
        ),
        migrations.AlterField(
            model_name='eventtrack',
            name='event',
            field=models.ForeignKey(to='events.Event', related_name='tracks'),
        ),
    ]
