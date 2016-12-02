# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signature',
            options={'verbose_name': '\u7b7e\u540d\u8bc1\u4e66', 'verbose_name_plural': '\u7b7e\u540d\u8bc1\u4e66'},
        ),
        migrations.AddField(
            model_name='signature',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='signature',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='signature',
            name='signs',
            field=models.TextField(default='', verbose_name='\u8bc1\u4e66\u5bc6\u6587'),
        ),
    ]
