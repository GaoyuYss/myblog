# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0005_auto_20181206_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='icon',
            field=models.ImageField(null=True, upload_to='article'),
        ),
    ]