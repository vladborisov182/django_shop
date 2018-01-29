from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from shop.filter import ProductFilter
from shop.models import Product
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created')
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticatedOrReadOnly,)