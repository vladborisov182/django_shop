from django.conf.urls import url
from shop import views

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='ProductDetail'),
    url(r'^$', views.product_list, name='ProductList'),
]
