# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-14 04:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0036_auto_20170109_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(choices=[('iden', '\u8ba4\u8bc1'), ('sign', '\u5408\u7ea6'), ('', '\u652f\u4ed8'), ('', '\u6536\u8d27'), ('', '\u9000\u8d27')], max_length=100, verbose_name='\u6d88\u606f\u7c7b\u578b')),
                ('subject', models.CharField(default='', max_length=255, verbose_name='\u6d88\u606f\u4e3b\u9898')),
                ('content', models.TextField(default='', verbose_name='\u6d88\u606f\u6b63\u6587')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u63a8\u9001\u7ed9\u7528\u6237')),
            ],
            options={
                'ordering': ('pk',),
                'verbose_name': '\u7528\u6237\u6d88\u606f',
                'verbose_name_plural': '\u7528\u6237\u6d88\u606f',
            },
        ),
    ]
