# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtracklevelrate',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='scheduleitemrate',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]