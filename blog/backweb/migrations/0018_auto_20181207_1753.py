# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-07 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0017_auto_20181207_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.ForeignKey(db_column='栏目编号', on_delete=django.db.models.deletion.CASCADE, to='backweb.Type'),
        ),
    ]