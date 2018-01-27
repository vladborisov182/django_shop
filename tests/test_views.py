from cart.views import cart_add, cart_detail, cart_remove
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve
from shop.models import Category, Manufacturer, Product


class ProductListViewTest(TestCase):

    def test_product_list_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/products/') 
        self.assertEqual(resp.status_code, 200)

    def test_product_list_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)

    def test_product_list_view_uses_correct_template(self):
        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'shop/product/list.html')


class WishListViewTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='12345') 
        test_user.save()
        login = self.client.login(username='testuser', password='12345')

    def test_wishlist_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/wishlist/') 
        self.assertEqual(resp.status_code, 200)

    def test_wishlist_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('wishlist:WishlistDetail'))
        self.assertEqual(resp.status_code, 200)

    def test_wishlist_view_uses_correct_template(self):
        resp = self.client.get(reverse('wishlist:WishlistDetail'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'wishlist/wishlist_items.html')

class CallbackViewTest(TestCase):

    def test_callback_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/callback/') 
        self.assertEqual(resp.status_code, 200)

    def test_callback_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('callback:Callback'))
        self.assertEqual(resp.status_code, 200)

    def test_callback_view_uses_correct_template(self):
        resp = self.client.get(reverse('callback:Callback'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'callback/callbackform.html')


class CartViewTest(TestCase):

    def test_cart_detail_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/cart/') 
        self.assertEqual(resp.status_code, 200)

    def test_cart_detail_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('cart:CartDetail'))
        self.assertEqual(resp.status_code, 200)

    def test_cart_detail_view_uses_correct_template(self):
        resp = self.client.get(reverse('cart:CartDetail'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'cart/cart_detail.html')

class ShopViewTest(TestCase):

    def test_shop_pdoduct_list_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/products/') 
        self.assertEqual(resp.status_code, 200)

    def test_shop_pdoduct_list_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)

    def test_shop_pdoduct_list_view_uses_correct_template(self):
        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'shop/product/list.html')

    def test_shop_product_detail_view_uses_correct_template(self): 
        category = Category.objects.create(name='Смартфоны')
        manufacturer = Manufacturer.objects.create(name='Apple')
        Product.objects.create(name='Test product smartphone', image='1.jpg', category=category, manufacturer=manufacturer, 
        year_of_issue=2017, description='test description', price=1000, discount=10, price_with_discount=0, available=True, slug='test-product-smartphone')

        resp = self.client.get('/products/1/test-product-smartphone/') 
        self.assertEqual(resp.status_code, 200)
