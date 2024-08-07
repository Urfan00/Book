from rest_framework.views import APIView
from Recipe.api.serializers import RecipesCreateSerializers, RecipesReadSerializers
from Recipe.models import Recipes
from rest_framework.response import Response



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




