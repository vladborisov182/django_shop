from cart.cart import Cart
from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Product


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:CartDetail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})
