from django.contrib.auth.models import User
from rest_framework import serializers
from shop.models import Category, Manufacturer, Product


class ManufacturerSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="api:manufacturer-detail")

    class Meta:
        model = Manufacturer
        fields = ('url', 'name')

class CategorySerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="api:category-detail")

    class Meta:
        model = Category
        fields = ('url', 'name')


class ProductSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="api:product-detail")
    manufacturer = ManufacturerSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('url', 'name', 'price', 'year_of_issue', 'manufacturer', 'category')
