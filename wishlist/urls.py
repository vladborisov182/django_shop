from django.conf.urls import url
from wishlist import views

urlpatterns = [
    url(r'^$', views.WishlistDetail, name='WishlistDetail'),
    url(r'^wishadd/(?P<product_id>\d+)/$', views.WishlistAdd, name='WishlistAdd'),
    url(r'^wishdel/(?P<product_id>\d+)/$', views.WishlistDel, name='WishlistDel'),
]
