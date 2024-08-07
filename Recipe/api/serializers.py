from rest_framework import serializers
from Recipe.models import Recipes
from Story.models import Category, Tag


class CategorySeralizers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['image', 'is_active']


class TagSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class RecipesReadSerializers(serializers.ModelSerializer):
    category = CategorySeralizers()
    tag = TagSeralizers(many=True)

    class Meta:
        model = Recipes
        fields = ['id', 'title', 'image', 'category', 'tag', 'user']


class RecipesCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id', 'title', 'image', 'category', 'tag', 'user']
