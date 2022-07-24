from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, StringRelatedField

from inventory import models


class StoreSerializer(ModelSerializer):
    class Meta:
        model = models.Store
        fields = '__all__'


class OfferSerializer(ModelSerializer):
    class Meta:
        model = models.Offer
        exclude = ['id']


class StoreInventorySerializer(ModelSerializer):
    store = StringRelatedField()
    class Meta:
        model = models.StoreInventory
        fields = ['store', 'stock']


class ProductSerializer(ModelSerializer):
    inventory = StoreInventorySerializer(many=True, read_only=True, allow_null=True)
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response

    class Meta:
        model = models.Product
        exclude = ['created_at']
