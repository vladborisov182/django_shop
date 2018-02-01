from shop.models import Category, Manufacturer, Product


def create_product(name, slug): 
    category = Category.objects.create(name='Test category')
    manufacturer = Manufacturer.objects.create(name='Test manufacturer')
    Product.objects.create(name=name, image='1.jpg', category=category, manufacturer=manufacturer, 
    year_of_issue=2017, description='test description', price=1000, discount=10, price_with_discount=0, available=True, slug=slug) 
