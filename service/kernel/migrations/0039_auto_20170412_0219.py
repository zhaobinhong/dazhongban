# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-12 02:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kernel', '0038_auto_20170412_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relancement',
            name='approval',
        ),
        migrations.RemoveField(
            model_name='relancement',
            name='order',
        ),
    ]
