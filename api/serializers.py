from django.contrib.auth.models import User
from rest_framework.serializers import (HyperlinkedIdentityField,
                                        ModelSerializer, StringRelatedField)
from shop.models import Product


class ProductSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(view_name="api:product-detail")
    manufacturer = StringRelatedField()
    category = StringRelatedField()

    class Meta:
        model = Product
        fields = ('url', 'name', 'price', 'year_of_issue', 'category', 'manufacturer')

class UserSerializer(ModelSerializer):

    wishlist_items = ProductSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'wishlist_items')
