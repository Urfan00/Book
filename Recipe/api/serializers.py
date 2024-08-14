from rest_framework import serializers
from Recipe.models import Recipes
from Story.models import Category, Tag


class CategorySeralizers(serializers.ModelSerializer):
    # recipes = serializers.SerializerMethodField()

    class Meta:
        model = Category
        # fields = ['id', 'name', 'image', 'is_active', 'recipes']
        fields = ['id', 'name', 'image', 'is_active']

    # def get_recipes(self, obj):
    #     serializer = RecipesCreateSerializers(obj.recipe_category.all(), context=self.context, many=True)
    #     return serializer.data


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
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Recipes
        fields = ['id', 'title', 'image', 'category', 'tag', 'user']

    def validate(self, attrs):
        request = self.context['request']
        attrs['user'] = request.user
        return super().validate(attrs)
