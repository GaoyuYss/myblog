# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-07 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0013_auto_20181207_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(db_column='栏目编号', default='1', max_length=5),
        ),
    ]
