from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products_list = Product.objects.filter(available=True, created__lte=timezone.now()).order_by('-created')

    question = request.GET.get('q')

    if question:
        products_list = Product.objects.filter(available=True, created__lte=timezone.now(), name__icontains=question).order_by('-created')

    elif category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)

    paginator = Paginator(products_list, 3)

    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/product/list.html', {
        'category' : category,
        'categories' : categories,
        'products' : products,
})

# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product' : product})




