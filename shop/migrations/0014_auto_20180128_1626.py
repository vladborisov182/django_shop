# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-28 16:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_product_wishlisted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=35, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(db_index=True, max_length=35, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_with_discount',
            field=models.IntegerField(default=0, verbose_name='Цена со скидкой'),
        ),
        migrations.AlterField(
            model_name='product',
            name='wishlisted',
            field=models.ManyToManyField(blank=True, related_name='wishlist_items', to=settings.AUTH_USER_MODEL, verbose_name='В избранном'),
        ),
    ]
