# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
