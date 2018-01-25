from django.conf.urls import url
from wishlist import views

urlpatterns = [
    url(r'^$', views.wishlist_detail, name='WishlistDetail'),
    url(r'^wishadd/(?P<product_id>\d+)/$', views.wishlist_add, name='WishlistAdd'),
    url(r'^wishdel/(?P<product_id>\d+)/$', views.wishlist_del, name='WishlistDel'),
]
