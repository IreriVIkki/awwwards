# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-14 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_auto_20181013_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
