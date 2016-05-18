# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 06:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.CharField(default=datetime.datetime(2016, 5, 18, 6, 19, 55, 636237, tzinfo=utc), help_text='meta\u63cf\u8ff0', max_length=255, verbose_name='Meta \u63cf\u8ff0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u540d\u79f0'),
        ),
    ]
