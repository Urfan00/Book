from django.urls import path
from Order.api.views import BasketAPI, WishlistAPI


urlpatterns = [
    path('wishlist/', WishlistAPI.as_view(), name='wishlists'),
    path('basket/', BasketAPI.as_view(), name='basket'),

]
