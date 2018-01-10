from django.db import models
from django.core.urlresolvers import reverse

class Manufacturer(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория')
    manufacturer = models.ForeignKey(Manufacturer, related_name='products', verbose_name='Производитель')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    year_of_issue = models.IntegerField(verbose_name='Год выпуска')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])
