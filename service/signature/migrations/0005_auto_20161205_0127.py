# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 01:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signature', '0004_identity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identity',
            name='created_at',
        ),
        migrations.AddField(
            model_name='identity',
            name='bankcard',
            field=models.CharField(default='', max_length=100, verbose_name='\u94f6\u884c\u5361\u53f7'),
        ),
        migrations.AddField(
            model_name='identity',
            name='card_type',
            field=models.CharField(default='', max_length=100, verbose_name='\u5361\u7247\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='identity',
            name='expired',
            field=models.CharField(default='', max_length=100, verbose_name='\u8fc7\u671f\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='identity',
            name='id_card',
            field=models.CharField(default='', max_length=100, verbose_name='\u8eab\u4efd\u8bc1'),
        ),
        migrations.AddField(
            model_name='identity',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='\u59d3\u540d'),
        ),
        migrations.AddField(
            model_name='identity',
            name='phone',
            field=models.CharField(default='', max_length=100, verbose_name='\u7535\u8bdd'),
        ),
        migrations.AlterField(
            model_name='identity',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='identity', to=settings.AUTH_USER_MODEL),
        ),
    ]
