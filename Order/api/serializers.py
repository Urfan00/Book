from rest_framework import serializers
from Order.models import Wishlist
from Recipe.models import Recipes


class ProductFORWishlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipes
        fields = ['id', 'title', 'image', 'show_date']


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductFORWishlistSerializer(many=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'product']
