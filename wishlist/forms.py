from django import forms
from shop.models import Product


class WishlistForm(forms.Form):

    def save(self, user, product):
        product.wishlisted.add(user)
        
    def delete(self, user, product):
        product.wishlisted.remove(user)
