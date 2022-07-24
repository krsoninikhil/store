from rest_framework.serializers import ModelSerializer, SerializerMethodField, StringRelatedField

from inventory import models


class OfferListSerializer(ModelSerializer):
    class Meta:
        model = models.Offer
        fields = ['amount', 'valid_till']


class StoreSerializer(ModelSerializer):
    retailer = StringRelatedField()

    class Meta:
        model = models.Store
        exclude = ['created_at', 'updated_at']


class StoreInventorySerializer(ModelSerializer):
    store = StoreSerializer()
    offers = SerializerMethodField()

    def get_offers(self, obj):
        offers = models.Offer.objects.filter(store=obj.store_id, product=obj.product_id)
        return OfferListSerializer(offers, many=True).data

    class Meta:
        model = models.StoreInventory
        exclude = ['id', 'created_at', 'updated_at', 'product']


class ProductSerializer(ModelSerializer):
    inventory = StoreInventorySerializer(many=True, read_only=True, allow_null=True)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

    class Meta:
        model = models.Product
        exclude = ['created_at']


class OfferCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Offer
        exclude = []
