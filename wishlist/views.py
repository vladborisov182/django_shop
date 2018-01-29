from django.contrib import auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Product
from wishlist.forms import WishlistForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def wishlist_add(request, product_id):
    user = auth.get_user(request)
    product = get_object_or_404(Product, id=product_id)
    form = WishlistForm(request.POST)

    if form.is_valid():
        form.save(user=user, product=product)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def wishlist_del(request, product_id):
    user = auth.get_user(request)
    product = get_object_or_404(Product, id=product_id)
    form = WishlistForm(request.POST)

    if form.is_valid():
        form.delete(user=user, product=product)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def wishlist_detail(request):
    wishlist_items = request.user.wishlist_items.all()
    paginator = Paginator(wishlist_items, 4)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'wishlist/wishlist_items.html', {
        'products' : products,
})
