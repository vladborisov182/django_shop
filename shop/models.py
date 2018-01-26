from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=35, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=35, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория')
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', verbose_name='Производитель')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    year_of_issue = models.IntegerField(verbose_name='Год выпуска')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара')
    description = models.TextField(max_length=300, verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    price_with_discount = models.IntegerField(default=0, verbose_name='Цена со скидкой')
    wishlisted = models.ManyToManyField(User, blank=True, related_name='wishlist_items', verbose_name='В избранном')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        price = self.price
        discount = self.discount
        self.price_with_discount = int(price) - (int(price) * discount / 100)
        super(Product, self).save(*args, **kwargs)
