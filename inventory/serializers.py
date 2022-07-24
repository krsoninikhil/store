from rest_framework.serializers import ModelSerializer, SerializerMethodField, \
    StringRelatedField, ValidationError, CharField, EmailField
from rest_framework import serializers
from django.db.utils import IntegrityError

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
    store = SerializerMethodField()

    def create(self, validated_data):
        user =  self.context['request'].user
        validated_data['store'] = user.store if hasattr(user, 'store') else None
        return super().create(validated_data)


    def get_store(self, obj):
        user = self.context['request'].user
        return user.store.id if hasattr(user, 'store') else None

    class Meta:
        model = models.Offer
        exclude = []


class UserSerializer(ModelSerializer):
    first_name = CharField(max_length=256, required=True)
    last_name = CharField(max_length=256, required=True)
    email = EmailField(required=True)

    def create(self, validated_data):
        user = models.User(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])

        try:
            user.save()
        except IntegrityError:
            raise ValidationError('Duplicate username')
        return user

    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'email': {'required': True}}
