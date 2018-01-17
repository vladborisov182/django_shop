from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^$', views.ProductList, name='ProductList'),
    url(r'^search/$', views.ProductList, name='ProductListSearch'),
]
