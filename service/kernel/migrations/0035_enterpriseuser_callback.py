# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-17 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0034_auto_20170115_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterpriseuser',
            name='callback',
            field=models.URLField(blank=True, null=True, verbose_name='\u56de\u8c03URL'),
        ),
    ]
