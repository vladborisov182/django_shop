from cart.forms import CartAddProductForm
from django.contrib import auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from wishlist.forms import WishlistForm

from .filters import ProductFilter
from .models import Product


def ProductList(request):
    products_list = Product.objects.filter(available=True, created__lte=timezone.now()).order_by('-created')
    product_filter = ProductFilter(request.GET, queryset=products_list)

    user = auth.get_user(request)

    last_products = products_list[:4]

    paginator = Paginator(product_filter.qs, 6)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/product/list.html', {
        'filter' : product_filter,
        'products' : products,
        'last_products' : last_products,
        'user' : user,
})


def ProductDetail(request, id, slug):
    user = auth.get_user(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    wishlist_form = WishlistForm()
    in_wish = user in product.wishlisted.all()
    return render(request, 'shop/product/detail.html', {
        'product' : product,
        'user' : user,
        'cart_product_form': cart_product_form,
        'wishlist_form': wishlist_form,
        'in_wish' : in_wish,
})
