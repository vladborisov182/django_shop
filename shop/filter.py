import django_filters

from .models import Category, Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Название')

    min_year = django_filters.NumberFilter(name="year_of_issue", lookup_expr='gte', label='Год выпуска от ')
    max_year = django_filters.NumberFilter(name="year_of_issue", lookup_expr='lte', label='Год выпуска до ')

    min_price = django_filters.NumberFilter(name="price_with_discount", lookup_expr='gte', label='Цена от')
    max_price = django_filters.NumberFilter(name="price_with_discount", lookup_expr='lte', label='Цена до')

    
    class Meta:
        model = Product
        fields = ['category', 'manufacturer']
