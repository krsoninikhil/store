from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=False)
# router.register('brands', views.BrandView)

urlpatterns = [
    path('', include(router.urls)),
]
