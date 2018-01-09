from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filter import ProductFilter

# Страница с товарами
def ProductList(request):
    products_list = Product.objects.filter(available=True, created__lte=timezone.now()).order_by('-created')
    product_filter = ProductFilter(request.GET, queryset=products_list)

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
        'last_products' : last_products
})

# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product' : product})




