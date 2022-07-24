from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from inventory import models, serializers


class StoreInventoryView(GenericViewSet, ListModelMixin):

    serializer = serializers.StoreInventorySerializer

    def get_queryset(self, request):
        qs = StoreInventory.objects.all()

        brand = request.query_params('brand')
        if brand:
            qs = qs.filter(product__brand=brand)

        store = request.query_params('store')
        if store:
            qs = qs.filter(store=store)

        retailer = request.query_params('retailer')
        if retailer:
            qs = qs.filter(store__retailer=retailer)


class ProductView(GenericViewSet, RetrieveModelMixin):

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
