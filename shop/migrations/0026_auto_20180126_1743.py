# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20180126_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара'),
        ),
    ]
