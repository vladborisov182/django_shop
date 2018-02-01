from tests.product_creator import create_product

from callback.forms import CallbackForm
from cart.forms import CartAddProductForm
from django.contrib.auth.models import User
from django.test import TestCase
from shop.models import Product


class CallbackFormTest(TestCase):

    def test_callback_form_with_no_name_and_phone(self):
        form = CallbackForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['Это поле обязательно.'],
            'phone': ['Это поле обязательно.'],
        })

    '''def test_callback_form_with_no_phone(self):
        response = self.client.post("/callback/", {'name' : 'Leela'})
        self.assertFormError(response, 'form', 'phone', 'Это поле обязательно.')'''

    def test_callback_form_with_no_phone(self):
        form = CallbackForm({'name' : 'Leela'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'phone': ['Это поле обязательно.'],
        })

    '''def test_callback_form_with_no_name(self):
        response = self.client.post("/callback/", {'phone' : '+380123456789'})
        self.assertFormError(response, 'form', 'name', 'Это поле обязательно.')'''

    def test_callback_form_with_no_name(self):
        form = CallbackForm({'phone' : '+380123456789'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['Это поле обязательно.'],
        })

    def test_callback_form_with_name_and_phone(self): 
        form = CallbackForm({
            'name': "Leela",
            'phone': "+380123456789",
        })
        self.assertTrue(form.is_valid())

    def test_callback_form_name_field_label(self):
        form = CallbackForm()        
        self.assertTrue(form.fields['name'].label, 'Имя')

    def test_callback_form_name_field_label_length(self):
        form = CallbackForm()    
        self.assertTrue(form.fields['name'].max_length, 50)

    def test_callback_form_name_placeholder(self):
        form = CallbackForm() 
        self.assertEqual(form.fields['name'].widget.attrs['placeholder'], 'Имя')

    def test_callback_form_name_class(self):
        form = CallbackForm() 
        self.assertEqual(form.fields['name'].widget.attrs['class'], 'form-control')

    def test_callback_form_name_title(self):
        form = CallbackForm() 
        self.assertEqual(form.fields['name'].widget.attrs['title'], 'Ваше имя')

    def test_callback_form_phone_field_label(self):
        form = CallbackForm()        
        self.assertTrue(form.fields['phone'].label, 'Номер телефона')

    def test_callback_form_phone_placeholder(self):
        form = CallbackForm() 
        self.assertEqual(form.fields['phone'].widget.attrs['placeholder'], 'Телефон')

    def test_callback_form_phone_required(self):
        form = CallbackForm() 
        self.assertEqual(form.fields['phone'].widget.attrs['required'], 'True')

    def test_callback_form_phone_class(self):
        form = CallbackForm() 
        self.assertEqual(form.fields['phone'].widget.attrs['class'], 'form-control')

    def test_callback_form_phone_title(self):
        form = CallbackForm() 
        self.assertEqual(form.fields['phone'].widget.attrs['title'], 'Пример: 80XXYYYYYYY')

class CartFormTest(TestCase):

    def test_cart_form_with_no_quantity(self):
        form = CartAddProductForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'quantity': ['Это поле обязательно.'],
        })

    def test_cart_form_with_excess_of_quantity(self): 
        form = CallbackForm({
            'quantity': "21",
        })
        self.assertFalse(form.is_valid())

    def test_cart_form_with_normal_quantity(self): 
        form = CallbackForm({
            'quantity': "1",
        })
        self.assertFalse(form.is_valid())

    def test_cart_form_quantity_label(self):
        form = CartAddProductForm()        
        self.assertTrue(form.fields['quantity'].label, 'Количество')

    def test_cart_form_quantity_choices(self):
        PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
        form = CartAddProductForm()        
        self.assertTrue(form.fields['quantity'].choices, PRODUCT_QUANTITY_CHOICES)

    def test_cart_form_quantity_coerce(self):
        form = CartAddProductForm()        
        self.assertTrue(form.fields['quantity'].coerce, int)

    def test_cart_form_update_required(self):
        form = CartAddProductForm()        
        self.assertFalse(form.fields['update'].required, False)

    def test_cart_form_update_initial(self):
        form = CartAddProductForm()        
        self.assertFalse(form.fields['update'].initial, False)

    def test_cart_form_update_widget(self):
        form = CartAddProductForm()        
        self.assertTrue(form.fields['update'].widget, 'forms.HiddenInput')


class WishlistFormTest(TestCase):

    def test_wishlist_items_add(self):
        user1 = User.objects.create()

        create_product('Test wishlist', 'test-slug')
        product = Product.objects.get(name='Test wishlist')
        product_name = product.name
        product.wishlisted.add(user1)
        
        wishlist_items = user1.wishlist_items.all()

        self.assertQuerysetEqual(wishlist_items, [
            '<Product: ' + product_name + '>'
        ])

    def test_wishlist_items_del(self):
        user1 = User.objects.create()

        create_product('Test wishlist', 'test-slug')
        product = Product.objects.get(name='Test wishlist')
        product.wishlisted.remove(user1)
        
        wishlist_items = user1.wishlist_items.all()

        self.assertQuerysetEqual(wishlist_items, [])
    