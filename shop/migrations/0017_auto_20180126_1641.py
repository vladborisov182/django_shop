# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20180126_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
    ]
