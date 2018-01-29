from callback.forms import CallbackForm
from cart.forms import CartAddProductForm
from django.contrib.auth.models import User
from django.test import TestCase
from shop.models import Category, Manufacturer, Product
from wishlist.forms import WishlistForm

def create_product(name, slug): 
    category = Category.objects.create(name='Test category')
    manufacturer = Manufacturer.objects.create(name='Test manufacturer')
    Product.objects.create(name=name, image='1.jpg', category=category, manufacturer=manufacturer, 
    year_of_issue=2017, description='test description', price=1000, discount=10, price_with_discount=0, available=True, slug=slug)


class CallbackFormTest(TestCase):

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

    def test_callback_form_send_mail_subject(self):
        form_data = {'subject': 'Заявка на звонок'}
        form = CallbackForm(data=form_data)
        self.assertFalse(form.is_valid())

class CartAddProductFormTest(TestCase):

    def test_cart_add_product_form_quantity_label(self):
        form = CartAddProductForm()        
        self.assertTrue(form.fields['quantity'].label, 'Количество')

    def test_cart_add_product_form_quantity_choices(self):
        PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
        form = CartAddProductForm()        
        self.assertTrue(form.fields['quantity'].choices, PRODUCT_QUANTITY_CHOICES)

    def test_cart_add_product_form_quantity_coerce(self):
        form = CartAddProductForm()        
        self.assertTrue(form.fields['quantity'].coerce, int)

    def test_cart_add_product_form_update_required(self):
        form = CartAddProductForm()        
        self.assertFalse(form.fields['update'].required, False)

    def test_cart_add_product_form_update_initial(self):
        form = CartAddProductForm()        
        self.assertFalse(form.fields['update'].initial, False)

    def test_cart_add_product_form_update_widget(self):
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
