import django_filters.rest_framework
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from shop.models import Category, Manufacturer, Product

from shop.filters import ProductFilter
from .serializers import (CategorySerializer, ManufacturerSerializer,
                          ProductSerializer)


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created')
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    filter_backends = (DjangoFilterBackend,)
