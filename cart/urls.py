from cart import views
from django.conf.urls import url

urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    url(r'^$', views.CartDetail, name='CartDetail'),
]
