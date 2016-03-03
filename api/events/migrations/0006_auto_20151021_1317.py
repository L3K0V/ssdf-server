# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20151010_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtrack',
            name='name',
            field=models.CharField(unique=True, max_length=64),
        ),
    ]
