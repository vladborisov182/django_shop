from cart import views
from django.conf.urls import url

urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='CartAdd'),
    url(r'^$', views.cart_detail, name='CartDetail'),
]
