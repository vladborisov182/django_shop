# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-15 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20180114_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_after_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена со скидкой'),
        ),
    ]
