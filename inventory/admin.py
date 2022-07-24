from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from inventory import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    pass


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(models.Retailer)
class RetailerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_select_related = ['retailer']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Offer)
class OfferAdmin(admin.ModelAdmin):
    list_select_related = ['product']
    list_display = ['amount', 'valid_till']


@admin.register(models.StoreInventory)
class StoreInventoryAdmin(admin.ModelAdmin):
    list_select_related = ['product', 'store']
    list_display = ['product', 'store', 'stock']
    verbose_name_plural = 'Store inventory'
