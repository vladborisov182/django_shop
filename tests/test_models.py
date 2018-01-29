from django.db import IntegrityError
from django.test import TestCase
from shop.models import Category, Manufacturer, Product

def create_product(name, slug): 
    category = Category.objects.create(name='Test category')
    manufacturer = Manufacturer.objects.create(name='Test manufacturer')
    Product.objects.create(name=name, image='1.jpg', category=category, manufacturer=manufacturer, 
    year_of_issue=2017, description='test description', price=1000, discount=10, price_with_discount=0, available=True, slug=slug)


class ManufacturerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Manufacturer.objects.create(name='Asus')

    def test_name_label(self):
        manufacturer = Manufacturer.objects.get(name='Asus')
        field_label = manufacturer._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название')

    def test_name_max_length(self):
        manufacturer = Manufacturer.objects.get(name='Asus')
        max_length = manufacturer._meta.get_field('name').max_length
        self.assertEquals(max_length, 35)

    def test_object_name_is_name(self):
        manufacturer = Manufacturer.objects.get(name='Asus')
        expected_object_name = (manufacturer.name)
        self.assertEquals(expected_object_name, str(manufacturer))

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Ноутбуки')

    def test_name_label(self):
        category = Category.objects.get(name='Ноутбуки')
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название')

    def test_name_max_length(self):
        category = Category.objects.get(name='Ноутбуки')
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 35)

    def test_object_name_is_name(self):
        category = Category.objects.get(name='Ноутбуки')
        expected_object_name = (category.name)
        self.assertEquals(expected_object_name, str(category))


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        create_product("Test", 'test')       

    def test_name_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название')

    def test_category_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('category').verbose_name
        self.assertEquals(field_label,'Категория')

    def test_manufacturer_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('manufacturer').verbose_name
        self.assertEquals(field_label,'Производитель')

    def test_year_of_issue_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('year_of_issue').verbose_name
        self.assertEquals(field_label,'Год выпуска')

    def test_slug_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('slug').verbose_name
        self.assertEquals(field_label,'Ссылка')

    def test_image_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('image').verbose_name
        self.assertEquals(field_label,'Изображение товара')

    def test_description_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'Описание')

    def test_price_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label,'Цена')

    def test_discount_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('discount').verbose_name
        self.assertEquals(field_label,'Скидка')

    def test_price_with_discount_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('price_with_discount').verbose_name
        self.assertEquals(field_label,'Цена со скидкой')

    def test_available_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('available').verbose_name
        self.assertEquals(field_label,'Доступен')

    def test_wishlisted_label(self):
        product = Product.objects.get(name='Test')
        field_label = product._meta.get_field('wishlisted').verbose_name
        self.assertEquals(field_label,'В избранном')

    def test_name_max_length(self):
        product = Product.objects.get(name='Test')
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_slug_max_length(self):
        product = Product.objects.get(name='Test')
        max_length = product._meta.get_field('slug').max_length
        self.assertEquals(max_length, 200)

    def test_description_max_length(self):
        product = Product.objects.get(name='Test')
        max_length = product._meta.get_field('description').max_length
        self.assertEquals(max_length, 300)

    def test_object_name_is_name(self):
        product = Product.objects.get(name='Test')
        expected_object_name = (product.name)
        self.assertEquals(expected_object_name, str(product))

    def test_get_absolute_url(self):
        create_product('Test product for detail', 'test-product-for-detail')
        product = Product.objects.get(name='Test product for detail')
        product_id = str(product.id)
        product_slug = str(product.slug)
        self.assertEquals(product.get_absolute_url(), '/products/' + product_id + '/' + product_slug + '/')

    def test_unique_slug(self):
        create_product('Test product unique slug 1', 'test-product-unique-slug-1')
        p1 = Product.objects.get(name='Test product unique slug 1') 
        p1.save()  
        create_product('Test product unique slug 2', 'test-product-unique-slug-1')
        p2 = Product.objects.get(name='Test product unique slug 2')   
        self.assertRaises(IntegrityError, p2.save())

    def test_price_with_discount(self):
        create_product('Test product', 'test-product')
        product = Product.objects.get(name='Test product')
        price_with_discount = getattr(product, 'price_with_discount')
        self.assertEquals(price_with_discount, 900)
