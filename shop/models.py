from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''
        при помощи этой функции мы получаем абсолютный адрес товара или категории, где в качестве первого параметра вьюха, а в args мы указываем параметры url в том порядке, в котором написали в файле роутинга urls.py
        '''
        return reverse('shop:ProductListByCategory', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    year_of_issue = models.IntegerField(verbose_name='Год выпуска')
    manufacturer = models.CharField(blank=True, null=True, max_length=200, verbose_name='Производитель')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    discount = models.IntegerField(default=0, verbose_name='Скидка')
    stock = models.PositiveIntegerField(verbose_name='На складе')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])
