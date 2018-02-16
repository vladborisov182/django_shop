from api import views
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet),
router.register(r'wishlist_items', views.UserViewSet),

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]
