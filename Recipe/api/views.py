import django_filters.rest_framework
from rest_framework import filters
from rest_framework.views import APIView
from Recipe.api.pagination import LargePageNumberPagination, SmallPageNumberPagination
from Recipe.api.serializers import CategorySeralizers, RecipesCreateSerializers, RecipesReadSerializers
from Recipe.models import Recipes
from rest_framework.response import Response
from Story.models import Category
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class CategoryAPIView(APIView):

    def get(self, request, *args, **kwargs):

        categories = Category.objects.filter(is_active=True).all()
        serializers = CategorySeralizers(categories, context = {'request': request}, many=True)
        return Response(serializers.data)


class RecipeAPI(APIView):

    def get(self, request, *args, **kwargs):

        recipes = Recipes.objects.all()
        serializers = RecipesReadSerializers(recipes, context = {'request': request}, many=True)

        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = RecipesCreateSerializers(data=request.data, context={'request': request})

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)


class GenericAPIViewSerializerMixin:
    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


class RecipeListCreateAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # pagination_class = LargePageNumberPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tag', 'user', 'category']
    search_fields = ['title']
    ordering_fields = ['id', 'created_at']
    queryset = Recipes.objects.all()
    serializer_classes = {
        'GET' : RecipesReadSerializers,
        'POST' : RecipesCreateSerializers
    }


class RecipeRetrieveUpdateDestroyAPI(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_classes = {
        'GET' : RecipesReadSerializers,
        'PUT' : RecipesCreateSerializers,
        'PATCH' : RecipesCreateSerializers
    }


class RecipeReadUpdateDeleteView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        recipe = Recipes.objects.get(id=id)
        serializer = RecipesReadSerializers(recipe)
        return Response(serializer.data, status=200)

    def put(self, request, *args, **kwargs):
        id = kwargs['pk']
        recipe = Recipes.objects.get(id=id)
        recipe_data = request.data
        serializer = RecipesCreateSerializers(data=recipe_data, instance=recipe)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, *args, **kwargs):
        id = kwargs['pk']
        recipe = Recipes.objects.get(id=id)
        recipe_data = request.data
        serializer = RecipesCreateSerializers(data=recipe_data, partial=True, instance=recipe)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, *args, **kwargs):
        id = kwargs['pk']
        recipe = Recipes.objects.get(id=id)
        recipe.delete()
        return Response(status=204)




