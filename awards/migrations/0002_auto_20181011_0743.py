# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='awards.Post'),
        ),
    ]
