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
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Store)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StoreInventory)
class BrandAdmin(admin.ModelAdmin):
    pass
