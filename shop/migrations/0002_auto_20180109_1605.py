# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-09 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='slug',
        ),
    ]
