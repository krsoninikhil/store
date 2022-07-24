from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from inventory import models, serializers


class ProductView(GenericViewSet, RetrieveModelMixin, ListModelMixin):

    serializer_class = serializers.ProductSerializer


    def get_queryset(self):
        qs = models.Product.objects.all().prefetch_related('inventory')

        brand = self.request.query_params.get('brand')
        if brand:
            qs = qs.filter(brand=brand)

        store = self.request.query_params.get('store')
        if store:
            qs = qs.filter(inventory__store=store)

        retailer = self.request.query_params.get('retailer')
        if retailer:
            qs = qs.filter(inventory__store__retailer=retailer)

        return qs
