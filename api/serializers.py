from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="api:product-detail")
    manufacturer = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('url', 'name', 'price', 'year_of_issue', 'category', 'manufacturer')