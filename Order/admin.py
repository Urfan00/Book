from django.contrib import admin
from .models import Basket, BasketItem, Order, Wishlist
from import_export.admin import ImportExportModelAdmin



class WishlistAdmin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'created_at', 'updated_at']
    list_display_links = ['id', 'user']
    filter_horizontal = ['product']
    search_fields = ['user__username', 'product__title']
    list_filter = ['created_at', 'updated_at']


class BasketAdmin(ImportExportModelAdmin):
    list_display = ['id', 'user', 'status', 'created_at', 'updated_at']
    list_display_links = ['id', 'user']
    search_fields = ['user__username']
    list_filter = ['status', 'created_at', 'updated_at']


class BasketItemAdmin(ImportExportModelAdmin):
    list_display = ['id', 'basket', 'price', 'count', 'product', 'created_at', 'updated_at']
    list_display_links = ['id', 'basket']
    search_fields = ['basket__user__username', 'product__title']
    list_filter = ['created_at', 'updated_at']


class OrderAdmin(ImportExportModelAdmin):
    list_display = ['id', 'basket', 'total_price', 'created_at', 'updated_at']
    list_display_links = ['id', 'basket']
    search_fields = ['basket__user__username']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketItem, BasketItemAdmin)
admin.site.register(Order, OrderAdmin)


