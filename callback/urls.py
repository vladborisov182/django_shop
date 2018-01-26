from callback import views
from django.conf.urls import url

urlpatterns = [
    url(r'^callback/', views.call_back, name='Callback'),
]
