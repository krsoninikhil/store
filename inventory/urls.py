from django.urls import path, include
from rest_framework.routers import DefaultRouter

from inventory import views


router = DefaultRouter(trailing_slash=False)
router.register('products', views.ProductView, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
