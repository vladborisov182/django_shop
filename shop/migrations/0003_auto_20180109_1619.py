# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-09 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180109_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='Ссылка'),
        ),
    ]
