# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='member')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('level', models.CharField(default='B', max_length=2, choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('IA', 'Intermidiate-Advanced'), ('A', 'Advanced'), ('AP', 'Advanced Plus')])),
                ('member', models.OneToOneField(to='members.Member', related_name='person')),
            ],
        ),
    ]
