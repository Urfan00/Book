from django.urls import path
from Order.api.views import WishlistAPI


urlpatterns = [
    path('wishlist/', WishlistAPI.as_view(), name='wishlists'),

]