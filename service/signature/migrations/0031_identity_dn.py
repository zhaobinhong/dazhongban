# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0030_auto_20161228_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='dn',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='DN'),
        ),
    ]
