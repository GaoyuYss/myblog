# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-07 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0011_auto_20181207_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(db_column='简短描述', max_length=200, null=True),
        ),
    ]