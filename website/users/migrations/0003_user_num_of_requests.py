# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160802_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='num_of_requests',
            field=models.PositiveIntegerField(default=0, verbose_name='Number of Requests'),
        ),
    ]
