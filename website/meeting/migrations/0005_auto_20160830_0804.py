# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_auto_20160813_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='applicator',
        ),
        migrations.AlterModelOptions(
            name='applicator',
            options={'ordering': ('request_date', 'company_name'), 'verbose_name': 'Applicator', 'verbose_name_plural': 'Applicators'},
        ),
        migrations.AddField(
            model_name='applicator',
            name='date_has_been_set',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applicator',
            name='lastname',
            field=models.CharField(default='lastname', max_length=200, verbose_name='Lastname'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicator',
            name='phone',
            field=models.CharField(default='23232323', max_length=200, verbose_name='Phone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicator',
            name='rank',
            field=models.CharField(default='CEO', max_length=200, verbose_name='Rank'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicator',
            name='request_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicator',
            name='set_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicator',
            name='address',
            field=models.CharField(blank=True, max_length=400, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='applicator',
            name='city',
            field=models.CharField(blank=True, max_length=50, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='applicator',
            name='company_name',
            field=models.CharField(max_length=200, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='applicator',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='applicator',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='applicator',
            name='website',
            field=models.URLField(blank=True, verbose_name='Website'),
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
