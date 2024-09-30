from django.db import models
from Account.models import Account
from Recipe.models import Recipes
from services.mixin import DateMixin



class Wishlist(DateMixin):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ManyToManyField(Recipes)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlist'


class Basket(DateMixin):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.pk}"

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Basket'


class BasketItem(DateMixin):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name="basket_items")
    price = models.FloatField(default=0)
    count = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    def __str__(self):
        return self.basket.user.get_full_name()

    class Meta:
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Item'


class Order(DateMixin):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    total_price = models.FloatField()

    def __str__(self):
        return self.basket.user.get_full_name()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'