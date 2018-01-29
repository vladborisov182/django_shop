from cart.views import cart_add, cart_detail, cart_remove
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve
from shop.models import Category, Manufacturer, Product


def create_product(name, slug): 
    category = Category.objects.create(name='Test category')
    manufacturer = Manufacturer.objects.create(name='Test manufacturer')
    Product.objects.create(name=name, image='1.jpg', category=category, manufacturer=manufacturer, 
    year_of_issue=2017, description='test description', price=1000, discount=10, price_with_discount=0, available=True, slug=slug) 


class WishListViewTest(TestCase):

    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_wishlist_view_for_anon(self): 
        self.client.logout()
        resp = self.client.get('/wishlist/') 
        self.assertEqual(resp.status_code, 302)

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

    def test_wishlist_view_with_no_products(self):
        resp = self.client.get(reverse('wishlist:WishlistDetail'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Список избранного пуст')
        self.assertQuerysetEqual(resp.context['products'], [])

    def test_wishlist_view_with_a_past_product(self): 
        create_product('Test product for wishlist', 'test')

        product = Product.objects.get(name='Test product for wishlist')

        user1 = User.objects.create()
        product.wishlisted.add(user1)
        wishlist_items = user1.wishlist_items.all()

        self.assertQuerysetEqual(wishlist_items, [
            '<Product: Test product for wishlist>'
        ])

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

    def test_cart_view_with_no_products(self):
        resp = self.client.get(reverse('cart:CartDetail'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Корзина пуста')
        self.assertQuerysetEqual(resp.context['cart'], [])

class ShopViewTest(TestCase):

    def test_shop_view_with_no_products(self):
        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Товары отсутствуют')
        self.assertQuerysetEqual(resp.context['products'], [])

    def test_shop_view_with_a_past_product(self): 
        create_product('Test product for past 1', 'test')

        resp = self.client.get(reverse('shop:ProductList'))
        self.assertQuerysetEqual(resp.context['products'], [
            '<Product: Test product for past 1>'
        ])

    def test_shop_last_product_view_with_no_products(self):

        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)
        self.assertQuerysetEqual(resp.context['last_products'], [])
    
    def test_shop_view_with_four_last_products(self):
        for i in range (1, 5):
            create_product('Test product for last ' + str(i), 'test') 

        resp = self.client.get(reverse('shop:ProductList'))
        self.assertQuerysetEqual(resp.context['products'], [
            '<Product: Test product for last 4>',
            '<Product: Test product for last 3>',
            '<Product: Test product for last 2>',
            '<Product: Test product for last 1>'
        ])

    def test_shop_product_list_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/products/') 
        self.assertEqual(resp.status_code, 200)

    def test_shop_product_list_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)

    def test_shop_product_list_view_uses_correct_template(self):
        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'shop/product/list.html')

    def test_shop_product_detail_view_url_exists_at_desired_location(self):

        create_product('Test product for detail', 'test-product-for-detail')
        product = Product.objects.get(name='Test product for detail')
        product_id = str(product.id)
        product_slug = str(product.slug)

        resp = self.client.get('/products/' + product_id + '/' + product_slug + '/')
