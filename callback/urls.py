from django.conf.urls import url, include
from callback import views


urlpatterns = [
    url(r'^callback/', views.Callback, name='Callback'),
]