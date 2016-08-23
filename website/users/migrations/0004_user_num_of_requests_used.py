# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-21 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_num_of_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='num_of_requests_used',
            field=models.PositiveIntegerField(default=0, verbose_name='Number of Requests'),
        ),
    ]