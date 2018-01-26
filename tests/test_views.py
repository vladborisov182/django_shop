from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase


class ProductListViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/products/') 
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('shop:ProductList'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'shop/product/list.html')


class WishListViewTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(username='testuser', password='12345') 
        test_user.save()
        login = self.client.login(username='testuser', password='12345')

    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/wishlist/') 
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('wishlist:WishlistDetail'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('wishlist:WishlistDetail'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'wishlist/wishlist_items.html')
