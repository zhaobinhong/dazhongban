# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0016_auto_20161206_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='alias',
            field=models.CharField(default='', max_length=100, verbose_name='\u5907\u6ce8\u522b\u540d'),
        ),
    ]
