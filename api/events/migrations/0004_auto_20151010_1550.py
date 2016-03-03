# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20151010_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tracks',
        ),
        migrations.AddField(
            model_name='eventtrack',
            name='event',
            field=models.ForeignKey(related_name='track', default=0, to='events.Event'),
            preserve_default=False,
        ),
    ]
