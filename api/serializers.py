from shop.models import Product, Manufacturer, Category
from rest_framework import serializers


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="api:manufacturer-detail")

    class Meta:
        model = Manufacturer
        fields = ('url', 'name')

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="api:category-detail")

    class Meta:
        model = Category
        fields = ('url', 'name')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="api:product-detail")
    manufacturer = ManufacturerSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('url', 'name', 'category', 'price', 'manufacturer', 'year_of_issue')