from rest_framework import serializers
from Order.models import Basket, BasketItem, Wishlist
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


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductFORWishlistSerializer()

    class Meta:
        model = BasketItem
        fields = ['id', 'basket', 'product', 'count', 'price', 'created_at', 'updated_at']


class BasketSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    basket_items = BasketItemSerializer(many=True)

    class Meta:
        model = Basket
        fields = ['id', 'user', 'status', 'basket_items', 'created_at', 'updated_at']
