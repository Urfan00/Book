from rest_framework.views import APIView

from Recipe.models import Recipes
from .serializers import WishlistSerializer
from Order.models import Wishlist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class WishlistAPI(APIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        print('ok111')
        obj, created = Wishlist.objects.get_or_create(user = request.user)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product_id = "1"
        print('ok', product_id)
        product = Recipes.objects.filter(pk=product_id).first()

        if product and self.request.user.is_authenticated:
            wishlist1, created = Wishlist.objects.get_or_create(user_id = request.user)
            wishlist2 = Wishlist.objects.filter(user_id = request.user).first()
            wishlist2.product.add(product)
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        ProductID = '1'
        print('delete', ProductID)
        if ProductID:
            user_wishlist = Wishlist.objects.get(user_id = self.request.user)
            product = user_wishlist.product.get(id = ProductID)
            user_wishlist.product.remove(product.id)
        return Response(status = status.HTTP_200_OK)
