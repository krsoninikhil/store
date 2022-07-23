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
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StoreInventory)
class StoreInventoryAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Store inventory'
